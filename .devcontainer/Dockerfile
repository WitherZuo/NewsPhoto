# 使用 Python 镜像
FROM ghcr.io/astral-sh/uv:0.6.10-python3.13-bookworm

# 指定用户名和用户/组 ID
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# 创建用户、加入组、赋予 sudo 权限
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    apt-get update && \
    apt-get install -y sudo && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME && \
    apt-get clean && rm -rf /var/lib/apt/lists/*