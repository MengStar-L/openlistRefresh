# OpenList Refresh

AList 目录自动刷新工具 —— 定时强制刷新指定目录，确保文件列表始终是最新状态。

## 功能

- 定时调用 AList API 强制刷新指定目录（跳过缓存）
- 支持自定义刷新间隔
- 支持 systemd 部署为后台服务

## 快速开始

### 1. 环境要求

- Python 3.11+
- `requests` 库

```bash
pip install requests
```

### 2. 配置

复制示例配置文件并填写你的信息：

```bash
cp config.example.toml config.toml
```

编辑 `config.toml`：

```toml
# AList 面板地址 (不要以 / 结尾)
base_url = "http://your-alist-server:5244"

# 需要强制刷新的目录路径
target_path = "/YourPath"

# 管理员 Token
admin_token = "your_admin_token_here"

# 自动刷新间隔 (秒)
refresh_interval = 60
```

### 3. 运行

```bash
python3 openlistrefresh.py
```

## 部署为 systemd 服务

### 1. 上传文件

将项目文件上传到服务器，例如 `/opt/openlistRefresh/`：

```bash
mkdir -p /opt/openlistRefresh
# 将 openlistrefresh.py、config.toml 上传到该目录
```

### 2. 修改 service 文件

编辑 `openlistrefresh.service`，将 `WorkingDirectory` 和 `ExecStart` 修改为你的实际路径：

```ini
[Service]
WorkingDirectory=/opt/openlistRefresh
ExecStart=/usr/bin/python3 /opt/openlistRefresh/openlistrefresh.py
```

### 3. 安装并启动服务

```bash
# 复制 service 文件到 systemd 目录
sudo cp openlistrefresh.service /etc/systemd/system/

# 重新加载 systemd
sudo systemctl daemon-reload

# 启动服务
sudo systemctl start openlistrefresh

# 设置开机自启
sudo systemctl enable openlistrefresh
```

### 4. 常用管理命令

```bash
# 查看服务状态
sudo systemctl status openlistrefresh

# 查看日志
sudo journalctl -u openlistrefresh -f

# 重启服务
sudo systemctl restart openlistrefresh

# 停止服务
sudo systemctl stop openlistrefresh
```

## License

MIT
