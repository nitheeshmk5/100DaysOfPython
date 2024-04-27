class User:
    def __init__(self,username,id):
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1
        
nitheesh = User("nitheesh",1)
praveen = User("parveen",2)
dharshan = User("dharshan",3)

nitheesh.follow(praveen)
praveen.follow(nitheesh)
dharshan.follow(nitheesh)

print(f"Nitheesh followers count {nitheesh.followers}")