from colorama import Fore

import subprocess


def output_message(output: subprocess.Popen, error: bool = False) -> str:
    """
    Decode and format output from subprocess.Popen stdout or stderr
    """

    if error and output.stderr:
        # Format error messages with red color
        stderr = output.stderr.read().decode('utf8')

        if stderr:
            return f"{Fore.RED}{stderr}{Fore.RESET}"
    elif output.stdout:
        return output.stdout.read().decode('utf8')

    return ''
