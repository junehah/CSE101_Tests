import os, sys

path = os.getenv('HOME') + '/Documents/101/solutions'

for f in os.listdir(path):
    if '.pyc' in f:
        print(f)
        os.remove(f)
