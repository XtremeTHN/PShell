import sys
import shlex

import subprocess
import traceback

from modules.variables import PYTHON_EXEC_GLOBALS, PYTHON_EXEC_LOCALS

def exec_code(code):
    try:
        exec(code, PYTHON_EXEC_GLOBALS, PYTHON_EXEC_LOCALS)
    except SystemExit:
        sys.exit()
    except:
        traceback.print_exc()

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

        subprocess.run(args=args, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)

    def handle_python_code(self, code: str):
        if code in PYTHON_EXEC_GLOBALS:
            print(PYTHON_EXEC_GLOBALS[code])
        if code in PYTHON_EXEC_LOCALS:
            print(PYTHON_EXEC_LOCALS[code])

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
