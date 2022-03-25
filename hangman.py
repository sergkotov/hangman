#Игра "Висельник" Слово выбирается случайно из списка
import random

def hangman():
    #word - загаданное слово. Цель игры - отгадать слово по буквам
    words = ["крот", "жираф", "окунь", "камень", "подушка", "друг", "лопата", "мухомор"]
    word = random.choice(words)
    wrong = 0
    stages = ["",
    "________        ",
    "|               ",
    "|       |       ",
    "|       O       ",
    "|     / | \     ",
    "|      / \      ",
    "|               ",
    ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    print(" ".join(board))
    while wrong < len(stages)-1: #игровой цикл
        print("\n")
        char = input("Введите букву: ")
        if char in rletters:
            char_index = rletters.index(char)
            board[char_index] = char
            rletters[char_index] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[:e]))
        if "__" not in board:
            print("Вы победили! Было загадано слово: " + " ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[:wrong + 1]))
        print("Вы проиграли! Было загадано слово: {}".format(word))

hangman()