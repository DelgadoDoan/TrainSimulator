TRAIN_SPEED = 0.015 # in km/s

TRAINS = [
    {"id": 1, "line": "LRT-1", "platform_side": "right", "pos": {"x": 0, "y": 0}, "status": "idle", "next_station": None, "eta": None},
    {"id": 2, "line": "LRT-1", "platform_side": "right", "pos": {"x": 0, "y": 0}, "status": "idle", "next_station": None, "eta": None},
    {"id": 3, "line": "LRT-1", "platform_side": "right", "pos": {"x": 0, "y": 0}, "status": "idle", "next_station": None, "eta": None},
    {"id": 4, "line": "LRT-1", "platform_side": "left", "pos": {"x": 0, "y": 18.073}, "status": "idle", "next_station": None, "eta": None},
    {"id": 5, "line": "LRT-1", "platform_side": "left", "pos": {"x": 0, "y": 18.073}, "status": "idle", "next_station": None, "eta": None},
    {"id": 6, "line": "LRT-1", "platform_side": "left", "pos": {"x": 0, "y": 18.073}, "status": "idle", "next_station": None, "eta": None},
    {"id": 7, "line": "LRT-2", "platform_side": "right", "pos": {"x": 0, "y": 9.685}, "status": "idle", "next_station": None, "eta": None},
    {"id": 8, "line": "LRT-2", "platform_side": "right", "pos": {"x": 0, "y": 9.685}, "status": "idle", "next_station": None, "eta": None},
    {"id": 9, "line": "LRT-2", "platform_side": "right", "pos": {"x": 0, "y": 9.685}, "status": "idle", "next_station": None, "eta": None},
    {"id": 10, "line": "LRT-2", "platform_side": "left", "pos": {"x": 15.967, "y": 9.685}, "status": "idle", "next_station": None, "eta": None},
    {"id": 11, "line": "LRT-2", "platform_side": "left", "pos": {"x": 15.967, "y": 9.685}, "status": "idle", "next_station": None, "eta": None},
    {"id": 12, "line": "LRT-2", "platform_side": "left", "pos": {"x": 15.967, "y": 9.685}, "status": "idle", "next_station": None, "eta": None},
    {"id": 13, "line": "MRT-3", "platform_side": "right", "pos": {"x": 8.197, "y": 5.675}, "status": "idle", "next_station": None, "eta": None},
    {"id": 14, "line": "MRT-3", "platform_side": "right", "pos": {"x": 8.197, "y": 5.675}, "status": "idle", "next_station": None, "eta": None},
    {"id": 15, "line": "MRT-3", "platform_side": "right", "pos": {"x": 8.197, "y": 5.675}, "status": "idle", "next_station": None, "eta": None},
    {"id": 16, "line": "MRT-3", "platform_side": "left", "pos": {"x": 8.197, "y": 21.755}, "status": "idle", "next_station": None, "eta": None},
    {"id": 17, "line": "MRT-3", "platform_side": "left", "pos": {"x": 8.197, "y": 21.755}, "status": "idle", "next_station": None, "eta": None},
    {"id": 18, "line": "MRT-3", "platform_side": "left", "pos": {"x": 8.197, "y": 21.755}, "status": "idle", "next_station": None, "eta": None},
]

ROUTES = {
    "LRT-1": [
        {"id": 1, "station_name": "Roosevelt", "loc": {"x": 0, "y": 0}},
        {"id": 2, "station_name": "Balintawak", "loc": {"x": 0, "y": 1.87}},
        {"id": 3, "station_name": "Monumento", "loc": {"x": 0, "y": 4.12}},
        {"id": 4, "station_name": "5th Avenue", "loc": {"x": 0, "y": 5.207}},
        {"id": 5, "station_name": "R. Papa", "loc": {"x": 0, "y": 6.161}},
        {"id": 6, "station_name": "Abad Santos", "loc": {"x": 0, "y": 6.821}},
        {"id": 7, "station_name": "Blumentrit", "loc": {"x": 0, "y": 7.748}},
        {"id": 8, "station_name": "Tayuman", "loc": {"x": 0, "y": 8.419}},
        {"id": 9, "station_name": "Bambang", "loc": {"x": 0, "y": 9.037}},
        {"id": 10, "station_name": "Doroteo Jose", "loc": {"x": 0, "y": 9.685}},
        {"id": 11, "station_name": "Carriedo", "loc": {"x": 0, "y": 10.37}},
        {"id": 12, "station_name": "Central Terminal", "loc": {"x": 0, "y": 11.095}},
        {"id": 13, "station_name": "United Nations", "loc": {"x": 0, "y": 12.309}},
        {"id": 14, "station_name": "Pedro Gil", "loc": {"x": 0, "y": 13.063}},
        {"id": 15, "station_name": "Quirino", "loc": {"x": 0, "y": 13.857}},
        {"id": 16, "station_name": "Vito Cruz", "loc": {"x": 0, "y": 14.684}},
        {"id": 17, "station_name": "Gil Puyat", "loc": {"x": 0, "y": 15.745}},
        {"id": 18, "station_name": "Libertad", "loc": {"x": 0, "y": 16.475}},
        {"id": 19, "station_name": "EDSA", "loc": {"x": 0, "y": 17.485}},
        {"id": 20, "station_name": "Baclaran", "loc": {"x": 0, "y": 18.073}},
    ], 
    "LRT-2": [
        {"id": 21, "station_name": "Recto", "loc": {"x": 0, "y": 9.685}},
        {"id": 22, "station_name": "Legarda", "loc": {"x": 1.05, "y": 9.685}},
        {"id": 23, "station_name": "Pureza", "loc": {"x": 2.439, "y": 9.685}},
        {"id": 24, "station_name": "V. Mapa", "loc": {"x": 3.796, "y": 9.685}},
        {"id": 25, "station_name": "J. Ruiz", "loc": {"x": 5.03, "y": 9.685}},
        {"id": 26, "station_name": "Gilmore", "loc": {"x": 5.958, "y": 9.685}},
        {"id": 27, "station_name": "Betty Go Belmonte", "loc": {"x": 7.033, "y": 9.685}},
        {"id": 28, "station_name": "Araneta-Cubao", "loc": {"x": 8.197, "y": 9.685}},
        {"id": 29, "station_name": "Anonas", "loc": {"x": 9.635, "y": 9.685}},
        {"id": 30, "station_name": "Katipunan", "loc": {"x": 10.59, "y": 9.685}},
        {"id": 31, "station_name": "Santolan", "loc": {"x": 12.56, "y": 9.685}},
        {"id": 32, "station_name": "Marikina", "loc": {"x": 13.683, "y": 9.685}},
        {"id": 33, "station_name": "Antipolo", "loc": {"x": 15.967, "y": 9.685}},
    ], 
    "MRT-3": [
        {"id": 34, "station_name": "North Avenue", "loc": {"x": 8.197, "y": 5.675}},
        {"id": 35, "station_name": "Quezon Avenue", "loc": {"x": 8.197, "y": 6.895}},
        {"id": 36, "station_name": "Kamuning", "loc": {"x": 8.197, "y": 7.835}},
        {"id": 37, "station_name": "Cubao", "loc": {"x": 8.197, "y": 9.685}},
        {"id": 38, "station_name": "Santolan", "loc": {"x": 8.197, "y": 11.135}},
        {"id": 39, "station_name": "Ortigas", "loc": {"x": 8.197, "y": 13.445}},
        {"id": 40, "station_name": "Shaw Blvd.", "loc": {"x": 8.197, "y": 14.215}},
        {"id": 41, "station_name": "Boni", "loc": {"x": 8.197, "y": 15.195}},
        {"id": 42, "station_name": "Guadalupe", "loc": {"x": 8.197, "y": 15.965}},
        {"id": 43, "station_name": "Buendia", "loc": {"x": 8.197, "y": 17.795}},
        {"id": 44, "station_name": "Ayala", "loc": {"x": 8.197, "y": 18.675}},
        {"id": 45, "station_name": "Magallanes", "loc": {"x": 8.197, "y": 19.865}},
        {"id": 46, "station_name": "Taft", "loc": {"x": 8.197, "y": 21.755}},
    ]
}