from openai import OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)
EXTRA_HEADERS = {
    "HTTP-Referer": "https://localhost:3000",
    "X-Title": "My Local Python Bot"
}
def chat_bot():
    print("Bot (type quit to quit)")
    messages = []

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-r1",
                messages=messages,
                extra_headers=EXTRA_HEADERS
            )

            msg = completion.choices[0].message
            bot_reply = msg.content if msg and msg.content else "…"

            print(f"BOT: {bot_reply}")
            messages.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_bot()
