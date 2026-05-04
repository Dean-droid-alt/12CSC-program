import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

image = Image.open("Image_Gallery/Homepage.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

play_button = tk.PhotoImage(file="Image_Gallery/play_button.png")
btn = tk.Button(root, image=play_button, cursor="hand2", command=lambda: print("Clicked!"))
btn.place(relx=0.5, rely=0.71, anchor="center")

name_entry = tk.Entry(root, width=25, bd=2.5, font= ("Arial", 20))
Username = name_entry.get()
name_entry.place(relx=0.5, rely=0.5, anchor="center")


def on_enter(event):
    btn.config(bg = "#000000")

def on_leave(event):
    btn.config(bg = "#d8d3c9")

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)


root.mainloop()