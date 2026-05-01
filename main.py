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
btn.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()