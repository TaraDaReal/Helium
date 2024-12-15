from sys import stderr, stdout

def HeliumUndefinedToken(err):
    print(f"Undefined token {err}, did you forget to define {err}?", file=stderr)
    quit(1)
