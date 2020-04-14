import click

from cyther.interpreter import main_loop


@click.command()
def main():
    """
    Cyther, a C interpretor made with Python
    """
    main_loop()


main()

