

class Product():
    def __init__(self,pid,pnm,pqty,pprice,pven):
        self.productID=int(pid)
        self.productName=pnm
        self.productQuantiyt=pqty
        self.productPrice=pprice
        self.productVendor=pven

    def __str__(self):
        return f"""{self.__dict__}"""

    def __repr__(self):
        return str(self)