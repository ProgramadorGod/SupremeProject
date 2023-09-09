# Car.py
class Car:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        ShoppingCart = self.session.get('ShoppingCart')

        if not ShoppingCart:
            ShoppingCart = self.session["ShoppingCart"] = {} 



        self.ShoppingCart = ShoppingCart
    def AddProduct(self, Product):
        product_id = str(Product.id)
        if product_id not in self.ShoppingCart:
            self.ShoppingCart[product_id] = {
                "Product_Id": Product.id,
                "Name": Product.Name,
                "Price": str(Product.Price),
                "Mount": 1,
                "Image": Product.Image.url,
            }
        else:
            for key, value in self.ShoppingCart.items():
                if key == product_id:
                    value["Mount"] += 1
                    break

        self.SaveCart()

    def SubtractPds(self, Product):
        for key, value in self.ShoppingCart.items():
            if key == str(Product.id):
                value["Mount"] -= 1
                if value["Mount"] < 1:
                    self.Delete(Product)
                break

        self.SaveCart()

    def Delete(self, Product):
        product_id = str(Product.id)
        if product_id in self.ShoppingCart:
            del self.ShoppingCart[product_id]
            self.SaveCart()

    def EmptyCart(self):
        self.session["ShoppingCart"] = {}
        self.session.modified = True

    def SaveCart(self):
        self.session["ShoppingCart"] = self.ShoppingCart
        self.session.modified = True

