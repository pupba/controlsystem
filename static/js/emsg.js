// WebSocket 연결 시도
var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var ws_path =
    ws_scheme +
    "://" +
    window.location.hostname +
    ":8080" +
    "/ws/controlsystem/";
var socket = new WebSocket(ws_path);

// 연결이 열리면 호출됩니다.
socket.onopen = function () {
    console.log("WebSocket 연결이 열렸습니다.");
};

// 서버로부터 메시지를 받으면 호출됩니다.
socket.onmessage = function (event) {
    const [id, name, location, kind, etc] = event.data
        .slice(1, -1)
        .split(", ")
        .map((value) => {
            if (value[0] === "'") {
                return value.slice(1, -1);
            } else {
                return parseInt(value);
            }
        });
    console.log(name, location, kind, etc);
    const table = document.querySelector("#emtable");
    let tbody = table.querySelector("tbody");
    
    // 나중에 해결방안 찾기
    if (id === 1)
        while (tbody.firstChild) {
            tbody.removeChild(tbody.firstChild);
        }
    // 새로운 행 생성
    const tr = document.createElement("tr");

    let data = [name, location, kind, etc];
    for (let i = 0; i < data.length; i++) {
        var td = document.createElement("td");
        td.textContent = data[i];
        tr.appendChild(td);
    }
    tbody.appendChild(tr);
};

// 연결이 닫히면 호출됩니다.
socket.onclose = function () {
    console.log("WebSocket 연결이 닫혔습니다.");
};
