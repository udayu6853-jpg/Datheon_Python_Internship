
import re
import json
from pathlib import Path

FAQ_FILE = Path(__file__).with_name("faq.json")


def load_faqs():
    """Load the internship FAQ dataset."""
    try:
        with FAQ_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("FAQ data must be a JSON object.")

        return data

    except FileNotFoundError:
        print("Error: faq.json was not found.")
    except json.JSONDecodeError as error:
        print(f"Error reading JSON: {error}")
    except (OSError, ValueError) as error:
        print(f"Could not load FAQs: {error}")

    return {"greetings": [], "faqs": []}


def find_intents(message, data):
    """Identify greetings and questions from the FAQ dataset."""
    text = message.lower().strip()
    intents = []

    greetings = data.get("greetings", [])

    if isinstance(greetings, list):
        for greeting in greetings:
            if isinstance(greeting, str):
                pattern = r"\b" + re.escape(greeting.lower()) + r"\b"
                if re.search(pattern, text):
                    intents.append("greeting")
                    break

    faqs = data.get("faqs", [])

    if isinstance(faqs, list):
        for faq in faqs:
            if not isinstance(faq, dict):
                continue

            question = faq.get("question", "")

            if not isinstance(question, str) or not question.strip():
                continue

            # Match important words from the FAQ question.
            words = re.findall(r"\b[a-zA-Z0-9]+\b", question.lower())
            keywords = [
                word for word in words
                if word not in {
                    "what", "are", "your", "how", "do", "i",
                    "when", "will", "the", "is", "a", "an",
                    "of", "to", "my", "you", "from"
                }
            ]

            if keywords and any(
                re.search(r"\b" + re.escape(word) + r"\b", text)
                for word in keywords
            ):
                intents.append(("faq", faq))

    return intents


def get_response(message, data):
    """Create a response and determine whether to exit."""
    text = message.strip().lower()

    if re.fullmatch(r"(bye|goodbye|exit|quit)", text):
        return "Goodbye! Best of luck with your projects.", True

    if not text:
        return "Please enter a message.", False

    intents = find_intents(text, data)
    responses = []

    if "greeting" in intents:
        responses.append("Hello! Welcome to the Datheon Internship Assistant.")

    for intent in intents:
        if isinstance(intent, tuple) and intent[0] == "faq":
            faq = intent[1]
            answer = faq.get("answer", "")

            if isinstance(answer, str) and answer.strip():
                responses.append(answer)

    if responses:
        # Avoid repeating identical answers.
        responses = list(dict.fromkeys(responses))
        return " ".join(responses), False

    return (
        "Sorry, I couldn't find a matching answer. "
        "Try asking about business hours, project submission, "
        "or your certificate."
    ), False


def main():
    data = load_faqs()

    print("=" * 48)
    print("       DATHEON INTERNSHIP CHATBOT")
    print("=" * 48)
    print("Ask about business hours, project submission, or certificates.")
    print("Type 'bye', 'exit', or 'quit' to stop.")

    while True:
        try:
            message = input("\nYou: ")
            response, should_exit = get_response(message, data)
            print("Bot:", response)

            if should_exit:
                break

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break


if __name__ == "__main__":
    main()
