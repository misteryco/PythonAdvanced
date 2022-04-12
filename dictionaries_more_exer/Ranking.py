contest_data = input()
contests = {}
users_data = {}
while contest_data != "end of contests":
    data = contest_data.split(":")
    contest_name = data[0]
    contest_pass = data[1]
    contests[contest_name] = contest_pass
    contest_data = input()
# print(contests)

users_input = input()
while users_input != "end of submissions":
    submission = users_input.split('=>')
    contest = submission[0]
    password = submission[1]
    username = submission[2]
    points = int(submission[3])
    if contest in contests and contests[contest] == password:
        if username in users_data:
            if contest in users_data[username]:
                if users_data[username][contest] < points:
                    users_data[username][contest] = points
            else:
                users_data[username][contest] = points
        else:
            users_data[username] = {contest:points}
    users_input = input()
# print(users_data)

# users_data = sorted(users_data.keys())
max_user_and_points = ["none", -1]

for user, contests in users_data.items():
    sum_of_user_points = 0
    for contest, points in contests.items():
        sum_of_user_points += points
    if sum_of_user_points > max_user_and_points[1]:
        max_user_and_points = [user, sum_of_user_points]

print(f"Best candidate is {max_user_and_points[0]} with total {max_user_and_points[1]} points.")
print(f"Ranking:")
ordered_users = sorted(users_data.keys())
for user in ordered_users:
    print(f"{user}")
    for contest_ in sorted(users_data[user].items(), key = lambda kv: (kv[1], kv[0]), reverse=True):
        print(f"#  {contest_[0]} -> {contest_[1]}")