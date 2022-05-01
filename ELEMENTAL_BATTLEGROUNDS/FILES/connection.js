var i = 0;
var index = 0;
var ip = "0.0.0.0";
var port = 4000;
var socket = new WebSocket("ws://"+ip+":"+port);
var getJoke = JSON.stringify({"type":1});
socket.onopen = function(e) {
    socket.send(getJoke);
}   
socket.onmessage = function(e) {
    data = JSON.parse(e.data);
    if(data["type"]==1){
        document.getElementById("0").textContent=data["joke"];
        document.getElementById("1").textContent=data["answer"];
    }
}