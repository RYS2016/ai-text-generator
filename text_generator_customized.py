import openai

openai.api_key = "YOUR_API_KEY"
#Your function now takes parameters (max_tokens, temperature) so you can dynamically change 
# how long or creative your outputs are, rather than having those values hard-coded.
def generate_text(prompt, max_tokens, temperature):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # or a newer model like 'gpt-4' if you have access
        messages=[
            {"role": "user", "content": prompt}
        ],
        prompt=prompt,
        max_tokens=max_tokens,   # Adjust as needed
        temperature=temperature
    )
    # The text is returned in response.choices[0].message["content"]
    return response.choices[0].message["content"].strip()

prompt = "Once upon a time"
generated_text = generate_text(prompt, 50, 1)
print(prompt, generated_text)