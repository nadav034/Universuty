from __future__ import annotations
from PIL import Image
import matplotlib.pyplot as plt


class Post:

    def __init__(self, owner: User, type, body, price: float = None, location=None):
        self.owner = owner
        self.type = type
        self.body = body
        self.price = price
        self.location = location
        self.likes_counter = 0
        self.comments_counter = 0
        self.likes = list()
        self.comments = list()
        available = "For sale!"
        self.available = available

    def __str__(self):
        if self.type == "Text":
            return (f'{self.owner.name} published a post:\n"{self.body}"\n')
        if self.type == "Image":
            return (f"{self.owner.name} posted a picture\n")
        if self.type == "Sale":
            return (f"{self.owner.name} posted a product for sale:\n "
                  f"For sale! {self.body}, price:{self.price}, pickup from:{self.location}\n ")

    def like(self, user):
        if user.name not in self.likes:
            self.likes_counter += 1
            self.likes.append(user)
            str = "like"
            self.notify(str,user, self.type, self.body)

    def comment(self, user, str):
        self.comments_counter += 1
        self.comments.append(str)
        str1 = "comment"
        self.notify(str1,user, self.type, str)

    def notify(self,action, user, type: str, body=None):
        if action.__eq__("like"):
            if user != self.owner:
                self.owner.notifications.append(self.like_update(user))
                print(f"notification to {self.owner.name}: {user.name} liked your post ")

        if action.__eq__("comment"):
            if user != self.owner:
                self.owner.notifications.append(self.comment_update(user, body))
                print(f"notification to {self.owner.name}: {user.name} comment on your post: {body} ")

        if action.__eq__("post"):
            for user in self.owner.followers:
                user.notifications.append(self.post_update(self.owner))

    def like_update(self, user):
        if user is not None:
            a: str = f"{user.name} liked your post"
            return a

    def comment_update(self, user, txt):
        if user is not None:
            a: str = f"{user.name} comment on your post: {txt}"
            return a

    def post_update(self, user):
        if user is not None:
            a: str = f"{user.name} has a new post"
            return a

    def sale_update(self):
        if self.type == "Sale":
            self.available = "For sale! "

    def sold(self, password):
        if password == self.owner.password:
            if self.type == "Sale":
                self.available = "Sold! "
                print(f"{self.owner.name}'s product is sold\n")
                print(print(f"{self.owner.name} posted a product for sale:\n "
                            f"{self.available}{self.body}, price:{self.price}, pickup from:{self.location} "))

    def discount(self, discount: float, password):
        if self.owner.password == password:
            self.price = self.price - (self.price * discount / 100)
            print(f"Discount on {self.owner.name} product! the new price is: {self.price}")

    def display(self):
        if self.type == "Image":
            img = Image.open(self.body)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
            print("Shows picture")
