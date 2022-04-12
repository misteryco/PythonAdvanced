class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

line = input()
emails = []
while line != "Stop":
    line = line.split(" ")
    sender = line[0]
    receiver = line[1]
    content = line[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

sended_list = [int(x) for x in input().split(", ")]

for element in sended_list:
    emails[element].send()

for email in emails:
    print(email.get_info())