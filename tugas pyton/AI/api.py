import os
from openai import OpenAI

def get_deepseek_response(messages):
    try:
        client = OpenAI(
            api_key=os.environ.get("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def chat_with_deepseek():
    messages = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]
    
    print("Chat with DeepSeek AI (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        messages.append({"role": "user", "content": user_input})
        ai_response = get_deepseek_response(messages)
        
        if ai_response:
            print("AI:", ai_response)
            messages.append({"role": "assistant", "content": ai_response})
        else:
            print("Failed to get a response. Please try again.")

if __name__ == "__main__":
    chat_with_deepseek()