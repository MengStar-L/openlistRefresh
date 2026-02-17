import requests
import time
import logging
import tomllib
from pathlib import Path

# ================= 读取配置 =================
CONFIG_PATH = Path(__file__).parent / "config.toml"
with open(CONFIG_PATH, "rb") as f:
    _cfg = tomllib.load(f)

BASE_URL = _cfg["base_url"]
TARGET_PATH = _cfg["target_path"]
ADMIN_TOKEN = _cfg["admin_token"]
REFRESH_INTERVAL = _cfg["refresh_interval"]
# ============================================

# 配置日志输出
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def force_refresh_directory():
    url = f"{BASE_URL}/api/fs/list"
    
    headers = {
        "Authorization": ADMIN_TOKEN,
        "Content-Type": "application/json"
    }
    
    # payload 中的 refresh: True 是强制跳过缓存拉取最新数据的关键
    payload = {
        "path": TARGET_PATH,
        "password": "",
        "page": 1,
        "per_page": 0,
        "refresh": True
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response_data = response.json()
        
        if response.status_code == 200 and response_data.get("code") == 200:
            logging.info(f"✅ 成功强制刷新目录: {TARGET_PATH}")
        else:
            logging.error(f"❌ 刷新失败: {response_data.get('message', '未知错误')}")
            
    except Exception as e:
        logging.error(f"⚠️ 请求发生异常: {e}")

if __name__ == "__main__":
    logging.info(f"🚀 开始持续运行自动刷新服务，目标目录: {TARGET_PATH}，间隔: {REFRESH_INTERVAL}秒")
    while True:
        force_refresh_directory()
        time.sleep(REFRESH_INTERVAL)