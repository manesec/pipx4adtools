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

# ntlm_theft
def start_ntlm_theft():
    script_path = Path(__file__).resolve().parent / "ntlm_theft" / "ntlm_theft.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)


# dementor.py
def start_dementor():
    script_path = Path(__file__).resolve().parent / "Dementor" / "dementor.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)


# LdapRelayScan
def start_LdapRelayScan():
    script_path = Path(__file__).resolve().parent / "LdapRelayScan" / "LdapRelayScan.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# targetedKerberoast
def start_targetedKerberoast():
    script_path = Path(__file__).resolve().parent / "targetedKerberoast" / "targetedKerberoast.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# PKINITtools : getnthash.py
def start_getnthash():
    script_path = Path(__file__).resolve().parent / "PKINITtools" / "getnthash.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)


# PKINITtools : gets4uticket.py
def start_gets4uticket():
    script_path = Path(__file__).resolve().parent / "PKINITtools" / "gets4uticket.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# PKINITtools : gettgtpkinit.py
def start_gettgtpkinit():
    script_path = Path(__file__).resolve().parent / "PKINITtools" / "gettgtpkinit.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)


# PassTheCert
def start_passthecert():
    script_path = Path(__file__).resolve().parent / "PassTheCert" / "Python" / "passthecert.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# owa emailextract
def start_owamailextract():
    script_path = Path(__file__).resolve().parent / "owa-emailextract" / "emailextract.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# ntlmscan
def start_ntlmscan():
    script_path = Path(__file__).resolve().parent / "ntlmscan" / "ntlmscan.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

# owa proxyshell
def start_owaproxyshell():
    script_path = Path(__file__).resolve().parent / "proxyshell" / "proxyshell.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)


# tools4mane GetUserSIDBinary.py
def start_GetUserSIDBinary():
    script_path = Path(__file__).resolve().parent / "tools4mane" / "Tools" / "GetUserSIDBinary.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)
