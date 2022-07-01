//Home assistant Web Socket API

//This file is used to connect to the Home Assistant Web Socket API

//Create socket connection to Home Assistant

var hass = require('homeassistant-ws');
console.log(hass)
console.log('module loaded')
window.states = [];
window.selected_player = 'media_player.junipers_tv';
window.current_media_name = '';
window.current_media_object = [];
window.currentstatedata = {};



//Return Current States of all devices
async function returnStates(){
  var client = await hass.default({
    token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyMGI4MmVmMDM0NzI0NzgwYTcxMjY0NzE5MTRhZWFkYiIsImlhdCI6MTY1NjAzMTEzOCwiZXhwIjoxOTcxMzkxMTM4fQ.HqqsQh0HeyCAZWQTKZ9jkTCYkrQj9mHLST7P7UmuX9U',
    host: '192.168.68.110'
  });
  var states = await client.getStates();
  return states;
}



async function playPause(){
  var client = await hass.default({
    token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyMGI4MmVmMDM0NzI0NzgwYTcxMjY0NzE5MTRhZWFkYiIsImlhdCI6MTY1NjAzMTEzOCwiZXhwIjoxOTcxMzkxMTM4fQ.HqqsQh0HeyCAZWQTKZ9jkTCYkrQj9mHLST7P7UmuX9U',
    host: '192.168.68.110'
  });
  await client.callService('media_player', 'media_play_pause', {
    entity_id: window.selected_player,
  });
}


async function playPlex(title){
  var client = await hass.default({
    token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyMGI4MmVmMDM0NzI0NzgwYTcxMjY0NzE5MTRhZWFkYiIsImlhdCI6MTY1NjAzMTEzOCwiZXhwIjoxOTcxMzkxMTM4fQ.HqqsQh0HeyCAZWQTKZ9jkTCYkrQj9mHLST7P7UmuX9U',
    host: '192.168.68.110'
  });
  await client.callService('media_player', 'play_media', {
    entity_id: window.selected_player,
    media_content_type: 'movie',
    media_content_id: 'plex://{"library_name": "Movies", "title": "'+title+'"}',
  });
}







//States Changed Broadcast
async function statesChangeBraodcast(){
  var client = await hass.default({
    token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyMGI4MmVmMDM0NzI0NzgwYTcxMjY0NzE5MTRhZWFkYiIsImlhdCI6MTY1NjAzMTEzOCwiZXhwIjoxOTcxMzkxMTM4fQ.HqqsQh0HeyCAZWQTKZ9jkTCYkrQj9mHLST7P7UmuX9U',
    host: '192.168.68.110'
  });
  client.on('state_changed', (stateChangedEvent) => {


    if(stateChangedEvent.data.entity_id == window.selected_player && stateChangedEvent.data.state != 'off'){

      if(stateChangedEvent.data.new_state.attributes.media_title != window.current_media_name){
        document.getElementById('devicestatusview-header-title').innerHTML = stateChangedEvent.data.new_state.attributes.friendly_name;
        window.current_media_name = stateChangedEvent.data.new_state.attributes.media_title;

        //AJAX
        $.ajax({
          url: "/search-movie-tmdb/" + stateChangedEvent.data.new_state.attributes.media_title,
          type: "GET",
          "dataType": "json",
          "contentType": "application/json",
          success: function(data) {
            window.current_media_object = data;
            //Change img source of devicestatusposter
            document.getElementById('devicestatusposter').src = 'https://image.tmdb.org/t/p/original/' + data.poster_path;
          }
      });
      }



      $("#range-input").attr("value", stateChangedEvent.data.new_state.attributes.media_position);
      $("#range-input").attr("max", stateChangedEvent.data.new_state.attributes.media_duration);
      
    }

    

  });



  //Onclick listener for play/pause button
  document.querySelector("#playpausemedia").addEventListener('click', function(){
    playPause();
  });


}
statesChangeBraodcast();





module.exports = {returnStates: returnStates, playPlex: playPlex, playPause: playPause}