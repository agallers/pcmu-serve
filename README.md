## Description

For Serco testing camera pull & play of PCMU audio (8kHz) via websocket

## Server Files

I wrote web socket server testing files in python & perl. Pick whichever is easier for you.<br/>
(Python required pip3 install tornado, Perl requires mcpan -i Net::WebSocket::Server)

## Media Files

The .ulaw files are for the websocket script (binary G711 u-law: audio/x-mulaw,rate=8000,channels=1)<br/>
The .mp3  files are for your Windows/Linux computers to (so you know how it should sound)

## Setup

The audio filename and server port hardcoded atop ws script, you can edit.<br/>
Run ./ws.py and tell the camera/doorbell to connect to "ws://<ip>:<port>/"<br/>
Server will just keep sending 800 bytes of audio (=0.1seconds of audio) every .1 seconds while client is connected
