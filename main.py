import random
import email.message
import smtplib
import time
import json

def mode_setup():
    print("How many player (3~5):")
    number_of_player = int(input())
    return number_of_player

def get_player_email(number_of_player):
    i = 0
    player_email_list = []
    for i in range(number_of_player):
        print(f"Input player{i + 1}'s email:")
        player_email_list.append(str(input()))
        i = i + 1
    return player_email_list

def random_imposter(number_of_player):
    i = 0
    imposter_list = []
    for i in range(number_of_player):
        imposter_list.append(random.randrange(2))
        i = i + 1
    if sum(imposter_list) == 0:
        imposter_list[random.randrange(number_of_player)] = 1
    return imposter_list



def send_email(player_email, player_role):
    with open('password.json','r',encoding='utf8') as jfile:
        jdata = json.load(jfile)


    msg = email.message.EmailMessage()
    msg["From"] = jdata['email']
    msg["To"] = player_email
    msg["Subject"] = player_role
    msg.set_content(f"You are {player_role} player.")

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(jdata['email'], jdata['password'])
    server.send_message(msg)
    server.close()

def TXT_rec(number_of_player, email_list, imposter_list):
    i = 0
    file = open("rec.txt", mode="w", encoding="utf-8")
    for i in range(number_of_player):
        if imposter_list[i] == 0:
            player_roles = "normal player"
        else:
            player_roles = "imposter player"
        file.write(email_list[i])
        file.write(" : ")
        file.write(player_roles)
        file.write("\n")
    file.close()

def main():
    i = 0
    number_of_player = mode_setup()
    email_list = get_player_email(number_of_player)
    imposter_list = random_imposter(number_of_player)

    for i in range(number_of_player):
        if imposter_list[i] == 0:
            player_role = "normal"
        else:
            player_role = "imposter"
        player_email = email_list[i]
        send_email(player_email, player_role)
        i = i + 1
    TXT_rec(number_of_player, email_list, imposter_list)

if __name__ == "__main__":
    main()
