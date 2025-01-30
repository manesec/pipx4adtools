# pipx4adtools
Integration of some common tools on pipx and collection for pipx with redteam tools.

## Install

Installation of base Dependencies

```
sudo apt-get install libsasl2-dev python-dev-is-python3 libldap2-dev libssl-dev
```

Install current project

```
git clone --recurse-submodules https://github.com/manesec/pipx4adtools pipx4adtools
cd pipx4adtools
pipx install .
```

After the installation is complete, you can delete the entire pipx4adtools folder.

## Tools

```
$ pipx list
   package pipx4adtools 0.0.2, installed using Python 3.12.8
    - GPOwned.py
    - LdapRelayScan.py
    - PetitPotam.py
    - addspn.py
    - dementor.py
    - dnstool.py
    - getnthash.py
    - gets4uticket.py
    - gettgtpkinit.py
    - krbrelayx.py
    - noPac.py
    - nopac_scanner.py
    - ntlm_theft.py
    - passthecert.py
    - printerbug.py
    - pygpoabuse.py
    - targetedKerberoast.py
    - windapsearch.py
    - wmiexec-pro.py
```

## Uninstall

Just simple command to remove all files on pipx.

```
pipx uninstall pipx4tools
```


## How to upgrade?

remove it and install again.

```
pipx uninstall pipx4tools
rm -rf pipx4adtools
git clone --recurse-submodules https://github.com/manesec/pipx4adtools pipx4adtools
cd pipx4adtools
pipx install .
```

