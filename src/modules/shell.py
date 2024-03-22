import sys
import shlex

import subprocess

from modules.variables import exec_code

class Shell:
    def __init__(self):
        pass
    
    def mainloop(self):
        while True:
            cmd = input("> ")
            if cmd == "exit":
                break
            elif cmd.startswith("!"):
                self.handle_shell_cmd(cmd)
            else:
                self.handle_python_code(cmd)

    def handle_shell_cmd(self, cmd):
        cmd = cmd[1:]
        args = shlex.split(cmd)
        print(subprocess.check_output(args).decode("utf-8"))

    def handle_python_code(self, code: str):
        if code.endswith(":"):
            indented_code = [code]
            while True:
                cmd = input(">> ")
                if cmd != "":
                    indented_code.append(cmd)
                else:
                    break
            exec_code("\n".join(indented_code))
        else:
            exec_code(code)