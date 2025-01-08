import openai

openai.api_key = "Your API KEY"
#Instructs the model to respond poetically, with a higher temperature (1) for more creative and stylistic outputs.
def poetic_chatbot(prompt):
    response = openai.chat.completions.create(
        model = "gpt-4",
        messages = [
            {
                "role": "system",
                "content": "You are a poetic chatbot"
            },
            {
                "role": "user",
                "content": "When was Google founded?"
            },
            {
                "role": "assistant",
                "content": "In the late '90s, a spark did ignit, Google emerged, a radiant light. By Larry and Sergey, in '98, it was born, a serch engine......"
            },
            {
                "role": "user",
                "content": "Which country has the youngest president?"
            },
            {
                "role": "assistant",
                "content": "Ah, the persuit of yourth in politics, a theme we explore. In Austria, Sebastian Kurz did i,plore, at the age of 31, his journey......."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 1,
        max_tokens = 256
    )
    return response.choices[0].message.content.strip()
prompt = "When was cheese first made?"
poetic_chatbot(prompt)
