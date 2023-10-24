import random



def random_imposter(number_of_player):
    i = 0
    imposter_list = []
    for i in range(number_of_player):
        imposter_list.append(random.randrange(2))
        i = i + 1
    if sum(imposter_list) == 0:
        imposter_list[random.randrange(number_of_player)] = 1
    return imposter_list