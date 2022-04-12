import operator


def player_dict(unsplit_player_data):
    data_list = unsplit_player_data.split(" -> ")
    player = data_list[0]
    pos = data_list[1]
    skill = int(data_list[2])
    if player in players_pool:
        if pos in players_pool[player]:
            if skill > players_pool[player][pos]:
                players_pool[player][pos] = skill
        else:
            players_pool[player][pos] = skill
    else:
        players_pool[player] = {pos: skill}


def duel(unsplit_duel_data):
    splited_players = unsplit_duel_data.split(" vs ")
    pl_1 = splited_players[0]
    pl_2 = splited_players[1]
    if pl_1 in players_pool and pl_2 in players_pool:
        for position in players_pool[pl_1]:
            if position in players_pool[pl_2]:
                if players_pool[pl_1][position] > players_pool[pl_2][position]:
                    del players_pool[pl_2]
                elif players_pool[pl_1][position] < players_pool[pl_2][position]:
                    del players_pool[pl_1]


def total_skill_player():
    player_max_skill = ["", -1]
    for pl, data in players_pool.items():
        sum__ = 0
        for position, skill in data.items():
            sum__ += skill
        if sum__ > player_max_skill[1]:
            player_max_skill = [pl, sum__]
    return player_max_skill


def sum_skill_per_player(player_name):
    playerr_sum_skill = 0
    for position, skill in players_pool[player_name].items():
        playerr_sum_skill += skill
    return playerr_sum_skill


players_pool = {}
player_data = input()
while player_data != "Season end":
    if "->" in player_data:
        player_dict(player_data)
    elif "vs" in player_data:
        duel(player_data)
    player_data = input()

# print(players_pool)
# best_player = total_skill_player()
# print(f"{best_player[0]}: {best_player[1]} skill")


total_skill_dict = {}
for pl in players_pool:
    total_skill_dict[pl] = sum_skill_per_player(pl)

ordered_users = sorted(total_skill_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
for user in ordered_users:
    print(f"{user[0]}: {user[1]} skill")
    ordered_positions = sorted(players_pool[user[0]].items(), key=operator.itemgetter(0), reverse=False)
    ordered_skill_pos = (sorted(ordered_positions, key=operator.itemgetter(1), reverse=True))
    for posittion_ in ordered_skill_pos:
        print(f"- {posittion_[0]} <::> {posittion_[1]}")
