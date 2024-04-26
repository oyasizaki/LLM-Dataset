import ollama
prompt= "answer the question within 50 words"
question= "Why is the sky blue?"

response = ollama.chat(model='llama2',
                       messages=[
                           {
                                'role': 'user',
                                'content': prompt + question,
                            },
                            ]
                        )
print(response['message']['content'])
