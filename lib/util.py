def is_num(inp):
    try:
        float(inp)
        return True
    except ValueError:
        return False