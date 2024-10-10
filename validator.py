import pandas as pd
from openai import OpenAI

df_main = pd.read_excel("api.xlsx")
for index, row in df_main.iterrows():
    try:
        client = OpenAI(api_key=row["API"])
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Hello, world!",
                }
            ],
            model="gpt-4",
        )
        print(response.choices[0].message.content)
        df_main.loc[index, "Status"] = "Valid"
        df_main.loc[index, "Response"] = response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        df_main.loc[index, "Status"] = "Invalid"
        df_main.loc[index, "Response"] = str(e)
    # breakpoint()
df_main.to_excel("api.xlsx", index=False)
