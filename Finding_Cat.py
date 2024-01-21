print("Welcome to the Finding the Cat Game!")
print('''_                ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`
    /  ' `         ,       __.--'
    )/' _/     \   `-_,   /
    `-'" `"\_  ,_.-;_.-\_ ',   
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/''')
print("Your mission is the find the cat!")
way = str(input("Which way you should look? Right or Left\n"))

if way == 'Right':
    way2 = input("Go to the lake or Go to the house ?\n")
    if way2 == 'House':
        print("There are 3 doors. The color of the doors are Blue,Red and Green.")
        color = input("Which one are you going to choose?\n")
        if color == 'Blue':
            print("You drowned. Game Over!")
        elif color == 'Green':
            print("You found the cat!")
        else:
            print("You burned by fire. Game Over!")
    else:
        print("You are under attack of alligators. Game Over!")
else:
    print("You Fall into a hole. Game Over!")
