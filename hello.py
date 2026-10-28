import re

print('Hello from OpenCode!')

# Sequenze ANSI CSI (es. colori) e OSC (es. clipboard) da rimuovere.
_ANSI_ESCAPE = re.compile(
    r"\x1b(?:\[[0-?]*[ -/]*[@-~]|\][^\x07\x1b]*(?:\x07|\x1b\\)?)"
)
# Caratteri di controllo residui.
_CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f-\x9f]")


def sanitize_name(name):
    """Rimuove sequenze ANSI/OSC e caratteri di controllo da un nome non fidato."""
    return _CONTROL_CHARS.sub("", _ANSI_ESCAPE.sub("", name)).strip()


def greetings(name):
    return f"Hello, {sanitize_name(name)}!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greetings(user_name))
