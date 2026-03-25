import click


@click.command()
def main() -> None:
    """Prompt for text and print it with alternating blue/white words."""
    text = click.prompt("Enter a string of words", type=str)
    words = text.split()

    styled_words = [
        click.style(word, fg="blue" if index % 2 == 0 else "white")
        for index, word in enumerate(words)
    ]

    click.echo(" ".join(styled_words), color=True)


if __name__ == "__main__":
    main()
