FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y lib32gcc1 wget
RUN useradd -m steam
USER steam
RUN mkdir ~/steamcmd
WORKDIR /home/steam/steamcmd

# Ladataan steam-client
RUN wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
RUN tar -xvzf steamcmd_linux.tar.gz
RUN mkdir -p /home/steam/csgo

# Asennetaan kynäri konttiin
RUN ./steamcmd.sh +login anonymous +force_install_dir ../csgo +app_update 740 validate +quit
WORKDIR /home/steam/csgo

#RUN mkdir -p /home/steam/csgo/csgo/cfg/lanttu
ADD csconfig /home/steam/csgo/csgo/cfg/lanttu

EXPOSE 27015/udp
EXPOSE 27020/udp
EXPOSE 27020


# Jätetään entrypointiksi jotain...
ENTRYPOINT ["./srcds_run"]
