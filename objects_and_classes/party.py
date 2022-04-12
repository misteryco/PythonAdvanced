class Party:
    def __init__(self):
        self.people = []


party = Party()

persons = input()

while persons != "End":
    party.people.append(persons)
    persons = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
