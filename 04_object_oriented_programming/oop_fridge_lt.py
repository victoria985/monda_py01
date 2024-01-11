class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product: Product, quantity: float ):
        self.ingredients.append((product, quantity))

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


    def print_contents(self):
            print("Recipe Ingredients:")
            for ingredient, quantity in self.ingredients:
               print(f"{ingredient.name}: {quantity}")
   


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))

    def remove_product(self, name: str, quantity: float):
        product_id, product = self.check_product(name)    
        if product is not None:
            product.quantity -= quantity                 
        if product.quantity <= 0:                     
            self.contents.pop(product_id)             
        else:
           self.contents.remove(Product(name, quantity))
                

    def print_contents(self):
            print("Fridge Contents:")
            for product in self.contents:                   
                print(product)


    def check_recipe(self, recipe: Recipe):
        for ingredient in recipe.ingredients:
            product_id, product = self.check_product(ingredient.name)
            if product is None or product.quantity < ingredient.quantity:
                print("All ingredients in the fridge.")    
            else:
                print("Is not enough {product} in the fridge")   

    def print_recipe_ingridients(self):
            print("Recipe ingridients:")   
            for ingredient in self.contents:  
                print(ingredients)        
                
 
def main():
    fridge = Fridge()
    recipe = Recipe()

    while True:
        print('---Fridge---')
        print('0: exit')
        print('1: add product')
        print('2: remove product ')
        print('3: check product')
        print('4: check quantity')
        print('5: print fridge contents')
        print('6: check recipe')
        choice = input('Choice 0-6')
        if choice == "0":
           break
        elif choice == 1:
            name = input('Product name:')
            quantity = input('Product quantity:')
            fridge.add_product(name, quantity)
        elif choice == 2: 
            name = input('Product name:')
            quantity = input('Product quantity:')
            fridge.remove_product(name, quantity) 
        elif choice == 3: 
            product_name = input('Product name:')
            product_id, product = fridge.check_product(product_name)
            if product is not None:
                print(f'{product_name} is in the fridge')
            else:
                print(f'{product_name} is not found in the fridge') 
        elif choice == 4: 
            name = input('Product:')
            product_id, product = fridge.check_product(name)
            if product is not None:
                print(f'{product.name} {product.quantity}')
            else:
                print(f'{product_name} is not found in the fridge')               




    


    



    # meniukas | vartotojo sasaja

# apple = Product('apple', 1)
# another_apple = Product('apple', 1)

# print(apple == another_apple)
