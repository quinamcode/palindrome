def check(str):
    str = str.lower()
    reverse = "".join(reversed(str))
    if str == reverse:
        return True
    else:
        return False

str = input()
print(check(str))