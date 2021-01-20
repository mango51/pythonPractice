class Supermarket(object):
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def printLocation(self):
        print(self.location)

    def changeCategory(self, new_product):
        self.product = new_product

    def showList(self):
        print(self.product)

    def enterCustomer(self):
        self.customer = self.customer + 1

    def showInfo(self):
        print(self.name, self.location, self.product, self.customer)

marshmallow = Supermarket('서울','지에스슈퍼마켓','마시멜로우',30)

marshmallow.changeCategory('사탕')
marshmallow.showInfo()

newone = '달콤한 것'
marshmallow.changeCategory(newone)
marshmallow.showInfo()
