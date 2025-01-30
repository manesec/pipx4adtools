from setuptools import setup, find_packages

def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

def install_requirements():
    all_requirements = []

    all_requirements.extend(read_requirements('src/pyGPOAbuse/requirements.txt'))

    return all_requirements

setup(
    name='pipx4tools', 
    version='0.0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pygpoabuse.py=src.start:start_pygpoabuse', 
        ],
    },
    install_requires=install_requirements(),
    python_requires='>=3.6', 
    author='manesec', 
    author_email='mane@manesec.com',  
    description='collection for pipx with redteam tools.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
    url='https://github.com/manesec/spose-thread',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
