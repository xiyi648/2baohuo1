import requests
import time

# 要保活的目标（部署后替换实际域名）
TARGETS = [
    "https://qklm.xyz",       # 项目1
    "https://wyb.qklm.xyz",   # 项目2
    "https://onebaohuo2.onrender.com"  # 服务A的Render域名（后续替换）
]

while True:
    for url in TARGETS:
        try:
            requests.get(url, timeout=10)
            print(f"✅ 访问 {url} 成功")
        except Exception as e:
            print(f"❌ 访问 {url} 失败: {str(e)}")
    time.sleep(120)  # 每2分钟循环（120秒）
