class ShoppingCart:
    def __init__(self):
        self.items = []
        self.prices = []
        self.total = 0.0
        self.items = [
            {
                "id": 2,
                "name": "Confident Carrot",
                "image": "./confident_carrot.png",
                "price": 0.99,
            },
            {
                "id": 3,
                "name": "Romantic Radishes",
                "image": "./romantic_radishes.png",
                "price": 1.50,
            },
            {
                "id": 4,
                "name": "Panic Pear",
                "image": "./panic-pear.png",
                "price": 0.75,
            },
            {
                "id": 5,
                "name": "Obnoxious Onion",
                "image": "./obnoxious_onion.png",
                "price": 0.50,
            },
            {
                "id": 6,
                "name": "Melancholy Mushroom",
                "image": "./melancholy_mushroom.png",
                "price": 1.25,
            },
            {
                "id": 7,
                "name": "Affection Asparagus",
                "image": "./affection_asparagus.png",
                "price": 4.25,
            },
            {
                "id": 8,
                "name": "Patient Peas",
                "image": "./patient_peas.png",
                "price": 2.25,
            },
            {
                "id": 9,
                "name": "Bubbly Banana",
                "image": "./bubbly_banana.png",
                "price": 0.75,
            },
            {
                "id": 10,
                "name": "Cheeky Cherries",
                "image": "./cheeky_cherries.png",
                "price": 3.75,
            },
            {
                "id": 11,
                "name": "Rebellious Raspberries",
                "image": "./rebellious_raspberries.png",
                "price": 2.75,
            },
            {
                "id": 12,
                "name": "Amused Apple",
                "image": "./amused_apple.png",
                "price": 1.75,
            },
        ]

    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.prices.append(item_price)
        self.total += item_price

    def remove_item(self, item_name):
        if item_name in self.items:
            index = self.items.index(item_name)
            item_price = self.prices[index]
            self.items.remove(item_name)
            self.prices.remove(item_price)
            self.total -= item_price

    def get_total(self):
        return self.total

    def list_items(self):
        for item in self.items:
            print("print")
            print(item)
            my_item = item
            print(my_item)


def main():
    my_cart = ShoppingCart()

    while True:
        action = input(
            "Welcome to Veggie Tales, what would you like to do?:  (add/remove/checkout/listexit): "
        )

        if action == "add":
            item_name = input("Please enter the item name: ")
            item_price = float(input("Please enter the item price: "))
            my_cart.add_item(item_name, item_price)
            print("Item(s) added to cart.")

        elif action == "remove":
            item_name = input("Enter item name: ")
            my_cart.remove_item(item_name)
            print("Item removed from cart.")

        elif action == "checkout":
            total = my_cart.get_total()
            print(f"Total price: ${total:.2f}")
            break
        elif action == "list":
            my_cart.list_items()

        elif action == "exit":
            break

        else:
            print("Invalid action. Please try again.")


if __name__ == "__main__":
    main()
