import os
import urllib.request
import json
from dotenv import load_dotenv

# 加载 .env 中的密钥
load_dotenv()

# 1. 接口地址 (DeepSeek 的地址)
url = "https://api.deepseek.com/chat/completions"

# 2. 请求头 Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['DEEPSEEK_API_KEY']}", # DeepSeek 使用 Bearer Token
}

# 3. 请求体 Body
body = json.dumps({
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    "max_tokens": 256
}).encode() # 必须转换成 bytes

# 4. 构造请求并发起调用
req = urllib.request.Request(url, data=body, headers=headers, method="POST")

try:
    print("正在发送原生 HTTP 请求...")
    with urllib.request.urlopen(req) as resp:
        # 5. 解析返回的 JSON 数据
        result = json.loads(resp.read())
        # 6. 提取文本
        print("\n✅ 成功！回复如下：")
        print(result["choices"][0]["message"]["content"])
except urllib.error.HTTPError as e:
    print(f"❌ HTTP 错误: {e.code}")
    print(e.read().decode())
except Exception as e:
    print(f"❌ 发生错误: {e}")
