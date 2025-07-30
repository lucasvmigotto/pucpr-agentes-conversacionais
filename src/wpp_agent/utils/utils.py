def choice_accept(prompt: str) -> bool:
    OPTIONS: tuple[str, str] = ("Y", "N")
    while True:
        if (choice := input(f"{prompt} [Y/N] ").strip().upper()) in OPTIONS:
            break
    return choice == "Y"


def ask_reply(from_who: str, last_message: str) -> str:
    return f"Reply '{from_who}'?\n\t{from_who}: {last_message}"
