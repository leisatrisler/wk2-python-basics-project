#!/usr/bin/python

import tkinter as tk
from PIL import ImageTk, Image
import tkinter as tk


# 1. Item Description, Image, File, Item Price
# 2. Confident Carrot, confident carrot, .png, $0.99
# 3. Romantic Radishes, romantic radishes, .png, $1.50
# 4. Panic Pear, panic pear, .png, $0.75
# 5. Obnoxious Onion, obnoxious onion, .png, $0.50
# 6. Melancholy Mushroom, melancholy mushroom, .png, $1.25
# 7. Affection Asparagus, affection asparagus, .png, $4.25
# 8. Patient Peas, patient peas, .png, $2.25
# 9. Bubbly Banana, bubbly banana, .png, $0.75
# 10. Cheeky Cherries, cheeky cherries, .png, $3.75
# 11. Rebellious Raspberries, rebellious raspberries,.png, $2.75
# 12. Amused Apple, amused apple, .png, $1.75

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


def add_to_cart():
    item = entry.get()
    if item:
        cart.insert(tk.END, item)
        entry.delete(0, tk.END)


def remove_from_cart():
    selected_indices = cart.curselection()
    for index in reversed(selected_indices):
        cart.delete(index)


root = tk.Tk()
root.title("Veggie Tales")


entry = tk.Entry(root, width=30)
entry.pack(pady=10)


add_button = tk.Button(root, text="Add to Cart", command=add_to_cart)
add_button.pack()


cart = tk.Listbox(root, width=50)
cart.pack(pady=10)


remove_button = tk.Button(root, text="Remove from Cart", command=remove_from_cart)
remove_button.pack()

# Load and display images
#   "item": {
#         "id": 2,
#         "name": "Confident Carrot",
#         "image": "./confident_carrot.png",
#         "price": 0.99,
#     },
images = []
for item in items:
    print(item)
    details = item["item"]
    image = Image.open(details["image"])
    image = image.resize((250, 250))
    photo = ImageTk.PhotoImage(image)
    images.append(photo)

    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

root.mainloop()
