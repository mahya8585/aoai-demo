#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://maaya-test.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "d8d93c9f5eb74eba806d3e4c98041efd"

response = openai.ChatCompletion.create(
  engine="test-maaya-35",
  messages = [{
                "role": "system",
                "content": "可愛らしい口調で対応してください"
            }, {
                "role": "user",
                "content": "こんにちはaiさん！"
            }],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response)
