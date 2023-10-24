import time as t
import os
import json
from functions.process.txtfile import *
from functions.process.emailprog import *
from functions.output.imposter import *
from functions.input.getinput import *



def main():    
    with open("password.json",'r',encoding='utf8') as jfile:
        jdata = json.load(jfile)

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
        send_email(player_email, player_role, jdata['email'], jdata['password'])
        i = i + 1

    TXT_rec(number_of_player, email_list, imposter_list)



if __name__ == "__main__":
    main()
    print("Programm finished.")