set -e
img=$(grep -m1 'STEAMRT_IMAGE ?= registry' Makefile.in | sed 's/.*?= *//')
docker pull "$img"
printf 'FROM %s\nUSER root\nRUN apt-get update && apt-get install -y libwayland-dev libwayland-egl-backend-dev wayland-protocols libxkbcommon-dev libxkbregistry-dev libwayland-dev:i386 libxkbcommon-dev:i386 libxkbregistry-dev:i386\n' "$img" | docker build -t tkg-sdk-wl -
sed -i '0,/STEAMRT_IMAGE ?= registry.*/s||STEAMRT_IMAGE ?= tkg-sdk-wl|' Makefile.in