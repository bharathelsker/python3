def freq(str):
    SplitString = str.lower().split()

    UniqueWords = set(SplitString)

    for word in UniqueWords:
        print('{} got repeated {} times'.format(word, SplitString.count(word)))


def main():
    MyString = input('Enter the string : ')
    freq(MyString)


if __name__ == '__main__':
    main()
