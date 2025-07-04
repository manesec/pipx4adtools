# pipx4adtools
Integration of some common tools on pipx and collection for pipx with redteam tools.

## Install

Installation of base Dependencies

```
sudo apt-get install libsasl2-dev python-dev-is-python3 libldap2-dev libssl-dev
```

and just using pipx to install :

```
pipx install git+https://github.com/manesec/pipx4adtools

# sccm-ntlmrelayx
pipx install git+https://github.com/manesec/pipx4adtools@relay-sccm

# tgssub
pipx install git+https://github.com/manesec/pipx4adtools@tgssub
```

If you are using `uv` tools :

```
uv tool install git+https://github.com/manesec/pipx4adtools
uv tool install git+https://github.com/manesec/pipx4adtools@relay-sccm
uv tool install git+https://github.com/manesec/pipx4adtools@tgssub
```

## Tools

```
   package pipx4adtools 0.0.5, installed using Python 3.13.3
    - GPOwned.py
    - LAPSDumper.py
    - LdapRelayScan.py
    - PetitPotam.py
    - addspn.py
    - dementor.py
    - dfscoerce.py
    - dnstool.py
    - emailextract.py
    - evil_winrmexec.py
    - forest-frida_intercept.py
    - forest-ftinfo.py
    - forest-getftST.py
    - forest-getlocalsid.py
    - forest-gettrustinfo.py
    - forest-keytab.py
    - getUserSIDBinary.py
    - getnthash.py
    - gets4uticket.py
    - gettgtpkinit.py
    - keytabextract.py
    - krbrelayx.py
    - noPac.py
    - nopac_scanner.py
    - ntlm_theft.py
    - ntlmscan.py
    - owa-emailextract.py
    - owa-ntlmscan.py
    - owa-proxyshell.py
    - passthecert.py
    - printerbug.py
    - pygpoabuse.py
    - targetedKerberoast.py
    - windapsearch.py
    - winrmexec.py
    - wmiexec-pro.py
```

## Install from source code 

(no recommand) Install current project from github source code.

```
git clone --recurse-submodules https://github.com/manesec/pipx4adtools pipx4adtools
cd pipx4adtools
pipx install .
```

After the installation is complete, you can delete the entire pipx4adtools folder.

## Uninstall

Just simple command to remove all files on pipx.

```
pipx uninstall pipx4adtools
```


## How to upgrade?


```
pipx upgrade pipx4adtools
uv tool upgrade pipx4adtools

# or
pipx upgrade-all
```

If you build from the source code, remove it and install again :

```
pipx uninstall pipx4adtools
rm -rf pipx4adtools
git clone --recurse-submodules https://github.com/manesec/pipx4adtools pipx4adtools
cd pipx4adtools
pipx install .
```
