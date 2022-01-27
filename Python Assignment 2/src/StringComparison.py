
#works reguardless the size of the strings
def compare(_firstString, _secondString):
    _list = list(set(_firstString.lower()) - set(_secondString.lower()))
    print("The Non-Common Charecters are: ")
    for i in _list:
        print(i)

# works only for equal length strings
def COMPARE(_firstString, _secondString):
    print("The Non-Common Charecters are: ")
    if (len(_firstString) == len(_secondString)):
        for i in len(_firstString):
            if (_firstString[i] != _secondString[0]):
                print(_firstString[i])

if __name__ == "__main__":
    print("Enter Two Strings: ")
    first = input()
    second = input()

    compare(first, second)
