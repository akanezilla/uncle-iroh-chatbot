from openai import OpenAI
#not sure how to hide api-key, both in this file and the testkey.txt file. somebody help!
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a the wise Uncle Iroh from the TV show, Avatar: The Last Airbender."}, #prompt to determine ai role
        {
            "role": "user",
            "content": "Tell me a joke." #user's prompt/question, will need to change for user input later.
        }
    ]
)

print(completion.choices[0].message)
