from __future__ import annotations

from Post import Post



class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password
        self.log = True
        self.post_number = 0
        self.followers = list()
        self.following = list()
        self.posts = list()
        self.notifications = list()

    def __str__(self):
        return (f"User name: {self.name}, Number of posts: {self.post_number}, Number of followers: {len(self.followers)}")

    def follow(self, user: User):
        if user not in self.following:
            self.following.append(user)
            print(f"{self.name} started following {user.name}")
            user.followers.append(self)

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            user.followers.remove(self)
            print(f"{self.name} unfollowed {user.name}")

    def publish_post(self, type: str, body, price=None, location=None):
        if type.__eq__("Text"):
            p1 = Post(self, "Text", body)
            print(f'{self.name} published a post:\n"{body}"\n')
            str1= "post"
            p1.notify(str1,p1.owner, p1.type, p1.body)
            self.post_number+=1
            return p1
        if type.__eq__("Image"):
            p1 = Post(self, "Image", body)
            print(f"{self.name} posted a picture\n")
            str1 = "post"
            p1.notify(str1, p1.owner, p1.type, p1.body)
            self.post_number += 1
            return p1
        if type.__eq__("Sale"):
            p1 = Post(self, "Sale", body, price, location)
            print(f"{self.name} posted a product for sale:\n "
                  f"For sale! {body}, price:{price}, pickup from:{location}\n ")
            str1 = "post"
            p1.notify(str1, p1.owner, p1.type, p1.body)
            self.post_number += 1
            return p1

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notification in self.notifications:
            print(notification)
        print("\n")






