def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Hello World!")
banner("Hello World!", "*")
banner(border='.', message='Hello World!')