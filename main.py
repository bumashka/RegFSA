from FSA import FSA

if __name__ == '__main__':
    delta = [{"http": 1}, {"s": 2, ":": 3}, {":": 3}, {"\/": 4}, {"\/": 5},
             {"[-\w]": 6}, {"[-\w]": 6, "\.": 7}, {"[-\w]": 8, "\w": 9},
             {"[-\w]": 8, "\.": 9}, {"\w": 9, "\.": 10, "\/": 12, ".": 13}, {"\w": 11},
             {"\w": 11, ".": 13, "\/": 12}, {".": 13}, {".": 13}]
    fsa = FSA(delta)
    quit_ = True
    menu = "[1]Generate url\n[2]Check url\n[3]Quit"
    print(menu)
    while quit_:
        print(">>>")
        choice = input()
        match choice:
            case "1":
                fsa.generate()
            case "2":
                print("Please, enter the url you want to check!\n>>>")
                text_url = input()
                fsa.check(text_url)
            case "3":
                quit_ = False
            case _:
                print("Error!")
        print(menu)
