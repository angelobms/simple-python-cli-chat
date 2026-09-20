import os
import warnings
# pyrefly: ignore [missing-import]
import dotenv

# Suppress Pydantic serialization warnings emitted by OpenAI SDK compaction models
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

# pyrefly: ignore [missing-import]
from openai import OpenAI

dotenv.load_dotenv()

SYSTEM_PROMPT = ("You are an helpful assistant for a simple CLI chat. "
                 "Only respond with text messages. Get creative with the answers! "
                 "If the user asks to end, stop, quit, or close the conversation, "
                 "call the end_conversation function instead of replying with text.")

MODEL = "gpt-5.1"
INPUT_TOKEN_PRICE = 1.25 / 1_000_000   # $ per input token
OUTPUT_TOKEN_PRICE = 10.00 / 1_000_000  # $ per output token

END_CONVERSATION_TOOL = {
    "type": "function",
    "name": "end_conversation",
    "description": "Ends the chat session. Call this when the user asks to end, stop, quit, or close the conversation.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
    },
}

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL") # you can override the base URL if you're using a proxy
) # if these environment variables are set, the client will read them automatically

conversation = client.conversations.create()

while True:
    user_message = input("Enter a message: ")

    response = client.responses.create(
        model=MODEL,
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        tools=[END_CONVERSATION_TOOL],
        conversation=conversation.id # use the conversation ID from before
    )

    cost = (response.usage.input_tokens * INPUT_TOKEN_PRICE
            + response.usage.output_tokens * OUTPUT_TOKEN_PRICE)

    should_end = False
    for item in response.output:
        if item.type == "function_call" and item.name == "end_conversation":
            print(item.call_id)
            should_end = True

    print(f"You: {user_message}")
    print(f"Assistant: {response.output_text or None}")
    print(f"Cost: ${cost:.8f}")

    if should_end:
        break
