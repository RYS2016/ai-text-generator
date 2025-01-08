import openai

#Focuses on summarizing content, with a lower temperature (0.5) for more concise and controlled output.
#Provides system/user messages that guide the model to produce summaries
def text_summarizer(prompt):
    response = openai.chat.completion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content": "Some text......"
            },
            {
                "role": "user",
                "content": "Some text......"
            },
            {
                "role": "assistant",
                "content": "Some text......"
            },
            {
                "role": "user",
                "content": "Some text......"
            },
            {
                "role": "assistant",
                "content": "Some text......"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0.5,
        max_tokens = 256
    )
    return response.choices[0].message.content.strip()
prompt = "Some text"
text_summarizer(prompt)