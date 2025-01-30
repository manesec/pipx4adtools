import os

# start and run pygpoabuse
def start_pygpoabuse():
    os.chdir('src/pyGPOAbuse')
    exec(open('pygpoabuse.py').read())
