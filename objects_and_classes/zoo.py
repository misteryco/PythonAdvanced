class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, a_name):
        if species == "mammal":
            self.mammals.append(a_name)
        elif species == "fish":
            self.fishes.append(a_name)
        elif species == "bird":
            self.birds.append(a_name)
        Zoo.__animals +=1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        result += f"Total animals: {self.__animals}"

        return result


this_zoo = Zoo(input())
count_of_animals = int(input())

for animal in range(count_of_animals):
    this_animal = input().split()
    this_species = this_animal[0]
    this_name = this_animal[1]
    this_zoo.add_animal(this_species, this_name)

print(this_zoo.get_info(input()))

