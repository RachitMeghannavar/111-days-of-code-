class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


tejas = User("Tejas", "001")
rachit = User("Rachit", "002")
print(rachit.name)
print(rachit.id)
print(rachit.followers)
print(rachit.following)

tejas.follow(rachit)
print(f"Following Tejas: {tejas.following}")
print(f"Followers Rachit: {rachit.followers}")
