const Gdocument = document;

var username = 0;
var ishost = false;
var quicki=1;
var stopquickplay = 1;
var nextmap = 0;
var ended = 0;
var previousvar = 0;
var redovar = 0;
var banned = [];

function next(){
    if(stopquickplay==0){
        nextmap = 1
    }
    
} 
function previous(){
    previousvar = 1;
    next();
}
function stop(){
    stopquickplay = 1;
    quicki = 0;
}
function start(){
    stopquickplay = 0;
    quicki = 0;
    
}
function redo(){
    redovar = 1;
    next();
}
function setindex(e){
    quicki = e;
}


Node.prototype.fire=function(type,options){
     var event=new CustomEvent(type);
     for(var p in options){
         event[p]=options[p];
     }
     this.dispatchEvent(event);
}
function chat(message){
    mess = Gdocument.getElementById("newbonklobby_chat_input").value;
    mess2 = Gdocument.getElementById("ingamechatinputtext").value;
    Gdocument.getElementById("newbonklobby_chat_input").value = message;
    Gdocument.getElementById("ingamechatinputtext").value = message;
    Gdocument.fire("keydown",{keyCode:13});
    Gdocument.fire("keydown",{keyCode:13});
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
            if (a) { $('#newbonklobby_chat_content').scrollTop(Number.MAX_SAFE_INTEGER); };
            $('#ingamechatcontent').scrollTop(Number.MAX_SAFE_INTEGER);
}
function lastmessage(){

    var lm = Gdocument.getElementById("newbonklobby_chat_content").children[Gdocument.getElementById("newbonklobby_chat_content").children.length-1].children;
    if (lm[0].className == "newbonklobby_chat_msg_colorbox"){
        return lm[1].innerHTML.replace(/\&lt;/, "<").replace(/\&gt;/, ">").replace(/\&amp;/, "&") + " " + lm[2].innerHTML.replace(/\&lt;/, "<").replace(/\&gt;/, ">").replace(/\&amp;/, "&");
    }
    else if (lm[0].className == "newbonklobby_chat_status"){
        return lm[0].innerHTML.replace(/\&lt;/, "<").replace(/\&gt;/, ">").replace(/\&amp;/, "&");
    }
}
function map(e){
    if(e<0){
        displayInChat("There is no previous map.","#DA0808","#1EBCC1");
        quicki = 0;
        return;
    }
    if(Gdocument.getElementById("maploadwindowmapscontainer").children[e] == undefined){
        displayInChat("Click the maps button.","#DA0808","#1EBCC1");
        return;
    }
    Gdocument.getElementById("maploadwindowmapscontainer").children[e].click();
    Gdocument.getElementById("newbonklobby_editorbutton").click();
    setTimeout(function(){Gdocument.getElementById("mapeditor_midbox_testbutton").click();},1400);
    
}

function gotonextmap(e){
    if(e<0){
        displayInChat("There is no previous map.","#DA0808","#1EBCC1");
        quicki = 0;
        return;
    }
    if(Gdocument.getElementById("maploadwindowmapscontainer").children[e] == undefined){
        displayInChat("Click the maps button.","#DA0808","#1EBCC1");
        return;
    }
    Gdocument.getElementById("maploadwindowmapscontainer").children[e].click();
    Gdocument.getElementById("newbonklobby_editorbutton").click();
    Gdocument.getElementById("mapeditor_midbox_testbutton").click();
    


}
function commandhandle(chat_val){
    var new_val = "";
    if(ishost){
        if (chat_val.substring(1,5)=="next" && stopquickplay == 0){
            next();
            displayInChat("Switched to next map.","#DA0808","#1EBCC1");

        }
        else if (chat_val.substring(1,5)=="redo" && stopquickplay == 0){
            redo();
            displayInChat("Restarted map.","#DA0808","#1EBCC1");
        }
        else if (chat_val.substring(1,9)=="previous" && stopquickplay == 0){
            previous();
            displayInChat("Switched to previous map.","#DA0808","#1EBCC1");
        }
        else if (chat_val.substring(1,6)=="start"){
            start();
            displayInChat("Enabled quickplay.","#DA0808","#1EBCC1");
        }
        else if (chat_val.substring(1,5)=="stop"){
            stop();
            displayInChat("Disabled quickplay.","#DA0808","#1EBCC1");
        }
        else if (chat_val.substring(1,9)=="setindex"){

            if(parseInt(chat_val.substring(10))!=NaN){
                if(parseInt(chat_val.substring(10))>=0){
                    setindex(parseInt(chat_val.substring(10)));
                    displayInChat("Set the map index to " + quicki.toString() + ".","#DA0808","#1EBCC1");
                }
                else{
                    displayInChat("You cannot set the index to a negative number.","#DA0808","#1EBCC1");

                }
            }   
            
        }
        else if (chat_val.substring(1,4)=="ban" && chat_val.replace(/^\s+|\s+$/g, '').length>=6){
            banned.push(chat_val.substring(5).replace(/^\s+|\s+$/g, ''));
            displayInChat(chat_val.substring(5) + " is banned.","#DA0808","#1EBCC1");
            new_val = "/kick '"+chat_val.substring(5).replace(/^\s+|\s+$/g, '')+"'";
        }
        else if (chat_val.substring(1,6)=="index"){
            displayInChat("The map index is currently " + quicki.toString()+".","#DA0808","#1EBCC1");
        }
        else{
            return chat_val;
        }
        
    }
    return new_val;
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
function timeout1234() {
    setTimeout(function () {
        if(Gdocument.getElementsByClassName('newbonklobby_settings_button brownButton brownButton_classic buttonShadow brownButtonDisabled').length == 0){
            ishost = true;
        }
        else if(Gdocument.getElementsByClassName('newbonklobby_settings_button brownButton brownButton_classic buttonShadow brownButtonDisabled').length == 4){
            ishost = false;
        }
        if(Gdocument.getElementById("pretty_top_name")!=null){
            username = Gdocument.getElementById("pretty_top_name").textContent;
        }
        try{
        Last_message = lastmessage()
        } catch{
        Last_message = "";
        }
        if (ishost==true){
            for(i=0;i<banned.length;i++){
                if(Last_message == "* "+banned[i]+" has joined the game "){
                    chat("/kick '"+banned[i]+"'");
                }
            }
        }
        if(ishost == true && stopquickplay == 0){
            if(nextmap == 1){
                if (previousvar==1){
                    quicki--;
                    previousvar = 0;
                }
                else if (redovar==1){

                    redovar = 0;
                }
                else{
                    quicki++;
                }
                if(ended==0){
                    gotonextmap(quicki%(Gdocument.getElementById("maploadwindowmapscontainer").children.length));
                }
                else if(ended==1){
                    map(quicki%(Gdocument.getElementById("maploadwindowmapscontainer").children.length));
                    ended = 0;
                }

                Gdocument.getElementById("ingamewinner").style["visibility"]="hidden";
                nextmap = 0;
            }
            else if(Gdocument.getElementById("ingamewinner").style["visibility"]=="inherit" && stopquickplay == 0){
                nextmap = 1;
                ended = 1;


            }
        }
        
            
        
        timeout1234();
    }, 100);
}

timeout1234();