import random

responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "school": ["What do you think about school?", "School can be stressful sometimes."],
    "stressed": ["What are you worrying about?", "Do you want to talk about it?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

fallback = [
    "I don't understand.",
    "Can you explain more?",
    "I'm not sure I understand."
]
while True:
    user_input = input("You: ").lower()
    
    found = False

    for key in responses:
        if key in user_input:
            svar = random.choice(responses[key])
            print("Bot:", svar)
            found = True
            break

    if not found:
        print("Bot:", random.choice(fallback))

    if "bye" in user_input:
        break

