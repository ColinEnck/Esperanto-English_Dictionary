# Esperanto -- English dictionary search system
while True:
    word = input("Enter word for look-up:\n(type 'x' to exit)\n> ")
    print("")
    if word == "":
        continue
    elif word == "x":
        break
    if "x" in word:
        word = word.strip().lower().replace("cx", "ĉ").replace("gx", "ĝ")\
        .replace("hx", "ĥ").replace("jx", "ĵ").replace("sx", "ŝ").replace("ux", "ŭ")
    else:
        word = word.strip().lower().replace("ch", "ĉ").replace("gh", "ĝ")\
        .replace("hh", "ĥ").replace("jh", "ĵ").replace("sh", "ŝ").replace("uh", "ŭ")\
        .replace("'", "")
    f = open("espdic.txt")
    text = f.readlines()

    # matching line of text
    exact_find = ""
    other_finds = []

    for line in text:
        line_words = line.split()
        # if line has less than 2 "words"
        if len(line_words) < 2:
            continue
        # finding exact Esperanto word match and printing the line
        if line_words[0] == word and line_words[1] == ":":
            exact_find = line
            break

    if exact_find != "":
        print("---- Identical match ----")
        print(exact_find, end="")
        print("-------------------------\n")

    for line in text:
        if word in line and line != exact_find: other_finds.append(line)

    if len(other_finds) > 0:
        if exact_find != "":
            if input("Hit enter to continue or 'x' to skip...\n") == "x":
                print("----------------------\n")
                continue
        print("--- Other matches ----")
        i = 0
        for line in other_finds:
            print(line)
            i += 1
            if i % 10 == 0:
                if input("---\nHit enter to show the next 10 lines or 'x' to skip...\n---\n") == "x":
                    break
        print("----------------------\n")

    if exact_find == "" and len(other_finds) == 0:
        print("Sorry, there are no entries that match that query\n")
