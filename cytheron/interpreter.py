from colorama import Fore

import subprocess
import logging

from cytheron.exceptions import CompileError
from cytheron.compilation import compile
from cytheron.constants import C_OUTPUT_FILE
from cytheron.formatting import output_message

logger = logging.getLogger("cytheron")


def execute():
    """
    Run compiled executable and print output
    """

    # Execute compiled file
    run_output = subprocess.Popen([C_OUTPUT_FILE], stdout=subprocess.PIPE)

    logger.debug(f"Executing '{C_OUTPUT_FILE}'")

    # Print output message from executable
    print(output_message(run_output))


def main_loop():
    """
    Main interpreter loop
    """

    current_code = ''

    # Interpreter loop
    while True:
        # User Code Input
        user_input = input(f'{Fore.GREEN}>>> {Fore.RESET}')

        try:
            # Compile every code compiled sucessfully so far + new user code input
            compile(current_code + user_input)

            # Only add code to code history if it didn't error
            current_code += user_input

            execute()
        except CompileError:
            logger.debug('Error compiling, not executing')
            continue
