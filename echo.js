for (var i = 0; i < 50000; i++){
    clearInterval(i);
}
var Gdocument = document.getElementById("maingameframe").contentDocument;
var echo_list = [];
var username = "";
var message = "";

function fire(type,options){
     var event=new CustomEvent(type);
     for(var p in options){
         event[p]=options[p];
     }
     Gdocument.dispatchEvent(event);
}
function chat(message){
    mess = Gdocument.getElementById("newbonklobby_chat_input").value;
    mess2 = Gdocument.getElementById("ingamechatinputtext").value;
    Gdocument.getElementById("newbonklobby_chat_input").value = message;
    Gdocument.getElementById("ingamechatinputtext").value = message;
    fire("keydown",{keyCode:13});
    fire("keydown",{keyCode:13});
    Gdocument.getElementById("newbonklobby_chat_input").value = mess;
    Gdocument.getElementById("ingamechatinputtext").value = mess2;
}
function displayInChat(message, LobbyColor, InGameColor, options) {
            options = options ?? {};
            LobbyColor = LobbyColor ?? "#8800FF";
            InGameColor = InGameColor ?? "#AA88FF";
            let A = Gdocument.createElement("div");
            let B = Gdocument.createElement("span");
            B.className = "newbonklobby_chat_status";
            B.style.color = LobbyColor;
            A.appendChild(B);
            B.innerHTML = (options.sanitize ?? true) ? message.replace(/&/g, '&amp;').replace(/>/g, '&gt;').replace(/</g, '&lt;') : message;
            let C = Gdocument.createElement("div");
            let D = Gdocument.createElement("span");
            D.style.color = InGameColor;
            C.appendChild(D);
            D.innerHTML = (options.sanitize ?? true) ? message.replace(/&/g, '&amp;').replace(/>/g, '&gt;').replace(/</g, '&lt;') : message;
            let a = false;
            if(Gdocument.getElementById("newbonklobby_chat_content").scrollHeight - Gdocument.getElementById("newbonklobby_chat_content").scrollTop > Gdocument.getElementById("newbonklobby_chat_content").clientHeight - 1) {
                a = true;
            }
            Gdocument.getElementById("newbonklobby_chat_content").appendChild(A);
            Gdocument.getElementById("ingamechatcontent").appendChild(C);
            if (a) { Gdocument.getElementById("newbonklobby_chat_content").scrollTop = Number.MAX_SAFE_INTEGER;};
            Gdocument.getElementById("ingamechatcontent").scrollTop = Number.MAX_SAFE_INTEGER;
}
function lastmessage(){
    var lm = Gdocument.getElementById("newbonklobby_chat_content").children[Gdocument.getElementById("newbonklobby_chat_content").children.length-1].children;
    if (lm[0].className == "newbonklobby_chat_msg_colorbox"){
        return lm[1].innerHTML.replace(/\&lt;/, "<").replace(/\&gt;/, ">").replace(/\&amp;/, "&") + " " + lm[2].innerHTML.replace(/\&lt;/, "<").replace(/\&gt;/, ">").replace(/\&amp;/, "&");
    }
    else if (lm[0].className == "newbonklobby_chat_status"){
        return lm[0].innerHTML.replace(/\&lt;/, "<").replace(/\&gt;/, ">").replace(/\&amp;/, "&");
    }
    return "";
}
function commandhandle(chat_val){
    if (chat_val.substring(1,6)=="echo " && chat_val.replace(/^\s+|\s+$/g, '').length>=7){
        if (chat_val.substring(6).replace(/^\s+|\s+$/g, '')==username){
            displayInChat("You cannot echo yourself.","#DA0808","#1EBCC1");
            return "";
        }
        else if (echo_list.indexOf(chat_val.substring(6).replace(/^\s+|\s+$/g, ''))===-1) {
            echo_list.push(chat_val.substring(6).replace(/^\s+|\s+$/g, ''));
            displayInChat(chat_val.substring(6).replace(/^\s+|\s+$/g, '') + " is being echoed.","#DA0808","#1EBCC1");
            return "";
        }
        else{
            displayInChat(chat_val.substring(6).replace(/^\s+|\s+$/g, '') + " is already being echoed.","#DA0808","#1EBCC1");
            return "";
        }
    }
    else if (chat_val.substring(1,8)=="remove "  && chat_val.replace(/^\s+|\s+$/g, '').length>=7){
        if (echo_list.indexOf(chat_val.substring(7).replace(/^\s+|\s+$/g, ''))!==-1){
            echo_list.splice(echo_list.indexOf(chat_val.substring(7).replace(/^\s+|\s+$/g, '')),1);
            displayInChat(chat_val.substring(7).replace(/^\s+|\s+$/g, '')+" is not being echoed.","#DA0808","#1EBCC1");
            return "";
        }
        else{
            displayInChat("You cannot remove someone that you didn't echo.","#DA0808","#1EBCC1");
            return "";
        }
        
    }
    else if (chat_val.substring(1,6)=="clear"){
        echo_list = [];
        displayInChat("Cleared the echo list.","#DA0808","#1EBCC1");
        return "";
    }
    
    return chat_val;
    
        
}
(function(){
var newbonklobby_chat_input_old = Gdocument.getElementById("newbonklobby_chat_input").onkeydown ?? (function(){});
Gdocument.getElementById("newbonklobby_chat_input").onkeydown = function(e){
    newbonklobby_chat_input_old(e);
    if(e.keyCode==13){
        var chat_val = Gdocument.getElementById("newbonklobby_chat_input").value;
        if (chat_val!="" && chat_val[0]=="/"){
            Gdocument.getElementById("newbonklobby_chat_input").value = "";
            chat(commandhandle(chat_val));
        }
        chat_val = Gdocument.getElementById("ingamechatinputtext").value;
        if (chat_val!="" && chat_val[0]=="/"){
 
            Gdocument.getElementById("ingamechatinputtext").value = "";
            chat(commandhandle(chat_val));
        }
    }
}
})();
(function(){
var ingame_chat_input_old = Gdocument.getElementById("ingamechatinputtext").onkeydown ?? (function(){});
 Gdocument.getElementById("ingamechatinputtext").onkeydown = function(e){
    ingame_chat_input_old(e);
    if(e.keyCode==13){
        var chat_val = Gdocument.getElementById("newbonklobby_chat_input").value;
        if (chat_val!="" && chat_val[0]=="/"){
            Gdocument.getElementById("newbonklobby_chat_input").value = "";
            chat(commandhandle(chat_val));
        }
        chat_val = Gdocument.getElementById("ingamechatinputtext").value;
        if (chat_val!="" && chat_val[0]=="/"){
            Gdocument.getElementById("ingamechatinputtext").value = "";
            chat(commandhandle(chat_val));
        }
    }
}
})();
Last_message = "";
Laster_message = "";
new_message = false;
intervals1234 = setInterval(timeout1234,100);
function timeout1234() {
    if(Gdocument.getElementById("pretty_top_name")!=null){
        username = Gdocument.getElementById("pretty_top_name").textContent;
    } 
    try{
        Last_message = lastmessage()
    } catch{
        Last_message = "";
    }
    if (Laster_message != Last_message){
        Laster_message = Last_message;
        new_message = true;
    }
    if(new_message){
        for(i=0;i<echo_list.length;i++){
            if(Last_message.substring(0,echo_list[i].length+2) == echo_list[i]+": "){
                message = Last_message.substring(echo_list[i].length+2);
                chat(message);
            }
        }
    }
    new_message = false;
}
