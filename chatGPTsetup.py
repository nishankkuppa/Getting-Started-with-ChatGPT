import openai

# OpenAI credentials
openai.api_key = "YOUR-API-KEY-HERE"


# This function processes user input through the ChatGPT API
def GPTQuery(myInput):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,  # Lower temperature values make the output less random
        max_tokens=256,
        # Instruct the model on how to process certain inputs:
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": myInput},
        ]

    )

    chatGPTresponse = completion.choices[0].message.content

    return chatGPTresponse


def chatbot():
    while True:
        prompt = input("You: ")
        promptNew = prompt.lower()

        myResponse = GPTQuery(promptNew)
        print(f"ChatGPT: {myResponse}")


if __name__ == "__main__":
    chatbot()
