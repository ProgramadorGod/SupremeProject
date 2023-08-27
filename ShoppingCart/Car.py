class Car:
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session

        ShoppingCart = self.session.get('ShoppingCart')

        if not ShoppingCart:
            ShoppingCart = self.session["ShoppingCart"] = {}

        else:
            self.ShoppingCart = ShoppingCart
    

    def AddProducts(self,Product):
        if (str(Product.id) not in self.ShoppingCart.keys()):
                self.ShoppingCart[Product.id]={
                     "Product_Id":Product.id,
                     "Name":Product.Name,
                     "Price":str(Product.Price),
                     "Mount":1,
                     "Image":Product.Image.url,
                }

        else:
            for key, value in self.ShoppingCart.items():
                if key == str(Product.id):
                     value["Mount"] = value["Mount"]+1
                     break


        self.SaveCart()


    def SaveCart(self):
        self.session["ShoppingCart"] = self.ShoppingCart
        self.session.modified = True


    def Delete(self, Product):
        Product.id = str(Product.id)
        if Product.id in self.ShoppingCart:
            del self.ShoppingCart[Product.id] 
            self.SaveCart()
    
    def SubtractPds(self, Product):
        for key, value in self.ShoppingCart.items():
            if key == str(Product.id):
                    value["Mount"] = value["Mount"]-1
                    if value["Mount"] < 1:
                         self.Delete(Product)
                         
                    break
            
        self.SaveCart()


    def EmptyCart(self):
    
        self.session["ShoppingCart"] = {}
        self.session.modified = True
