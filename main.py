import tkinter as tk #Tells python to load the tkinter module
from PIL import Image, ImageTk #Makes it so that I can use Image and ImageTK modules from the pillow library, this allows images to be processed

root = tk.Tk() #Creates the tkinter window
root.title("Home page") #Gives the title of my first window

def home_page(): #Creates a def function for all elements in the home page
    image = Image.open("Image_Gallery/Homepage.png") #Opens image from image gallery folder
    photo = ImageTk.PhotoImage(image) #Converts an image to a tkinter compatible formate
    label = tk.Label(root, image=photo) #Creates a widget that displays an image instead of text
    label.image = photo #Attaches the label to the image so that is not deleted by pythons memory cleanup
    label.pack()  #Makes the image for the homepage appear

    name_entry = tk.Entry(root, width=25, bd=2.5, font= ("Arial", 20)) #Creates the name entry box with specific width, length and font
    name_entry.bind('<Return>')
    name_entry.place(relx=0.5, rely=0.48, anchor="center") #Aligns the name entry box to the centre of the screen and moves it to a suitable position

    outcome_label = tk.Label(root, text="Please enter your name", font=("Arial",9), bg="white") #Creates a label with a specific message, font, font size and background
    outcome_label.place(relx=0.5, rely=0.53, anchor="center") #Aligns the name entry box to the centre of the screen and moves it to a suitable position

    def name_checker(): #Creates a def function for
        name = name_entry.get() #Retrieves the text the user has entered
        if any(char.isdigit() for char in name): #Checks whether users name has any numbers in it
            outcome_label.config(text="Cannot have numbers in your name, try again", fg="red") #Does not let the user move on to the next page and changes the text in outcome_label into the error message in red
        elif name.strip() == "": #Checks whether user has entered anything into the box
            outcome_label.config(text="Please enter a name, try again", fg="red") #Does not let the user move on to the next page and changes the text in outcome_label into the error message in red
        elif any(char in "~!@#$%^&*()_+{}|:<>?*-=[]\\;',." for char in name): #Checks whether users name has any symbols in it
            outcome_label.config(text="Cannot have special characters, try again", fg="red") #Does not let the user move on to the next page and changes the text in outcome_label into the error message in red
        else: #If there is no problem with the users name
            outcome_label.config(text= "Success!", fg="green") #Changes the text in outcome_label into the success message in green
            root.after(1750, open_new_window) #Lets the user move on to the next page using the open_new_window command and makes it happen after a short period of time

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
    {"Questions": "What country is this?", "Options": ["India","China","Japan","Indonesia"], "Answer": "India", "Background": "Image_Gallery/Q2.png"},
    {"Questions": "What is this famous landmark?", "Options": ["Statue of liberty","Stonehenge","Christ The Redeemer", "Colosseum"], "Answer": "Christ the redeemer", "Background": "Image_Gallery/Q3.png"},
    {"Questions": "The ________ desert is the largest desert in the world", "Options": ["Antarctic","Arctic","Sahara","Arabian"],"Answer": "Antarctic", "Background": "Image_Gallery/Q4.png"},
    {"Questions": "What is the only continent on Earth that contains land in all four hemispheres?", "Options": ["North America","South America","Africa","Asia"],"Answer": "Africa", "Background": "Image_Gallery/Q5.png"},
    {"Questions": "What is the capital of Japan?", "Options": ["Osaka", "Tokyo", "Sapporo", "Nagasaki"], "Answer": "Tokyo", "Background": "Image_Gallery/Q6.png"},
    {"Questions": "What country is this?", "Options": ["Sweden", "Norway", "Denmark", "England"], "Answer": "Sweden", "Background": "Image_Gallery/Q7.png"},
    {"Questions": "What is this famous landmark?", "Options": ["Neuschwanstein Castle", "Mont-Saint-Michel", "Potala Palace", "Petra"], "Answer": "Mont-Saint-Michel", "Background": "Image_Gallery/Q8.png"},
    {"Questions": "_______ is the country with the highest population", "Options": ["USA","Russia","China","India"], "Answer": "India", "Background": "Image_Gallery/Q9.png"},
    {"Questions": "What is the largest ocean on Earth?", "Options": ["Atlantic","Indian","Pacific","Arctic"], "Answer": "Pacific", "Background": "Image_Gallery/Q10.png"},
]

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Questions page")
    next_image = Image.open("Image_Gallery/Question_page.png")
    next_photo = ImageTk.PhotoImage(next_image)
    image_label = tk.Label(new_window, image=next_photo)
    image_label.image = next_photo
    image_label.pack()

    def check_answer(selected_answer):
        if selected_answer == ["Answer"]:
            print("Correct")
        else:
            print("Wrong")

    Answer1_button = tk.PhotoImage(file="Image_Gallery/Answer1.png")
    btn1 = tk.Button(new_window, image=Answer1_button, cursor="hand2", text=(["Options"][1]), command=lambda: check_answer(["Options"][1]))
    btn1.image = Answer1_button
    btn1.place(relx=0.38, rely=0.75, anchor="center")

    Answer2_button = tk.PhotoImage(file="Image_Gallery/Answer2.png")
    btn2 = tk.Button(new_window, image=Answer2_button, cursor="hand2")
    btn2.image = Answer2_button
    btn2.place(relx=0.625, rely=0.75, anchor="center")

    Answer3_button = tk.PhotoImage(file="Image_Gallery/Answer3.png")
    btn3 = tk.Button(new_window, image=Answer3_button, cursor="hand2")
    btn3.image = Answer3_button
    btn3.place(relx=0.38, rely=0.92, anchor="center")

    Answer4_button = tk.PhotoImage(file="Image_Gallery/Answer4.png")
    btn4 = tk.Button(new_window, image=Answer4_button, cursor="hand2")
    btn4.image = Answer4_button
    btn4.place(relx=0.625, rely=0.92, anchor="center")

    def exit_to_home():
        new_window.destroy()
        root.deiconify()

    Exit_button = tk.PhotoImage(file="Image_Gallery/Exit_button.png")
    btn = tk.Button(new_window, image=Exit_button, cursor="hand2", command=exit_to_home)
    btn.image = Exit_button
    btn.place(relx=0.05, rely=0.09, anchor="center")

    Next_button = tk.PhotoImage(file="Image_Gallery/Next_button.png")
    btn = tk.Button(new_window, image=Next_button, cursor="hand2", bg = "#aea498", activebackground="#aea498", highlightthickness=0)
    btn.image = Next_button
    btn.place(relx=0.80, rely=0.845, anchor="center")

    root.withdraw()

root.mainloop()