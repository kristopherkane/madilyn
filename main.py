import sys
def main():
    args = sys.argv[1:]
    print("hello world: " + ' '.join(args))
    # args is a list of the command line args


if __name__ == "__main__":
    main()
