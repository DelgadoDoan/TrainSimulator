const socket = new WebSocket('wss://trensimph.up.railway.app/ws/simulator');

let trains = {};

socket.onopen = () => {
    const userToken = sessionStorage.getItem('userToken');
    
    if (userToken) {
        socket.send(JSON.stringify({ type: "reload", token: userToken }));
    } else {
        function generateUniqueToken() {
            const array = new Uint32Array(1);
            window.crypto.getRandomValues(array);
            return array[0].toString(36);
        }

        const newToken = generateUniqueToken();
        sessionStorage.setItem('userToken', newToken);
        socket.send(JSON.stringify({ type: "open", token: newToken }));
    }

    console.log("Connected");
};

socket.onmessage = (event) => {
    console.log(event.data);
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