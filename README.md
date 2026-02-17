# OpenList Refresh

AList 目录自动刷新工具 —— 定时强制刷新指定目录，确保文件列表始终最新。

## 部署步骤

> 以下命令在 Linux 服务器上依次执行即可。

### 1. 下载项目

```bash
git clone https://github.com/MengStar-L/openlistRefresh.git /opt/openlistRefresh
```

### 2. 安装依赖

```bash
pip install requests
```

### 3. 创建配置文件

```bash
cp /opt/openlistRefresh/config.example.toml /opt/openlistRefresh/config.toml
```

编辑配置文件：

```bash
nano /opt/openlistRefresh/config.toml
```

填入你的信息：

```toml
base_url = "http://你的AList地址:5244"
target_path = "/你的目录路径"
admin_token = "你的管理员Token"
refresh_interval = 60
```

> **Token 获取方式**：AList 后台 → 设置 → 其他 → 令牌

### 4. 注册为系统服务（开机自启）

```bash
cp /opt/openlistRefresh/openlistrefresh.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now openlistrefresh
```

### 5. 确认运行状态

```bash
systemctl status openlistrefresh
```

看到 `active (running)` 即表示部署成功 ✅

## 常用命令

```bash
# 查看实时日志
journalctl -u openlistrefresh -f

# 重启服务
systemctl restart openlistrefresh

# 停止服务
systemctl stop openlistrefresh
```

## License

MIT
