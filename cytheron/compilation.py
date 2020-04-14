import logging
import subprocess

from cytheron.formatting import output_message
from cytheron.exceptions import CompileError
from cytheron.constants import C_OUTPUT_FILE, C_INPUT_FILE

logger = logging.getLogger("cytheron")


def compile(c_input: str):
    """
    Compile C code, raises `CompileError` and prints error message
    if something goes wrong
    """

    # Include some standard header files and main function at start of C file
    base_code = '#include <stdio.h>\n'
    base_code += '#include <stdlib.h>\n'
    base_code += 'int main(void) {\n'

    write_mode = 'w+'
    with open(C_INPUT_FILE, write_mode) as f:
        f.write(base_code + '\n' + c_input + '\n}')

        logger.debug(f"Wrote C code to '{C_INPUT_FILE}' in '{write_mode}' mode")

    # Compile temporary file with gcc
    compile_command = ['gcc', C_INPUT_FILE, '-o', C_OUTPUT_FILE]
    compile_output = subprocess.Popen(compile_command, stderr=subprocess.PIPE)

    command_str = ' '.join(compile_command)
    logger.debug(f"Running command: '{command_str}'")
    logger.debug(f"Compiled '{C_INPUT_FILE}' to '{C_OUTPUT_FILE}'")

    if compile_output.stderr:
        output = output_message(compile_output, True)

        # Error when compiling, print error message and raise error
        if output:
            print(output)

            logger.debug("Raising CompileError")
            raise CompileError
