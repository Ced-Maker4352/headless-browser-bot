import argparse
from huggingface_hub import InferenceClient

def main():
    # 1. Parse the filename from the command line
    parser = argparse.ArgumentParser(
        description="Run Kimi-Dev on a local Python file and get fix suggestions"
    )
    parser.add_argument(
        "file", help="Path to the Python file you want Kimi-Dev to check"
    )
    args = parser.parse_args()

    # 2. Read in your buggy code
    with open(args.file, "r") as f:
        buggy_code = f.read()

    # 3. Initialize the HF conversational client
    client = InferenceClient()

    # 4. Build the chat messages
    system_msg = {
        "role": "system",
        "content": "You are a helpful assistant that suggests Python bug fixes."
    }
    user_msg = {
        "role": "user",
        "content": (
            "### Suggest a fix for this Python bug:\n"
            "```python\n"
            f"{buggy_code}"
            "```"
        )
    }

    # 5. Call the conversational API
    resp = client.chat_completion(
        model="moonshotai/Kimi-Dev-72B",
        messages=[system_msg, user_msg]
    )

    # 6. Print just the assistant’s reply
    print(resp.choices[0].message.content)

if __name__ == "__main__":
    main()
