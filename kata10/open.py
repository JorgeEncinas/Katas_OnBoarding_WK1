def main():
    open("/path/to/mars.jpg")

def exception_handling():
    try:
        open("config.txt")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")

if __name__ == '__main__':
    exception_handling()