from groq import Groq

api_key = '' #Input your own key here

client = Groq(api_key=api_key)

def phrase_as_dialect(sentence: str, dialect: str = "AAVE") -> str:
    prompt = (
        f"Please rewrite the following sentence into {dialect}, "
        f"using linguistically accurate grammar and avoiding stereotypes:\n\n"
        f"{sentence}"
    )

    response = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a linguistic assistant that helps rewrite English sentences into different dialects "
                    "accurately and respectfully."
                )
            },
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

def clean_output(response_text: str) -> str:
    if "<think>" in response_text and "</think>" in response_text:
        return response_text.split("</think>")[-1].strip()
    return response_text.strip()

if __name__ == "__main__":
    print("Dialect Rewriter (Groq + Mixtral)\n")
    sentence = input("Enter a sentence to rephrase: ")
    dialect = input("Enter the target dialect (e.g., AAVE, Scottish English, Indian English): ")

    raw_output = phrase_as_dialect(sentence, dialect)
    final_output = clean_output(raw_output)

    print(f"\nRewritten in {dialect}:\n{final_output}")
