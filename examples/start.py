import os,subprocess,sys
from pathlib import Path

# tgssub
def start_tgssub():
    script_path = Path(__file__).resolve().parent / "tgssub.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command) 

