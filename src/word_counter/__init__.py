import click


@click.command()
def main() -> None:
    """Prompt for text and print the number of words."""
    text = click.prompt("Enter a string of words", type=str)
    word_count = len(text.split())
    click.echo(f"Word count: {word_count}")


if __name__ == "__main__":
    main()
