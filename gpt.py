import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.chatcompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].messgaes.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("chatbot: ", response)