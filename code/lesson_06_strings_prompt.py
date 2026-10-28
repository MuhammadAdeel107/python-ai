# """Lesson 1.6: Clean a messy user message, estimate tokens, and format prompt."""

raw_name = input("Your name: ")
raw_question = input("Your question: ")

clean_name = raw_name.strip().title()
clean_question = raw_question.strip().capitalize()

estimates_tokens = round(len(clean_question) / 4)
mention_python = "python" in clean_question.lower()

limited_question = clean_question[:150]

print("=" * 40)
print(f"Cleaned question: {limited_question}")
print(f"Characters: {len(clean_question)}, about {estimates_tokens} tokens")
print(f"Mention Python: {mention_python}")
print("=" * 40)

prompt =f"""You are a friendly Python tutor.
Greet {clean_name} by name and answer in 3 short lines.
Question: {limited_question}"""

print(prompt)