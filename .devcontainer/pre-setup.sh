#!/usr/bin/bash
set -euo pipefail

# 安装依赖
apt-get update
apt-get install -y --no-install-recommends \
ca-certificates curl git jq gpg build-essential sudo

# 安装 fish
echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/4/Debian_12/ /' | tee /etc/apt/sources.list.d/shells:fish:release:4.list
curl -fsSL https://download.opensuse.org/repositories/shells:fish:release:4/Debian_12/Release.key | gpg --dearmor | tee /etc/apt/trusted.gpg.d/shells_fish_release_4.gpg > /dev/null
apt-get install -y --no-install-recommends fish

# 安装 pandoc
architecture="$(dpkg --print-architecture)"
if [ "${architecture}" != "amd64" ] && [ "${architecture}" != "arm64" ]; then
    echo "(!) Architecture ${architecture} unsupported"
    exit 1
fi
version=$(curl -s https://api.github.com/repos/jgm/pandoc/releases/latest | jq -r '.tag_name')

curl -Lo pandoc.deb https://github.com/jgm/pandoc/releases/download/${version}/pandoc-${version}-1-${architecture}.deb
dpkg -i pandoc.deb && rm pandoc.deb

# 清理缓存
apt-get clean
rm -rf /var/lib/apt/lists/*