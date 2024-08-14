from huggingface_hub import InferenceClient
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def mixtral8x7b(content):
    client = InferenceClient(
        os.getenv("MODEL_mixtral8x7b"),
        token=os.getenv("TOKEN"),
    )
    output=""
    for message in client.chat_completion(
        messages=[{"role": "user", "content": content}],
        max_tokens=500,
        stream=True,
    ):
        output += str(message.choices[0].delta.content)
    return output


def Mistral7b(content):
    client = InferenceClient(
        os.getenv("MODEL_Mistral7b"),
        token=os.getenv("TOKEN"),
    )
    output=""
    for message in client.chat_completion(
    	messages=[{"role": "user", "content": content}],
    	max_tokens=500,
    	stream=True,
    ):
        output += str(message.choices[0].delta.content)
    return output


def BiggieSmoLlm(content):
    API_URL = os.getenv("API_URL_BiggieSmoLlm")
    headers = {"Authorization": os.getenv("AUTHORIZATION_TOKEN_BiggieSmoLlm")}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": content,
    })

    return output[0]['generated_text']


def Phi3mini4k(content):
    client = InferenceClient(
        os.getenv("MODEL_Phi3mini4k"),
        token=os.getenv("TOKEN"),
    )
    output=""
    for message in client.chat_completion(
        messages=[{"role": "user", "content": content}],
        max_tokens=500,
        stream=True,
    ):
        output += str(message.choices[0].delta.content)
    return output