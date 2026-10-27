import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 加载 .env 文件
load_dotenv()

# 2. 验证是否成功读取
key = os.getenv("DEEPSEEK_API_KEY")
if key:
    print(f"✅ 成功读取到 DeepSeek Key: {key[:8]}...")
else:
    print("❌ 警告: 没有找到 DEEPSEEK_API_KEY！")
    exit()

# 3. 初始化客户端（指向 DeepSeek 的服务器）
client = OpenAI(
    api_key=key,
    base_url="https://api.deepseek.com"
)

# 4. 发起请求
try:
    print("正在请求 DeepSeek...")
    response = client.chat.completions.create(
        model="deepseek-chat", # DeepSeek 的模型名
        messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
    )
    print("\n✅ 成功！模型回复：")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"\n❌ 发生了错误: {e}")
