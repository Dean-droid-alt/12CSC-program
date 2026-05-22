import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Home page")

def home_page():
    image = Image.open("Image_Gallery/Homepage.png") #Opens image from image gallery folder
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

    name_entry = tk.Entry(root, width=25, bd=2.5, font= ("Arial", 20)) #Creates the name entry box with specific width, length and font
    name_entry.bind('<Enter>')
    name_entry.place(relx=0.5, rely=0.48, anchor="center") #Aligns the name entry box to the centre of the screen and moves it to a suitable position

    outcome_label = tk.Label(root, text="Please enter your name", font=("Arial",9), bg="white")
    outcome_label.place(relx=0.5, rely=0.53, anchor="center")

    def name_checker():
        name= name_entry.get()
        if any(char.isdigit() for char in name): #Checks whether users name has any numbers in it
            outcome_label.config(text="Cannot have numbers in your name, try again", fg="red") #Does not let the user move on to the next page and changes the text into the error message
        elif name.strip() == "": #Checks whether user has entered anything into the box
            outcome_label.config(text="Please enter a name, try again", fg="red") #Does not let the user move on to the next page and changes the text into the error message
        elif any(char in "~!@#$%^&*()_+{}|:<>?*-=[]\\;',." for char in name): #Checks whether users name has any symbols in it
            outcome_label.config(text="Cannot have special characters, try again", fg="red") #Does not let the user move on to the next page and changes the text into the error message
        else:
            outcome_label.config(text= "Success!", fg="green")
            root.after(1750, open_new_window)

    play_button = tk.PhotoImage(file="Image_Gallery/Play_button.png")
    btn = tk.Button(root, image=play_button, cursor="hand2", command=name_checker)
    btn.image = play_button
    btn.place(relx=0.5, rely=0.77, anchor="center")

    def on_enter(enter):
        btn.config(bg = "#000000")

    def on_leave(leave):
        btn.config(bg = "#d8d3c9")

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

home_page()

Questions_answers = [
    {"Questions": "What is the capital of Canada?", "Options": ["Montreal","Toronto","Vancouver","Ottawa"], "Answer": "Ottawa", "Background": "Image_Gallery/Q1.png"},
    {"Questions": "What country is this?", "Options": ["India","China","Japan","Indonesia"], "Answer": "India"},
    {"Questions": "What is this famous landmark?", "Options": ["Statue of liberty","Stonehenge","Christ The Redeemer", "Colosseum"], "Answer": "Christ the redeemer"},
    {"Questions": "The ________ desert is the largest desert in the world", "Options": ["Antarctic","Arctic","Sahara","Arabian"],"Answer": "Antarctic"},
    {"Questions": "What is the only continent on Earth that contains land in all four hemispheres?", "Options": ["North America","South America","Africa","Asia"],"Answer": "Africa"}]

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Questions page")
    next_image = Image.open("Image_Gallery/Question_page.png")
    next_photo = ImageTk.PhotoImage(next_image)
    image_label = tk.Label(new_window, image=next_photo)
    image_label.image = next_photo
    image_label.pack()

    Answer1_button = tk.PhotoImage(file="Image_Gallery/Answer1.png")
    btn = tk.Button(new_window, image=Answer1_button, cursor="hand2")
    btn.image = Answer1_button
    btn.place(relx=0.38, rely=0.75, anchor="center")

    Answer2_button = tk.PhotoImage(file="Image_Gallery/Answer2.png")
    btn = tk.Button(new_window, image=Answer2_button, cursor="hand2")
    btn.image = Answer2_button
    btn.place(relx=0.625, rely=0.75, anchor="center")

    Answer3_button = tk.PhotoImage(file="Image_Gallery/Answer3.png")
    btn = tk.Button(new_window, image=Answer3_button, cursor="hand2")
    btn.image = Answer3_button
    btn.place(relx=0.38, rely=0.92, anchor="center")

    Answer4_button = tk.PhotoImage(file="Image_Gallery/Answer4.png")
    btn = tk.Button(new_window, image=Answer4_button, cursor="hand2")
    btn.image = Answer4_button
    btn.place(relx=0.625, rely=0.92, anchor="center")

    Exit_button = tk.PhotoImage(file="Image_Gallery/Exit_button.png")
    btn = tk.Button(new_window, image=Exit_button, cursor="hand2", command=home_page)
    btn.image = Exit_button
    btn.place(relx=0.05, rely=0.09, anchor="center")

    Next_button = tk.PhotoImage(file="Image_Gallery/Next_button.png")
    btn = tk.Button(new_window, image=Next_button, cursor="hand2")
    btn.image = Next_button
    btn.place(relx=0.80, rely=0.845, anchor="center")

    root.withdraw()

root.mainloop()