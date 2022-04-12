class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes

this_comment = Comment("Dan", "tuka ima tuka nema")
this_other_comment = Comment("Yan", "Other ima tuka nema", 121)
print(this_comment.username)
print(this_comment.content)
print(this_other_comment.likes)
