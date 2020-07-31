# Archecord Discord Minecraft RCON Bot

This is a fairly simple Discord Bot to run commands in Discord Chat as if you were at the console. CAUTION: It doesn't provide permissions so guard it like you are OP.

### 0) Register the App at Discord
[https://discord.com/developers/applications](https://discord.com/developers/applications)

### 1) Setup Environment
* Use your environment of choice. Pip modules are in 'requirements.txt'
* Create a '.env' file in the same directory as the app script and set your:  
`RCON_PASSWORD=password` 
`RCON_SERVER=some.domain.or.IP`  
`DISCORD_TOKEN=lettersANDNumbers` (From Step 0)

* You need to make sure your server is accessible at your chosen RCON port and set up for RCON in your 'server.properties' file on your Minecraft server.  
`rcon.port=25575`  
`rcon.password=SomethingSecret`  
`enable-rcon=true`  

* There is also an optional line `broadcast-rcon-to-ops=true` if you want any online OPs to see RCON at work. RCON transmits unencrypted so this is best if the app and server run on the same network.

### 2) Run the App
* Use the '//' for the app to pick up commands like '//say Hello World'
* For some kind of security, /op, /deop, /kill, /stop and /give are filtered out but you can edit this for your own needs.