import openai

openai.api_key = "YOUR_API_KEY"

def generate_text(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # or a newer model like 'gpt-4' if you have access
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,   # Adjust as needed
        temperature=0.7
    )
    # The text is returned in response.choices[0].message["content"]
    return response.choices[0].message["content"].strip()

prompt = "Once upon a time"
generated_text = generate_text(prompt)
print(generated_text)
