//Home assistant Web Socket API

//This file is used to connect to the Home Assistant Web Socket API

//Create socket connection to Home Assistant

import hass from 'homeassistant-ws';

async function main(){
    const client = await hass({
        token: 'token-here',
    });
}

