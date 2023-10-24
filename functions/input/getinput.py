import re


i = 0


def mode_setup():
    print("How many player (3~5):")
    number_of_player = int(input())
    while number_of_player > 5 or number_of_player < 3:
        print("ERROR! Input must be bewteen 3 and 5")
        number_of_player = int(input("Input again (3~5)\n"))
    else:
        return number_of_player

def get_player_email(number_of_player):
    global i
    player_email_list = []
    while i in range(number_of_player):
        print(f"Input player{i + 1}'s email:")
        email = str(input()).low()
        at = re.search("@", email)
        dotcom = re.search(".com", email)
        if at and dotcom:
            player_email_list.append(email)
            i = i + 1
        else:
            print("ERROR! Input isn't a email format")
    return player_email_list
