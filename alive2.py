import requests
import time
from flask import Flask  # 新增：轻量Web框架
import os

# 保活逻辑（原代码，放后台线程）
def keep_alive_task():
    TARGETS = [
        "https://qklm.xyz",       # 项目1
        "https://wyb.qklm.xyz",   # 项目2
        "https://onebaohuo2.onrender.com"  # 服务A域名
    ]
    while True:
        for url in TARGETS:
            try:
                requests.get(url, timeout=10)
                print(f"✅ 访问 {url} 成功")
            except Exception as e:
                print(f"❌ 访问 {url} 失败: {str(e)}")
        time.sleep(120)  # 每2分钟循环


# 假Web服务（仅用于让Render检测到端口）
app = Flask(__name__)
@app.route('/')
def fake_web():
    return "I'm just a keep-alive bot 🤫"  # 访问这个地址会看到这句话


# 启动：同时运行保活线程 + Web服务
if __name__ == "__main__":
    # 后台运行保活任务
    import threading
    t = threading.Thread(target=keep_alive_task)
    t.daemon = True  # 主线程退出时，后台线程也退出（不影响，因为Web服务会一直跑）
    t.start()
    
    # 监听Render分配的端口（必须！否则Web Service会报错）
    port = int(os.environ.get('PORT', 5000))  # 优先用环境变量PORT，默认5000
    app.run(host='0.0.0.0', port=port
