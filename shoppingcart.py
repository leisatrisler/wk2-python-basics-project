import tkinter as tk
from PIL import Image, ImageTk


class ShoppingCart(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("vg Cart")
        self.items = []
        self.total = 0.0

        self.item_listbox = tk.Text(self, width=50, height=10)
        self.item_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.cart_listbox = tk.Listbox(self, width=50)
        self.cart_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.total_label = tk.Label(self, text="Total: $0.00")
        self.total_label.pack()

        self.images = []
        for item in items:
            my_items = item["item"]
            print(my_items)
            image = Image.open(my_items["image"])
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.images.append(photo)
            self.item_listbox.image_create(tk.END, image=photo)
            self.item_listbox.insert(tk.END, "\n" + my_items["name"])

        self.add_button = tk.Button(self, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack(pady=10)

        self.remove_button = tk.Button(
            self, text="Remove from Cart", command=self.remove_from_cart
        )
        self.remove_button.pack(pady=10)

    def add_to_cart(self):
        selected_index = self.item_listbox.index(tk.INSERT)
        if selected_index:
            selected_item = items[selected_index - 1]
            self.cart_listbox.insert(tk.END, selected_item["name"])
            self.total += selected_item["price"]
            self.update_total_label()

    def remove_from_cart(self):
        selected_index = self.cart_listbox.curselection()
        if selected_index:
            removed_item = self.cart_listbox.get(selected_index)
            self.cart_listbox.delete(selected_index)
            selected_item = next(
                (item for item in items if item["name"] == removed_item), None
            )
            if selected_item:
                self.total -= selected_item["price"]
                self.update_total_label()

    def update_total_label(self):
        self.total_label.config(text="Total: ${:.2f}".format(self.total))


if __name__ == "__main__":
    items = [
        {
            "item": {
                "id": 2,
                "name": "Confident Carrot",
                "image": "./confident_carrot.png",
                "price": 0.99,
            },
            "item": {
                "id": 3,
                "name": "Romantic Radishes",
                "image": "./romantic_radishes.png",
                "price": 1.50,
            },
            "item": {
                "id": 4,
                "name": "Panic Pear",
                "image": "./panic-pear.png",
                "price": 0.75,
            },
            "item": {
                "id": 5,
                "name": "Obnoxious Onion",
                "image": "./obnoxious_onion.png",
                "price": 0.50,
            },
            "item": {
                "id": 6,
                "name": "Melancholy Mushroom",
                "image": "./melancholy_mushroom.png",
                "price": 1.25,
            },
            "item": {
                "id": 7,
                "name": "Affection Asparagus",
                "image": "./affection_asparagus.png",
                "price": 4.25,
            },
            "item": {
                "id": 8,
                "name": "Patient Peas",
                "image": "./patient_peas.png",
                "price": 2.25,
            },
            "item": {
                "id": 9,
                "name": "Bubbly Banana",
                "image": "./bubbly_banana.png",
                "price": 0.75,
            },
            "item": {
                "id": 10,
                "name": "Cheeky Cherries",
                "image": "./cheeky_cherries.png",
                "price": 3.75,
            },
            "item": {
                "id": 11,
                "name": "Rebellious Raspberries",
                "image": "./rebellious_raspberries.png",
                "price": 2.75,
            },
            "item": {
                "id": 12,
                "name": "Amused Apple",
                "image": "./amused_apple.png",
                "price": 1.75,
            },
        }
    ]
app = ShoppingCart()
app.mainloop()
