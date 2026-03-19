import random

responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "school": ["What do you think about school?", "School can be stressful sometimes."],
    "stressed": ["What are you worrying about?", "Do you want to talk about it?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

questions = {
    "what type of robot are you": ["I'm an AI programmed by a human to help you with your emotions."],
    "can you help me": ["Yes, I can try to help you.", "Of course, tell me what's wrong."],
    "what do you do": ["I talk with people and respond to simple questions."],
    "are you real": ["I'm not a human, but I am a real computer program."],
    "how old are you": ["I don't have an age like humans do."],
    "are you similiar to Jarvis": ["i fear Jarvis is more cooler than me"]
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
        for key in questions:
            if key in user_input:
                svar = random.choice(questions[key])
                print("Bot:", svar)
                found = True
                break

    if not found:
        print("Bot:", random.choice(fallback))

    if "bye" in user_input:
        break