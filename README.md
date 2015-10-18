# lanttu-cs
Lantun CS-palvelinten conffit


## Ohjeet
Kopioi `csconfig/` hakemistossa olevat tiedostot `/opt/csgo/config` -hakemistoon

Buildaa container
`docker build -t lanttu/csgo .`

Aja container (huom. vaihda hostname/ip!!!)

```
docker run --name cs7 -v /opt/csgo/config:/home/steam/csgo/csgo/cfg/lanttu -p 10.10.0.107:27015:27015/udp -p 10.10.0.107:27015:27015  -p 10.10.0.107:27020:27020/udp -d lanttu/csgo -game csgo +hostname cs7 -secure -strictportbind -console -usercon +ip 0.0.0.0 -port 27015 +tv_name cs7tv +tv_enable 1 +tv_port 27020 -tickrate 128 +map de_dust2 +mapgroup mg_bomb +servercfgfile lanttu/csgo-server.cfg -maxplayers_override 12 +game_mode 1 +game_type 0
```

Palvelimelle pitäisi nyt voida yhdistääsuoraan IP-osoitteella.

