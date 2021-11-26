def print_dictionary():
    with open('dictionary.txt', 'r') as dic:
        for f in dic.readlines():
            d = f.rstrip()
            word, meaning = d.split('|')
            print(f"word = {word} meaning = {meaning}")


def search():
    count = 0
    search = input("enter the word you want to search")
    with open('dictionary.txt', 'r') as dic:
        for f in dic.readlines():
            d = f.rstrip()
            words, meanings = d.split('|')
            if search == words:
                print(f'''word found 
                {words} means {meanings}
                ''')
                count += 1
            else:
                pass
    if count == 0:
        print("There is no such word in our dictionary. ")


while True:
    user_input = input(''' 
Please Enter the command as per your wish
Press 0 for Exit
Press 1 for seeing whole dictionary    
Press 2 for Search for meaning of a word
-> ''')
    if user_input == '0':
        break
    elif user_input == '1':
        print_dictionary()
    elif user_input == '2':
        search()
    else:
        print("Invalid Command Please Enter the correct one. Or Press 0 to Exit")
