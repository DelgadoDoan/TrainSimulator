const socket = new WebSocket('wss://trensimph.up.railway.app/ws/simulator');
// 'wss://trensimph.up.railway.app/ws/simulator'
// 'ws://127.0.0.1:8000/ws/simulator'

let trains = {};

const scale = 750 / 25;
const offsetX = 1500 / 3;
const offsetY = 750 / 20;

lrt1Line = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 1.87},
    {"x": 0, "y": 4.12},
    {"x": 0, "y": 5.207},
    {"x": 0, "y": 6.161},
    {"x": 0, "y": 6.821},
    {"x": 0, "y": 7.748},
    {"x": 0, "y": 8.419},
    {"x": 0, "y": 9.037},
    {"x": 0, "y": 9.685},
    {"x": 0, "y": 10.37},
    {"x": 0, "y": 11.095},
    {"x": 0, "y": 12.309},
    {"x": 0, "y": 13.063},
    {"x": 0, "y": 13.857},
    {"x": 0, "y": 14.684},
    {"x": 0, "y": 15.745},
    {"x": 0, "y": 16.475},
    {"x": 0, "y": 17.485},
    {"x": 0, "y": 18.073},
]

lrt2Line = [
    {"x": 0, "y": 9.685},
    {"x": 1.05, "y": 9.685},
    {"x": 2.439, "y": 9.685},
    {"x": 3.796, "y": 9.685},
    {"x": 5.03, "y": 9.685},
    {"x": 5.958, "y": 9.685},
    {"x": 7.033, "y": 9.685},
    {"x": 8.197, "y": 9.685},
    {"x": 9.635, "y": 9.685},
    {"x": 10.59, "y": 9.685},
    {"x": 12.56, "y": 9.685},
    {"x": 13.683, "y": 9.685},
    {"x": 15.967, "y": 9.685},
]

mrt3Line = [
    {"x": 8.197, "y": 5.675},
    {"x": 8.197, "y": 6.895},
    {"x": 8.197, "y": 7.835},
    {"x": 8.197, "y": 9.685},
    {"x": 8.197, "y": 11.135},
    {"x": 8.197, "y": 13.445},
    {"x": 8.197, "y": 14.215},
    {"x": 8.197, "y": 15.195},
    {"x": 8.197, "y": 15.965},
    {"x": 8.197, "y": 17.795},
    {"x": 8.197, "y": 18.675},
    {"x": 8.197, "y": 19.865},
    {"x": 8.197, "y": 21.755},
]


socket.onopen = () => {
    console.log("Connected");

    const c = document.getElementById("canvas");
    const ctx = c.getContext("2d");

    c.width = 1500;
    c.height = 750;


    drawRoutes = (line, color) => {
        ctx.beginPath();
        ctx.moveTo(line[0].x * scale + offsetX, line[0].y * scale + offsetY);

        for (let i = 1; i < line.length; i++) {
            ctx.lineTo(line[i].x * scale + offsetX, line[i].y * scale + offsetY);
        }
        
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;

        ctx.closePath();
        ctx.stroke();
    }


    drawStations = (line, color) => {
        for (let i = 0; i < line.length; i++) { 
            let newBox = document.createElement("div");
            newBox.classList.add("station");
            newBox.id = `box-${i}`;
        
            newBox.style.left = `${line[i].x * scale + offsetX - 5}px`;
            newBox.style.top = `${line[i].y * scale+ offsetY - 5}px`;
            newBox.style.background = color
        
            let label = document.createElement("span");
            newBox.appendChild(label);
        
            document.body.appendChild(newBox);
        }
    }


    drawRoutes(lrt1Line, "yellow");
    drawRoutes(lrt2Line, "purple");
    drawRoutes(mrt3Line, "blue");
    drawStations(lrt1Line, "yellow");
    drawStations(lrt2Line, "purple");
    drawStations(mrt3Line, "blue");
};

socket.onmessage = (event) => {
    let data = JSON.parse(event.data);

    for (let train of data.message) {
        let trainId = train.id;
        let trainLine = train.line

        // If the box for this train does not exist, create it
        if (!trains[trainId]) {
            let trainContainer = document.createElement("div");
            trainContainer.classList.add("train-container");
            trainContainer.id = `${trainId}`; // Unique ID for each train

            let trainBox = document.createElement("div");
            trainBox.classList.add("train");
            trainContainer.appendChild(trainBox);
            trainBox.style.background = train.status === "running" ? "green" : "red";

            let label = document.createElement("div");
            label.classList.add("train-label");

            label.innerText = `Line: ${trainLine}\nID: ${trainId}\n`;
            trainContainer.appendChild(label)

            document.body.appendChild(trainContainer);
            trains[trainId] = trainContainer;
        }

        let newX = train.pos.x * scale + offsetX - 5; // Adjust scaling
        let newY = train.pos.y * scale + offsetY - 5;

        // Update train position
        trains[trainId].style.left = newX + "px";
        trains[trainId].style.top = newY + "px";

        let trainBox = trains[trainId].querySelector(".train");
        trainBox.style.background = train.status === "running" ? "green" : "red";    
    }
};


socket.onclose = () => {
    console.log("Disconnected");
};