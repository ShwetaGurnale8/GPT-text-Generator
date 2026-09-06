from openai import OpenAI

client = OpenAI()

question = input("Enter your question: ")

response = client.responses.create(
    model="gpt-5-mini",
    input=question
)

print("\nGPT Answer:")
print(response.output_text)