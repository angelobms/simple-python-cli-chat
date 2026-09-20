# Simple Python CLI Chat

A command-line chat assistant built with the OpenAI API. This is a
[Hyperskill](https://hyperskill.org) project that walks through building a
CLI chatbot in three stages: making the first API call, handling interactive
input with token-cost tracking, and adding function calling so the assistant
can end the conversation on request.

## Stages

1. **Setting Up the Chat Assistant** — configure the OpenAI client and send a
   single static message to the Chat Completion / Responses API.
2. **Interactive Chat and Token Cost Calculation** — prompt the user for
   input from the console, send it to the API, print the assistant's reply,
   and calculate the token cost of each interaction.
3. **Continuous Interaction and Function Calling** — turn the assistant into
   a persistent chatbot that loops until the user asks to stop, using a
   function tool (`end_conversation`) that the model calls to end the chat.

## Project structure

```
simple-python-cli-chat/
├── main.py            # the CLI assistant
├── requirements.txt   # dependencies: openai, load_dotenv, hstest
├── tests.py           # test entry point
└── test/              # stage test suite (hstest)
```

## Requirements

- Python 3.10+
- An OpenAI API key

## Setup

1. Install dependencies (from this folder):

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in this folder (`task/`) with your API key:

   ```
   OPENAI_API_KEY=your-api-key-here
   ```

   Optionally set `OPENAI_BASE_URL` if you're routing requests through a
   proxy.

## Usage

Run the assistant from this folder:

```bash
python main.py
```

Example session:

```
Enter a message: What is 5 + 10?
You: What is 5 + 10?
Assistant: 5 + 10 equals 15.
Cost: $0.00003000

Enter a message: What is the largest ocean?
You: What is the largest ocean?
Assistant: The largest ocean on Earth is the Pacific Ocean.
Cost: $0.00005650

Enter a message: End conversation
call_TjO2fMKrLs6uj1NwkXHeeffn
You: End conversation
Assistant: None
Cost: $0.00006350
```

Say something like "end conversation", "stop", or "quit" to make the
assistant call the termination function and exit the loop.

## Testing

Run the `hstest`-based test suite from this folder:

```bash
python tests.py
```
