# """Lesson 1.7: Smart Model Router to route requests and calculate costs efficiently."""

try:
    task_type = input("Task (code / private / chat): ").strip().lower()
    tokens = int(input("Estimated tokens: "))

    if task_type == "code":
        model = "claude(cloud, strong at code)"
        price_per_1k = 0.8
    elif task_type == "private":
        model = "llama3.2 (local, ollama)"
        price_per_1k = 0.0
    elif task_type == "chat":
        model = "gpt-4o-mini (default fallback)"
        price_per_1k = 0.2
    else:
        model = "gpt-4o-mini (default fallback)"
        price_per_1k = 0.2
        print("Unknown task type. Falling back to default.")

    if tokens > 4000:
        print("Warning: long request, consider shortening it.")
    else:
        print("Length is fine.")

    cost = (tokens / 1000) * price_per_1k

    print(f"Chosen model: {model}")
    print(f"Estimated cost: {cost:.2f} PKR")

except ValueError:
    print("Error: Please enter a valid number for estimated tokens.")
