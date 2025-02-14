from setuptools import setup, find_packages

def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

def install_requirements():
    all_requirements = []

    all_requirements.extend(read_requirements('src/pyGPOAbuse/requirements.txt'))
    all_requirements.extend(read_requirements('src/GPOwned/requirements.txt'))
    all_requirements.extend(read_requirements('src/wmiexec-Pro/requirements.txt'))
    all_requirements.extend(read_requirements('src/windapsearch/requirements.txt'))
    all_requirements.extend(read_requirements('src/LdapRelayScan/requirements.txt'))
    all_requirements.extend(read_requirements('src/targetedKerberoast/requirements.txt'))
    all_requirements.extend(read_requirements('src/PKINITtools/requirements.txt'))

    # ntlm_theft
    all_requirements.append("xlsxwriter")

    # requests
    all_requirements.append("requests")

    # exchange proxyshell
    all_requirements.append("pypsrp")

    # forest-trust-tools
    all_requirements.append("frida")

    return all_requirements

setup(
    name='pipx4adtools',
    version='0.0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pygpoabuse.py=src.start:start_pygpoabuse',
            'GPOwned.py=src.start:start_GPOwned',
            'addspn.py=src.start:start_addspn',
            'dnstool.py=src.start:start_dnstool',
            'krbrelayx.py=src.start:start_krbrelayx',
            'printerbug.py=src.start:start_printerbug',
            'noPac.py=src.start:start_nopac',
            'nopac_scanner.py=src.start:start_nopac_scanner',
            'wmiexec-pro.py=src.start:start_wmiexec_pro',
            'windapsearch.py=src.start:start_windapsearch',
            'PetitPotam.py=src.start:start_petitpotam',
            'ntlm_theft.py=src.start:start_ntlm_theft',
            'dementor.py=src.start:start_dementor',
            'LdapRelayScan.py=src.start:start_LdapRelayScan',
            "targetedKerberoast.py=src.start:start_targetedKerberoast",
            "getnthash.py=src.start:start_getnthash",
            "gets4uticket.py=src.start:start_gets4uticket",
            "gettgtpkinit.py=src.start:start_gettgtpkinit",
            "passthecert.py=src.start:start_passthecert",
            "owa-emailextract.py=src.start:start_owamailextract",
            "owa-ntlmscan.py=src.start:start_ntlmscan",
            "owa-proxyshell.py=src.start:start_owaproxyshell",
            "getUserSIDBinary.py=src.start:start_GetUserSIDBinary",
            "forest-getftST.py=src.start:start_getftST",
            "forest-getlocalsid.py=src.start:start_getlocalsid",
            "forest-keytab.py=src.start:start_keytab",
            "forest-gettrustinfo.py=src.start:start_gettrustinfo",

        ],
    },
    install_requires=install_requirements(),
    python_requires='>=3.6',
    author='manesec',
    author_email='mane@manesec.com',
    description='collection for pipx with redteam tools.',
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/manesec/pipx4adtools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
