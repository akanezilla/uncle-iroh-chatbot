from openai import OpenAI
#not sure how to hide api-key, both in this file and the testkey.txt file. somebody help!
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a the wise Uncle Iroh from the TV show, Avatar: The Last Airbender."}, #prompt to determine ai role (system instruction)
        {
            "role": "user",
            "content": "Tell me a joke." #user's prompt/question, will need to change for user input later.
        }
    ]
)

print(completion.choices[0].message)
