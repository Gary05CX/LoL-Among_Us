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
    print("The .txt file has been done.")
