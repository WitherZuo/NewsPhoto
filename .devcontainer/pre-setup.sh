#!/usr/bin/bash
set -euo pipefail

# 安装依赖
apt-get update
apt-get install -y --no-install-recommends \
ca-certificates curl git build-essential sudo gpg

# 安装 fish
echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/4/Debian_13/ /' | tee /etc/apt/sources.list.d/shells:fish:release:4.list
curl -fsSL https://download.opensuse.org/repositories/shells:fish:release:4/Debian_13/Release.key | gpg --dearmor | tee /etc/apt/trusted.gpg.d/shells_fish_release_4.gpg > /dev/null
apt update
apt install fish

# 安装 pandoc
github_url="https://github.com"

architecture="$(dpkg --print-architecture)"
if [ "${architecture}" != "amd64" ] && [ "${architecture}" != "arm64" ]; then
    echo "(!) Architecture ${architecture} unsupported"
    exit 1
fi
version=$(git ls-remote --tags ${github_url}/jgm/pandoc.git \
        | grep -o 'refs/tags/[0-9].*' \
        | sed 's/refs\/tags\///' \
        | sort -V \
        | tail -n1)

curl -Lo pandoc.deb ${github_url}/jgm/pandoc/releases/download/${version}/pandoc-${version}-1-${architecture}.deb
dpkg -i pandoc.deb && rm pandoc.deb

# 清理缓存
apt-get clean
rm -rf /var/lib/apt/lists/*
