# """Lesson 1.8: Business Helper Bot for handling routine client queries."""

print("City Care Bot: Hi! Ask about timing, fee, location or appointments. Type 'bye' to exit.")

raw_name = input("City Care Bot: What is your name? ")
user_name = raw_name.strip().title()

message_count = 0
unanswered_count = 0

while True:
    user_input = input(f"{user_name}: ")
    clean_msg = user_input.strip().lower()
    if clean_msg == "bye":
        print(f"City Care Bot: Take Care, {user_name}!")
        break
    message_count += 1
    if "late" in clean_msg or "issue" in clean_msg or "problem" in clean_msg or "bad" in clean_msg:
        print("City Care Bot: Sorry about that. The clinic will call you today.")
    elif "timing" in clean_msg or "open" in clean_msg or "hours" in clean_msg:
        print("City Care Bot: We are open from 10 am to 8 pm, Monday to Saturday.")
    elif "fee" in clean_msg or "charges" in clean_msg or "price" in clean_msg:
        print("City Care Bot: Consultation fee is 2000 PKR.")
    elif "location" in clean_msg or "place" in clean_msg or "address" in clean_msg or "where" in clean_msg:
        print("City Care Bot: We are located near Jinnah Hospital, Johar.")
    elif "appointment" in clean_msg or "book" in clean_msg:
        print("City Care Bot: You can book an appointment via our helpline.")
    else:
        unanswered_count += 1
        print(f"City Care Bot: I am not sure yet. In Module 2, an AI will answer: You are the friendly assistant of City Care Clinic. Answer in 2 lines: {user_input}")

print("=" * 40)
print(f"Chat Summary: {message_count} messages, {unanswered_count} unanswered.")
