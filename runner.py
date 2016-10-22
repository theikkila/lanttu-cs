import json

import platform

host = platform.node()

config = json.load(open('servers.json'))


def command(server):
    return "docker run --name {server} -p {port}:{port}/udp -p {port}:{port} -p {tv_port}:{tv_port}/udp -p {tv_port}:{tv_port} --cpuset-cpus {core} -d lanttu/csgo -game csgo -console -usercon -usercon -port {port} +tv_name {server}TV +tv_enable 1 +tv_port {tv_port} -tickrate 128 +map de_dust2 +mapgroup mg_bomb +servercfgfile lanttu/csgo-server.cfg +sv_setsteamaccount {gslt} +tv_broadcast_origin_auth {server} -maxplayers_override 12 +game_mode 1 +game_type 0".format(**server)

for server in config['servers']:
    if server['host'] != host:
        continue
    if not server['enabled']:
        continue
    print(command(server))
