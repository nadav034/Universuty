from User import User


class SocialNetworkMeta(type):
    def __call__(self, *args, **kwargs):
        pass


class SocialNetwork:
    def __init__(self, name_of_network: str):
        self.name = name_of_network
        self.user_list: list[User] = []
        print(f"The social network {name_of_network} was created!")

    def __str__(self):
        resault_str =(f"{self.name} social network:\n")
        for user in self.user_list:
            resault_str += user.__str__()+ "\n"
        return resault_str


    def sign_up(self, username: str, password: str):
        if len(password) < 4 or len(password) > 8:
            return False
        if self.user_list.count(username):
            return False
        u1 = User(username, password)
        self.user_list.append(u1)
        self.log_in(u1,password)
        return u1

    def log_out(self, user_name):
        filtered = list(filter(lambda user: user.name == user_name, self.user_list))
        if len(filtered) != 1:
            return False
        user: User = filtered[0]
        user.log = False
        print(f"{user.name} disconnected")

    def log_in(self, user_name, password):
        filtered = list(filter(lambda user: user.name == user_name and user.password == password, self.user_list))
        if len(filtered) != 1:
            return False
        user: User = filtered[0]
        user.log = True
        print(f"{user.name} connected")
