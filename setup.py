from setuptools import setup, find_packages

def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

def install_requirements():
    all_requirements = []

    all_requirements.append("impacket@git+https://github.com/garrettfoster13/impacket.git@feature/relay-sccm-adminservice")
    all_requirements.append("setuptools")

    return all_requirements

setup(
    name='pipx4adtools-sccm-ntlmrelayx',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "sccm-ntlmrelayx.py=examples.start:start_ntlmrelayx",

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
