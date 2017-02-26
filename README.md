# lanttu-cs
Lantun CS-palvelinten conffit


## Ohjeet
_Huom vanha ohje alla oleva rivi_
Kopioi `csconfig/` hakemistossa olevat tiedostot `/opt/csgo/config` -hakemistoon

Buildaa container
`docker build --no-cache=true -t lanttu/csgo .`

_Mene suoraan servers.jsonin konffaamiseen, vanha konffi...._
Aja container (huom. vaihda hostname/ip!!!)

```
docker run --name cs7 -v /opt/csgo/config:/home/steam/csgo/csgo/cfg/lanttu -p 10.10.0.107:27015:27015/udp -p 10.10.0.107:27015:27015  -p 10.10.0.107:27020:27020/udp -d lanttu/csgo -game csgo +hostname cs7 -secure -strictportbind -console -usercon +ip 0.0.0.0 -port 27015 +tv_name cs7tv +tv_enable 1 +tv_port 27020 -tickrate 128 +map de_dust2 +mapgroup mg_bomb +servercfgfile lanttu/csgo-server.cfg -maxplayers_override 12 +game_mode 1 +game_type 0
```


## servers.json

Muista vaihtaa GSLT-tokenit! Löytyy valven sivuilta.
```
{
  "servers": [
    {"server": "JOKELANCS1", "gslt": "XXXXXXXXX", "port": 27015, "tv_port": 27030, "host": "game-srv-1", "enabled": true},
    {"server": "JOKELANCS2", "gslt": "XXXXXXXXX", "port": 27016, "tv_port": 27031, "host": "game-srv-1", "enabled": true},
    {"server": "JOKELANCS3", "gslt": "XXXXXXXXX", "port": 27017, "tv_port": 27032, "host": "game-srv-1", "enabled": true},
    {"server": "JOKELANCS4", "gslt": "XXXXXXXXX", "port": 27018, "tv_port": 27033, "host": "game-srv-2", "enabled": true},
    {"server": "JOKELANCS5", "gslt": "XXXXXXXXX", "port": 27019, "tv_port": 27034, "host": "game-srv-2", "enabled": true},
    {"server": "JOKELANCS6", "gslt": "XXXXXXXXX", "port": 27020, "tv_port": 27035, "host": "game-srv-2", "enabled": true},
    {"server": "JOKELANCS7", "gslt": "XXXXXXXXX", "port": 27021, "tv_port": 27036, "host": "game-srv-3", "enabled": true},
    {"server": "JOKELANCS8", "gslt": "XXXXXXXXX", "port": 27022, "tv_port": 27037, "host": "game-srv-3", "enabled": true},
    {"server": "JOKELANCS9", "gslt": "XXXXXXXXX", "port": 27023, "tv_port": 27038, "host": "game-srv-3", "enabled": true}
  ]
}
```



```
# poista vanhat servut
docker rm <container idt>

# generoi konffis
python runner.py | sh

# nauti
```

Palvelimelle pitäisi nyt voida yhdistääsuoraan IP-osoitteella.
