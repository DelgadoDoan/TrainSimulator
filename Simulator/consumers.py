import json
import asyncio
import math
import random
from .info import users, TRAIN_SPEED, TRAINS, STATIONS
from channels.generic.websocket import AsyncWebsocketConsumer


class TrainConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "train_simulation_server"
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()
        self.is_host = False
        self.active_tasks = []

        if not users:
            users["user"] = "server"
            self.is_host = True
            
            await self.channel_layer.send(
                self.channel_name, {
                    "type": "send_message",
                    "message": "This is the host server...",
                }
            )  
            await self.start_sim()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        for task in self.active_tasks:
            task.cancel()
        if self.is_host:
            del users["user"]


    async def start_sim(self):        
        # Group trains that are from the same end
        lrt1_left_trains = [train for train in TRAINS if train["platform_side"] == "left" and train["line"] == "LRT-1"]
        lrt1_right_trains = [train for train in TRAINS if train["platform_side"] == "right" and train["line"] == "LRT-1"]
        lrt2_left_trains = [train for train in TRAINS if train["platform_side"] == "left" and train["line"] == "LRT-2"]
        lrt2_right_trains = [train for train in TRAINS if train["platform_side"] == "right" and train["line"] == "LRT-2"]
        mrt3_left_trains = [train for train in TRAINS if train["platform_side"] == "left" and train["line"] == "MRT-3"]
        mrt3_right_trains = [train for train in TRAINS if train["platform_side"] == "right" and train["line"] == "MRT-3"]

        if not self.active_tasks:
            self.active_tasks.append(asyncio.create_task(self.send_data()))
            self.active_tasks.append(asyncio.create_task(self.start_line(lrt1_left_trains, STATIONS["LRT-1"])))
            self.active_tasks.append(asyncio.create_task(self.start_line(lrt1_right_trains, STATIONS["LRT-1"])))
            self.active_tasks.append(asyncio.create_task(self.start_line(lrt2_left_trains, STATIONS["LRT-2"])))
            self.active_tasks.append(asyncio.create_task(self.start_line(lrt2_right_trains, STATIONS["LRT-2"])))
            self.active_tasks.append(asyncio.create_task(self.start_line(mrt3_left_trains, STATIONS["MRT-3"])))
            self.active_tasks.append(asyncio.create_task(self.start_line(mrt3_right_trains, STATIONS["MRT-3"])))


    async def send_data(self):
        while True:
            await self.calculate_etas(STATIONS, TRAINS)
            
            await self.channel_layer.group_send(
                self.group_name, {
                    "type": "send_message",
                    "message": {
                        "trains": TRAINS,
                        "stations": [{"left_eta": s["left_eta"], "right_eta": s["right_eta"]} for l in STATIONS for s in STATIONS[l]],
                    },
                }
            )
            await asyncio.sleep(5)  # Send data every 5 seconds
    
    
    async def send_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))


    async def start_line(self, trains, route):
        for train in trains:
            self.active_tasks.append(asyncio.create_task(self.run_train(train, route)))
            await asyncio.sleep(random.randint(180, 300))  # Wait until sending the next train


    async def calculate_etas(self, stations, trains):
        for line in stations:
            for station in stations[line]:
                left_etas = []
                right_etas = []

                for train in trains:
                    if station["id"] == 1:  # Simulate unable to get ETA
                        continue

                    # Get distance from station to train
                    dx = station["loc"]["x"] - train["pos"]["x"]
                    dy = station["loc"]["y"] - train["pos"]["y"]
                    dist = math.sqrt(dx**2 + dy**2)

                    # Get train velocity (assumed constant velocity for each train)
                    if dist == 0:
                        eta = 0
                    else:
                        vx = TRAIN_SPEED * dx/dist
                        vy = TRAIN_SPEED * dy/dist
                        v = math.sqrt(vx**2 + vy**2)

                        # Estimate ETA of train to station
                        eta = dist / v

                    if train["platform_side"] == "left":
                        left_etas.append(eta)
                    else:
                        right_etas.append(eta)
                
                # Get mimimum etas
                station["left_eta"] = min(left_etas) if left_etas else None
                station["right_eta"] = min(right_etas) if right_etas else None
           

    async def run_train(self, train, route):
        r = route.copy()

        if train["platform_side"] == "left":
            r.reverse()
        
        i = r.index(train["next_station"]) - 1
        
        while True:
            await asyncio.sleep(1)  # Update position every 1s
            if i < len(r) - 1:
                train["status"] = "running"
                
                # Get distance to travel to next station
                dx = r[i+1]["loc"]["x"] - r[i]["loc"]["x"]
                dy = r[i+1]["loc"]["y"] - r[i]["loc"]["y"]
                dist = math.sqrt(dx**2 + dy**2)

                # Get train velocity
                vx = TRAIN_SPEED * dx/dist
                vy = TRAIN_SPEED * dy/dist

                # Get distance remaining from current position towards next station
                dist_left = math.sqrt((r[i+1]["loc"]["x"] - train["pos"]["x"])**2 + (r[i+1]["loc"]["y"] - train["pos"]["y"])**2)

                # If train has arrived
                if dist_left <= TRAIN_SPEED:
                    i += 1
                    train["status"] = "idle"
                    train["pos"]["x"] = r[i]["loc"]["x"]
                    train["pos"]["y"] = r[i]["loc"]["y"]

                    if i < len(r) - 1:
                        train["next_station"] = r[i+1]
                    
                    await asyncio.sleep(random.randint(60, 120))  # Train stops for 60s - 120s
                else:
                    # If train has not yet arrived
                    train["pos"]["x"] += vx
                    train["pos"]["y"] += vy
            else:
                train["platform_side"] = "left" if train["platform_side"] == "right" else "right"
                train["status"] = "idle"

                r.reverse()
                i = 0
                train["next_station"] = r[i+1]
                               
                await asyncio.sleep(random.randint(120, 180))  # Train stops for 120s - 180s
  