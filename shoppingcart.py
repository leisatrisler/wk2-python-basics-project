import tkinter as tk
from PIL import Image, ImageTk


class ShoppingCart(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Veggie Tales")
        self.items = []
        self.total = 0.0

        # this is the left box with icons
        self.item_listbox = tk.Text(self, width=75, height=75)
        self.item_listbox.pack(side=tk.LEFT, padx=50, pady=50)

        # this is the right box
        self.cart_listbox = tk.Listbox(self, width=50)
        self.cart_listbox.pack(side=tk.LEFT, padx=50, pady=50)

        # this is the far right add to cart and total
        self.total_label = tk.Label(self, text="Total: $0.00")
        # self.total_label.bind("<Button-1>", self.add_to_cart)
        self.total_label.pack()

        def on_click(event):
            print("I clicked")

        self.images = []
        for item in items:
            image = Image.open(item["image"])
            image = image.resize((220, 220))
            photo = ImageTk.PhotoImage(image)
            self.images.append(photo)
            self.item_listbox.insert(tk.END, "\n" + item["name"])
            self.item_listbox.image_create(tk.END, image=photo)

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
app = ShoppingCart()
app.mainloop()
