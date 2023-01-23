import re
import openai

# Set the API key
openai.api_key = "YOUR-API-KEY"

# Use the ChatGPT model to generate text
model_engine = "text-davinci-002"

prompt = "5 preguntas en español de NPS en seguro de vida con sus respectivas opciones"
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.3
)
message = completion.choices[0].text.strip()

# Process text
result = {}
for key, value in enumerate(message.split('\n')):
    if value:
        if re.search(r'^(\d)+.', value): # Regex for detect start with number
            result[value] = []
        elif re.search(r'^([a-zA-Z]?)+[.]', value): # Regex for detect start with character
            last_key = list(result.keys())[-1]
            result[last_key].append(value)
        else:
            pass

for key, value in enumerate(result):
    for _key, option in enumerate(result[value]):
        print(option)

print(result)
