import json

import platform

host = platform.node()

config = json.load(open('servers.json'))


def command(server):
    return "docker kill {server} && docker rm {server}".format(**server)

for server in config['servers']:
    if server['host'] != host:
        continue
    if not server['enabled']:
        continue
    print(command(server))
