import click


@click.command()
def main() -> None:
    """Prompt for text and print it with alternating blue/white words and a green final word."""
    text = click.prompt("Enter a string of words", type=str)
    words = text.split()

    styled_words = [
        click.style(word, fg="blue" if index % 2 == 0 else "white")
        for index, word in enumerate(words)
    ]

    if styled_words:
        styled_words[-1] = click.style(words[-1], fg="green")

    click.echo(" ".join(styled_words), color=True)


if __name__ == "__main__":
    main()
