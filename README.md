112-2 教育大數據資料探勘專題
====
* 授課教師： 蔡芸琤 老師、Summit Suen 老師
* 姓名：姚貫升

## HW1: Lab 1 - Exploring the Power of LLM（Large Language Model,大型語言模型）

[Code] (https://colab.research.google.com/notebooks/welcome.ipynb?hl=zh_tw#scrollTo=O-gfxRMJAgRS)
'''python
import requests
import json

# 定義 API 端點 URL 和 API 金鑰
url = "https://ntnu-ml.openai.azure.com/openai/deployments/ntnu-ml-gpt4-32k/chat/completions?api-version=2024-02-15-preview"
api_key = "7c196b48c6c14f25adc5a8d7dcbc8d02"  # 請替換為實際的 API 金鑰

# 設定 HTTP 請求的 headers
headers = {
    "Content-Type": "application/json",
    "api-key": "7c196b48c6c14f25adc5a8d7dcbc8d02"
}

# 使用者輸入的餐廳名稱
restaurant_name = input("請輸入您想要推薦的餐廳名稱：")

# 準備發送的 JSON 請求主體
data = {
    "messages": [
        {
            "role": "system",
            "content": "根據 `` 中提供的 rating.csv 資料，用協同過濾的概念推薦餐廳給使用者，請以 json array 格式回答\n\`\ncustomerId,restaurantId,rating\nc1,r2,3\nc1,r3,1\nc1,r5,3\nc1,r6,2\nc2,r1,3\nc2,r3,1\nc2,r5,1\nc2,r6,1\nc3,r4,3\nc3,r5,3\nc3,r6,3\nc4,r1,1\nc4,r4,1\nc4,r5,3\nc5,r2,1\nc5,r3,2\nc5,r4,3\nc6,r2,3\nc6,r3,3\nc6,r5,3\nc7,r2,3\nc7,r3,3\nc7,r4,1\nc8,r1,2\nc8,r2,1\nc8,r5,1\nc8,r6,2\n\`"
        },
        {
            "role": "user",
            "content": restaurant_name
        }
    ],
    "max_tokens": 800,
    "temperature": 0.5,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "top_p": 0.95,
    "stop": None
}

# 發送 POST 請求
response = requests.post(url, json=data, headers=headers)

# 解析回應
print(response.text)

if response.status_code == 200:
    result = response.json()
    choices = result.get("choices", [])  # 取得 'choices' 鍵值對，若不存在則返回空列表
    if choices:
        recommended_restaurants = choices[0]["message"]["content"]  # 取得推薦的餐廳列表
        print(f"推薦給 '{restaurant_name}' 的餐廳列表：{recommended_restaurants}")
    else:
        print("未找到推薦的餐廳列表")
else:
    print(f"請求失敗，狀態碼：{response.status_code}")
'''
[video] (https://youtu.be/5fotsQHgyeM)
