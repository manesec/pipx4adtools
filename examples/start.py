import os,subprocess,sys
from pathlib import Path

# ntlmrelayx
def start_ntlmrelayx():
    script_path = Path(__file__).resolve().parent / "ntlmrelayx.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

