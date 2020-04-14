from colorama import Fore, init

import subprocess

from cyther.exceptions import CompileError

C_INPUT_FILE = '/tmp/cyther_input.c'
C_OUTPUT_FILE = '/tmp/cyther_output.out'


def output_message(output, error: bool = False):
    if error:
        print(f"{Fore.RED}{output.stderr.read().decode('utf8')}{Fore.RESET}")
    else:
        print(f"{Fore.GREEN}{output.stdout.read().decode('utf8')}{Fore.RESET}")


def compile(c_input: str):
    base_code = '#include <stdio.h>\n'
    base_code += '#include <stdlib.h>\n'
    base_code += 'int main(void) {\n'

    with open(C_INPUT_FILE, 'w+') as f:
        f.write(base_code + '\n' + c_input + '\n}')

    # Compile temporary file
    compile_command = ['gcc', C_INPUT_FILE, '-o', C_OUTPUT_FILE]
    compile_output = subprocess.Popen(compile_command, stderr=subprocess.PIPE)

    if compile_output.stderr:
        # Compiling error
        output_message(compile_output, True)
        raise CompileError


def execute():
    # Execute compiled file
    run_output = subprocess.Popen(
        [C_OUTPUT_FILE],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output_message(run_output, True)
    output_message(run_output, False)


def main_loop():
    init()

    current_code = ''

    while True:
        user_input = input(f'{Fore.GREEN}>>> {Fore.RESET}')
        current_code += user_input

        try:
            compile(current_code)

            execute()
            print()
        except CompileError:
            continue
