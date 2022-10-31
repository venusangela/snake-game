with open("data.txt") as file:
    score = int(file.read())
    print(score)
    print(type(score))
