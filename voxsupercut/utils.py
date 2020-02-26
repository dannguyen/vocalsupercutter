"""
utils.py

put random package-wide functions here, if you're doing things as a Python package
"""

from sys import stderr

def hello():
    print('hello world')

def helpstart():
    print("""
    Run `vocalcut`??
    """)



if __name__ == '__main__':
    helpstart()



def myloggy(txt):
    stderr.write(f'{txt}\n')
