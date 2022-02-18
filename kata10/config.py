def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")

def main2():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")

def main3():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file:", err)
    except IsADirectoryError:
        print("Found config.txt but it's a directory, so it couldn't be read")
    except (BlockingIOError, TimeoutError):
        print("Filesystem is under heavy load, can't complete reading configuration file")

def main4():
    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt, but couldn't read it")
        else:
            print("OSError has been found:", err)

if __name__ == '__main__':
    main4()