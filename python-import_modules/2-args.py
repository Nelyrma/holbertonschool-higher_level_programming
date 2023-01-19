#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    length = len(argv)

    if (length - 1) == 1:
        print("1 argument:")
    else:
        print(f"{length - 1} arguments:" if (length - 1) else "0 arguments.")
    for i in range(1, length):
        print(f"{i}: {argv[i]}")
