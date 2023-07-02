import openai

openai.api_key = "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"

models = openai.Model.list()
#print(models)

def handle_input(user_input):
    copletion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo"
        , messages=[{"role": "user", "content": user_input}]
    )
    return  copletion