food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
month = 30
eated = 300
go_to_pet_store = False
for day in range(1, month+1):
    food -= eated
    if day % 2 == 0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= weight/3
    if food <= 0 or hay <= 0 or cover <= 0:
        go_to_pet_store = True
        break
if go_to_pet_store:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
