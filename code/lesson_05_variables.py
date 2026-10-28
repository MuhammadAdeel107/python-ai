# """Lesson 1.5: AI Model Profile Card with cost estimation using core data types."""

model_name="llama3.2"
context_window=128000
price_per_1k_tokens= 0.5
runs_locally= True

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context Window: {context_window} {type(context_window)}")
print(f"Price Per 1k Tokens:{price_per_1k_tokens} {type(price_per_1k_tokens)}")
print(f"Runs Locally:{runs_locally} {type(runs_locally)}")


tokens_per_chat = int(input("Tokens Per Chat: "))

cost = (tokens_per_chat / 1000) * price_per_1k_tokens

print(f"Estimated cost: {round(cost, 2)}PKR")