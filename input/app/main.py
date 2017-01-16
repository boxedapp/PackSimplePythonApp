import sys
import codecs

def main():
    f = codecs.open('hello.txt', encoding='utf-8')
    for line in f:
        print repr(line)

    raw_input("Press Enter to continue...")    

if __name__ == "__main__":
    main()
