function clickedButton(){
    i+=1;
    i=i%2;
    if(i==0){
        document.getElementById("0").style["visibility"]="visible";
        document.getElementById("1").style["visibility"]="hidden";
        socket.send(JSON.stringify({"type":1}));
    }
    else if(i==1){
        document.getElementById("0").style["visibility"]="visible";
        document.getElementById("1").style["visibility"]="visible";
    }
}
