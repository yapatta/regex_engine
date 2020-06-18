import dfareg


def main():
    s = r"(ABC*|abc*)*"
    reg = dfareg.compile(s)
    print("正規表現: " + s)
    print("ABC: " + str(reg.matches("ABC")))
    print("ABBC: " + str(reg.matches("ABBC")))
    print("abcccAB: " + str(reg.matches("abcccAB")))


if __name__ == "__main__":
    main()
