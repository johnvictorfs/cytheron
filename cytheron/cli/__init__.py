from colorama import init
import click

import logging

from cytheron.interpreter import main_loop
from cytheron.logger import CustomFormatter


@click.command()
@click.option('--debug/--no-debug', default=False)
def main(debug: bool = False):
    """
    Cytheron, a C interpretor made with Python
    """
    # Initialize colorama colors formatting
    init()

    # Setup debugging
    logger = logging.getLogger("cytheron")
    logger.setLevel(logging.CRITICAL)

    ch = logging.StreamHandler()
    ch.setLevel(logging.CRITICAL)
    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)

    if debug:
        # Add debugging logging in debug mode
        logger.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)

    main_loop()


main()
