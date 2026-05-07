import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

image = Image.open("Image_Gallery/Homepage.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

play_button = tk.PhotoImage(file="Image_Gallery/Play_button.png")
btn = tk.Button(root, image=play_button, cursor="hand2", command=lambda: label.pack_forget(), text="Hide Text")
btn.place(relx=0.5, rely=0.77, anchor="center")

class Quiz:
    def __init__(self,parent):
        Username = name_entry.get()
        if Username.isdigit():
            self.outcome_label.config(text="Cannot have numbers in your name, try again", fg="red")
        elif Username.strip() == "":
            self.outcome_label.config(text="Please enter a name, try again", fg="red")
        elif any(char in "~!@#$%^&*()_+{}|:<>?*-=[]\\;',." for char in Username):
            self.outcome_label.config(text="Cannot have special characters, try again", fg="red")
        else:
            root.after(1750, open_new_window)

name_entry = tk.Entry(root, width=25, bd=2.5, font= ("Arial", 20))
label = tk.Label(root, text=f"Welcome to the quiz {name_entry}",fg="green")
label.place(relx=0.5, rely=0.53, anchor="center")
name_entry.bind('<Return>', lambda event:name_entry.delete(0, tk.END))
name_entry.place(relx=0.5, rely=0.48, anchor="center")



def on_enter(event):
    btn.config(bg = "#000000")

def on_leave(event):
    btn.config(bg = "#d8d3c9")

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Questions page")
    next_image = Image.open("Image_Gallery/Question_page.png")
    next_photo = ImageTk.PhotoImage(next_image)
    image_label = tk.Label(new_window, image=next_photo)
    image_label.image = next_photo
    image_label.pack(pady=40)
    root.withdraw()


root.mainloop()