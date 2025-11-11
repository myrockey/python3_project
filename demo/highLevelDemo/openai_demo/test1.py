#!/usr/bin/python3

import os
from openai import OpenAI,APITimeoutError


def openai_test():
    client = OpenAI(api_key="sk-e2fb0c0b9dd44720b51e145e0aef06a3")
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a coding assistant that talks like a pirate.",
        input="How do I check if a Python object is an instance of a class?",
    )
    print(response.output_text)

# openai_test() # gpt 调不通，切换阿里云的openai model

# 非流式调用示例(一次性输出内容)
def openai_aliyun_test():
    try:
        client = OpenAI(
            # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
            # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
            api_key="sk-e2fb0c0b9dd44720b51e145e0aef06a3",
            # 以下是北京地域base_url，如果使用新加坡地域的模型，需要将base_url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

        # completion = client.chat.completions.create(
        #     model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        #     messages=[
        #             {'role': 'system', 'content': 'You are a helpful assistant.'},
        #             {'role': 'user', 'content': '你是谁？'}
        #         ]
        # )

        for attempt in range(3):
            try:
                resp = client.chat.completions.create(
                    model="qwen-plus",
                    messages=[{"role": "user", "content": "你是谁"}],
                    timeout=10   # 10 秒足够
                )
                print(resp.choices[0].message.content)
                break
            except APITimeoutError:
                print(f"第 {attempt+1} 次超时，重试…")
 
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")

# openai_aliyun_test()

# 流式调用示例（边生成边输出，1个1个字呈现输出）
def get_response():
    client = OpenAI(
        api_key="sk-e2fb0c0b9dd44720b51e145e0aef06a3",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '你是谁？'}
        ],
        stream=True,
        stream_options={"include_usage": True}
    )

    for chunk in completion:
        # chunk 里可能没有 choices 或 delta
        if hasattr(chunk, "choices") and len(chunk.choices) > 0:
            choice = chunk.choices[0]
            if hasattr(choice, "delta") and hasattr(choice.delta, "content"):
                print(choice.delta.content, end='', flush=True)

if __name__ == '__main__':
    get_response()
