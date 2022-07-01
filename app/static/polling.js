var isActive = true;

            $().ready(function () {
                //EITHER USE A GLOBAL VAR OR PLACE VAR IN HIDDEN FIELD
                //IF FOR WHATEVER REASON YOU WANT TO STOP POLLING
                pollServer();
            });

            function pollServer()
            {
                if (isActive)
                {
                    window.setTimeout(function () {
                        $.ajax({
                            url: "http://192.168.68.104:5000/polling/climate.lounge_room",
                            type: "POST",
                            "dataType": "json",
                            "contentType": "application/json",
                            success: function (response) {
                                


                                //CHECK FAN SPEED
                                if(response['attributes']['fan_mode'] != fanmode){
                                    document.querySelector("#currentfanmode").innerText = response['attributes']['fan_mode']
                                    fanmode = response['attributes']['fan_mode']
                                        $(fanspeedelement).animate({
                                            opacity: 1
                                        });
                                }
                                //CHECK IF DEVICE STATE THEN UPDATE POWER BUTTON, FAN BUTTON, MODE SELECTOR
                                if(response['state'] != currentstate){
                                    //UPDATE POWER TOGGLE, FANMODE
                                    var fanspeedelement = document.querySelector("#currentfanmode");
                                    if(response['state'] == 'off'){
                                    document.querySelector("#toggleOnOff").className = "modebuttons"
                                    document.querySelector("#toggleOnOff").setAttribute( "onClick", "toggleOnOff('off', '"+response['entity_id']+"');" );
                                    document.querySelector("#changefanmode > i").setAttribute( "style", "");
                                    document.querySelector("#currentfanmode").innerText = "off"
                                    fanmode = response['attributes']['fan_mode']
                                    $(fanspeedelement).animate({
                                        opacity: 1
                                    });
                                    }
                                    else{
                                        document.querySelector("#toggleOnOff").className = "modebuttonsactive"
                                        document.querySelector("#toggleOnOff").setAttribute( "onClick", "toggleOnOff('"+response['state']+"', '"+response['entity_id']+"');" );
                                        document.querySelector("#changefanmode > i").setAttribute( "style", "-webkit-animation: spin 4s infinite linear;");
                                        document.querySelector("#currentfanmode").innerText = response['attributes']['fan_mode']
                                        fanmode = response['attributes']['fan_mode']
                                        $(fanspeedelement).animate({
                                            opacity: 1
                                        });
                                    }
                                    
                                }
                                //END STATE CHECK
                                //UPDATE MODE SELECTORS
                                $.each(response['attributes']['hvac_modes'], function(index, value) {
                                        var modediv = document.querySelector('#'+value)
                                        if(modediv){
                                            if(response['state'] == value){
                                                modediv.className = "modebuttonsactive";
                                            }
                                            else{
                                                modediv.className = "modebuttons";
                                            }
                                        }
                                        
                                    });
                                    //UPDATE SET TEMPERATURE
                                    if(response['attributes']['temperature'] != currenttemp){
                                        if(updatingtemp != true){
                                            document.querySelector("#climatemiddle > p").innerHTML = response['attributes']['temperature'] + '<span id="degreesymbol">°</span>';
                                        }
                                        
                                    }
                                




                                pollServer();
                            },
                            error: function () {
                                
                                pollServer();
                            }});
                    }, 5000);
                }
            }