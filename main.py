from FSA import FSA

if __name__ == '__main__':
    delta = [{"http": 1},  # 0
             {"s": 2, ":": 3},  # 1
             {":": 3},  # 2
             {"\/": 4},  # 3
             {"\/": 5},  # 4
             {"[-\w]": 6},  # 5
             {"[-\w]": 6, "\.": 7},  # 6
             {"\w": 9, "-": 8},  # 7
             {"[-\w]": 8, "\.": 10},  # 8
             {"-": 8, "\w": 9, "\.": 10, "\/": 14, ".": 15},  # 9
             {"\w": 11},  # 10
             {"\w": 11, "\.": 12, "\/": 14, ".": 15},  # 11
             {"\w": 13},  # 12
             {"\w": 13, "\/": 14, ".": 15},  # 13
             {".": 15},  # 14
             {".": 15}  # 15
             ]
    fsa = FSA(delta)
    quit_ = True
    menu = "[1]Generate url\n[2]Check url\n[3]Check urls from file\n[4]Quit"
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
                print("Checking urls from file \'url.txt\'")
                fsa.check_from_file("url.txt")
            case "4":
                quit_ = False
            case _:
                print("Error!")
        print(menu)
