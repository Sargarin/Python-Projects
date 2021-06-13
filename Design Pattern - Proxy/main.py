import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class Interface(ABC):

    @abstractmethod
    def display_image(self, filename):
        pass


class Image(Interface):

    def display_image(self, filename):
        print("loading " + filename)
        self.image = plt.imread(filename)
        print("display " + filename)
        plt.imshow(self.image)
        plt.show()


class ProxyImage(Interface):

    def __init__(self) -> None:
        self.img = Image()

    def display_image(self, filename):
        print("loading " + filename)
        self.image = plt.imread(filename)
        print("display " + filename)

if __name__ == "__main__":
    Image.display_image(Image,"40mbIMG.jpg")

    proxy_image1 = ProxyImage()
    proxy_image1.display_image("40mbIMG.jpg")
