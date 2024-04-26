import ollama
prompt= "You are an API that converts bodies of text into a single question and answer into a JSON format. Each JSON " \
          "contains a single question with a single answer. Only respond with the JSON and no additional text. \n"
text= "chunk" # chunk of text got from previous code

response = ollama.chat(model='llama2',
                       messages=[
                           {
                                'role': 'user',
                                'content': prompt + text,
                            },
                            ]
                        )
print(response['message']['content'])
