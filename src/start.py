import os,subprocess,sys
from pathlib import Path

# pygpoabuse
def start_pygpoabuse():
    script_path = Path(__file__).resolve().parent / "pyGPOAbuse" / "pygpoabuse.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command) 


# GPOwned
def start_GPOwned():
    script_path = Path(__file__).resolve().parent / "GPOwned" / "GPOwned.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)


# krbrelayx : addspn
def start_addspn():
    script_path = Path(__file__).resolve().parent / "krbrelayx" / "addspn.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# krbrelayx : dnstool
def start_dnstool():
    script_path = Path(__file__).resolve().parent / "krbrelayx" / "dnstool.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# krbrelayx : printerbug
def start_printerbug():
    script_path = Path(__file__).resolve().parent / "krbrelayx" / "printerbug.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# krbrelayx : krbrelayx
def start_krbrelayx():
    script_path = Path(__file__).resolve().parent / "krbrelayx" / "krbrelayx.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)


# noPac : noPac
def start_nopac():
    script_path = Path(__file__).resolve().parent / "noPac" / "noPac.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# noPac : scanner
def start_nopac_scanner():
    script_path = Path(__file__).resolve().parent / "noPac" / "scanner.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# wmiexec-pro
def start_wmiexec_pro():
    script_path = Path(__file__).resolve().parent / "wmiexec-Pro" / "wmiexec-pro.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# windapsearch
def start_windapsearch():
    script_path = Path(__file__).resolve().parent / "windapsearch" / "windapsearch.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# PetitPotam
def start_petitpotam():
    script_path = Path(__file__).resolve().parent / "PetitPotam" / "PetitPotam.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)
