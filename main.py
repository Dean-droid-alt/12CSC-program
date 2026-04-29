import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
image = Image.open("Image_Gallery/Homepage.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()
root.mainloop()