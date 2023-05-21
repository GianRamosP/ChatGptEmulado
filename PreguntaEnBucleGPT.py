import openai

openai.api_key = "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"

while True:
    
    prompt = input("Ask a question: ")
    
    if prompt == "exit":
        break
    
    completion = openai.Completion.create(engine="text-davinci-003",
                         prompt=prompt,
                         max_tokens=2048)
                         
    print(completion.choices[0].text)

