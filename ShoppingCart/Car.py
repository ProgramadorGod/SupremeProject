from ShoppingCart.models import ProductRelation

# Car.py
class Car:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        ShoppingCart = self.session.get('ShoppingCart')

        if not ShoppingCart:
            ShoppingCart = self.session["ShoppingCart"] = {} 


        self.ShoppingCart = ShoppingCart

        
    def AddProduct(self, product, user):
        ProductRelation.objects.create(
            user=user,
            product=product
        )

    def SubtractPds(self, Product, user):
        product_id = str(Product.id)

        # Intenta obtener el objeto ProductRelation del usuario y producto específicos
        product_relation = ProductRelation.objects.filter(user=user, product=Product).first()

        if product_relation:
            # Si existe, elimina la relación
            product_relation.delete()

            # Actualiza el carrito
            if product_id in self.ShoppingCart:
                del self.ShoppingCart[product_id]
        
        self.SaveCart()


    def Delete(self, Product,user):
        product_id = str(Product.id)

        # Intenta obtener el objeto ProductRelation del usuario y producto específicos
        product_relation = ProductRelation.objects.filter(user=user, product=Product)

        if product_relation:
            # Si existe, elimina la relación
            product_relation.delete()

            # Actualiza el carrito
            if product_id in self.ShoppingCart:
                del self.ShoppingCart[product_id]
        
        self.SaveCart()

    def EmptyCart(self,user):
        product_relation = ProductRelation.objects.filter(user=user)
        if product_relation:
            product_relation.delete()
        
        



    def SaveCart(self):
        self.session["ShoppingCart"] = self.ShoppingCart
        self.session.modified = True

