# chat_completion = openai.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Hello",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )
# print(chat_completion.choices[0].message.content)
#--------------------
# from key import my_api_key
# import openai

# openai.api_key = my_api_key
# messages = []

# while True:
#     message = input("user: ")
#     if message:
#         messages.append({"role": "user", "content": message})
#         result = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    
#         reply = result.choices[0].message.content
#         print(f"ChatGPT: {reply}")
