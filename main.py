def print_info() -> None:
    print(
        "[C] Command to say that this letter exists and is in (this) place",
        "-> '1 position letter' (Example '1 2 i')"
    )
    print(
        "[C] Command to say that this letter exists",
        "but not here (this position)",
        "-> '2 position letter' (Example '2 3 l')"
    )
    print(
        "[C] Command to say that this letter does not exist",
        "-> 'letter' (Example 't')"
    )
    print(
        "[C] To display words that currently match the information given",
        "-> 'show'"
    )
    print(
        "[!] Separate commands in a line with '-'",
        "-> (Example: 't-h-1 2 u-2 1 g')"
    )
    print("[!] Exit -> 'exit'")
    print()


def print_banner() -> None:
    print(
        r"""
 __      __                .___.__             ___ ___                __    
/  \    /  \___________  __| _/|  |   ____    /   |   \_____    ____ |  | __
\   \/\/   /  _ \_  __ \/ __ | |  | _/ __ \  /    ~    \__  \ _/ ___\|  |/ /
 \        (  <_> )  | \/ /_/ | |  |_\  ___/  \    Y    // __ \\  \___|    < 
  \__/\  / \____/|__|  \____ | |____/\___  >  \___|_  /(____  /\___  >__|_ \
       \/                   \/           \/         \/      \/     \/     \/
"""
    )


WORDS_FILENAME = "cwords.txt"
correct_dic = dict()
just_exists_dic = dict()
does_not_exist_ls = list()


def is_possible_word(word: str) -> bool:
    for index, char in correct_dic.items():
        if word[index - 1] != char:
            return False
    for index, char in just_exists_dic.items():
        if word[index - 1] == char or char not in word:
            return False
    for char in does_not_exist_ls:
        if char in word:
            return False
    return True


def main() -> None:
    print_banner()
    print_info()

    while True:
        ent = input("> ").split("-")
        for command in ent:
            params = command.split()
            if command == "exit":
                exit()
            elif command == "show":
                with open(WORDS_FILENAME, mode="r") as fs:
                    for word in fs.readlines():
                        word = word.replace("\n", "")
                        if is_possible_word(word):
                            print(word)
            elif params[0] == "1":
                correct_dic[int(params[1])] = params[2].lower()
            elif params[0] == "2":
                just_exists_dic[int(params[1])] = params[2].lower()
            else:
                does_not_exist_ls.append(params[0].lower())


if __name__ == "__main__":
    main()
