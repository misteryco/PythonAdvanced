days = int(input())
players = int(input())
energy_of_the_group = float(input())
water_per_person = float(input())
food_per_person = float(input())

total_food = food_per_person * players * days
total_water = water_per_person * players * days
not_enough_energy = False

for day in range(1, days + 1):
    daily_loss_of_energy = float(input())
    energy_of_the_group -= daily_loss_of_energy
    if energy_of_the_group <= 0:
        not_enough_energy = True
        break
    if day % 2 == 0:
        energy_of_the_group += 0.05 * energy_of_the_group
        total_water -= 0.3 * total_water
    if day % 3 == 0:
        energy_of_the_group += 0.10 * energy_of_the_group
        total_food -= total_food / players

if not_enough_energy:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {energy_of_the_group:.2f} energy!")