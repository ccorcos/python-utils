from sys import stdout
from time import sleep

def progress(n, total):
    stdout.write("\r%d" % i)
    stdout.flush()
    if n == total:
        stdout.write("\n") # move the cursor to the next line