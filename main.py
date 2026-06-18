import tkinter as tk #Tells python to load the tkinter module
from PIL import Image, ImageTk #Makes it so that I can use Image and ImageTK modules from the pillow library, this allows images to be processed
from tkinter import messagebox

root = tk.Tk() #Creates the tkinter window
root.title("Home page") #Gives the title of my first window

def home_page(): #Creates a def function for all elements in the home page
    image = Image.open("Image_Gallery/Homepage.png") #Opens image from image gallery folder
    photo = ImageTk.PhotoImage(image) #Converts an image to a tkinter compatible format
    label = tk.Label(root, image=photo) #Creates a widget that displays an image instead of text
    label.image = photo #Attaches the label to the image so that is not deleted by pythons memory cleanup
    label.pack()  #Makes the image for the homepage appear

    global name_entry, outcome_label
    name_entry = tk.Entry(root, width=25, bd=2.5, font= ("Arial", 20)) #Creates the name entry box with specific width, length and font
    name_entry.bind('<Return>', lambda event: name_checker()) #Makes it so that you can enter your name with the enter button
    name_entry.place(relx=0.5, rely=0.48, anchor="center") #Aligns the name entry box to the centre of the screen and moves it to a suitable position

    outcome_label = tk.Label(root, text="Please enter your name", font=("Arial",9), bg="white") #Creates a label with a specific message, font, font size and background
    outcome_label.place(relx=0.5, rely=0.53, anchor="center") #Aligns the name entry box to the centre of the screen and moves it to a suitable position

    def name_checker(): #Creates a def function for the name checker part
        name = name_entry.get() #Retrieves the text the user has entered
        if any(char.isdigit() for char in name): #Checks whether users name has any numbers in it
            outcome_label.config(text="Cannot have numbers in your name, try again", fg="red") #Does not let the user move on to the next page and changes the text in outcome_label into the error message in red
        elif name.strip() == "": #Checks whether user has entered anything into the box
            outcome_label.config(text="Please enter a name, try again", fg="red") #Does not let the user move on to the next page and changes the text in outcome_label into the error message in red
        elif any(char in "~!@#$%^&*()_+{}|:<>?*-=[]\\;',." for char in name): #Checks whether users name has any symbols in it
            outcome_label.config(text="Cannot have special characters, try again", fg="red") #Does not let the user move on to the next page and changes the text in outcome_label into the error message in red
        else: #If there is no problem with the users name
            outcome_label.config(text= "Success!", fg="green") #Changes the text in outcome_label into the success message in green
            btn.config(command=lambda: None) #Disables the play button after it has been pressed
            root.after(1750, open_questions_page) #Lets the user move on to the next page using the open_questions_page command and makes it happen after a short period of time

    play_button = tk.PhotoImage(file="Image_Gallery/Play_button.png") #Coverts the image of the play button into a tkinter compatible format
    btn = tk.Button(root, image=play_button,  cursor="hand2", command=name_checker) #Creates a button with the play button image that turns the mouse into the pointer when it is hovered over and goes through the name_checker def function when clicked
    btn.image = play_button #Makes the play button have the attributes of the button
    btn.place(relx=0.5, rely=0.77, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def on_enter(enter): #Creates a variable for what happens when the mouse is on the button
        btn.config(bg = "#000000") #Makes the background of the button black

    def on_leave(leave): #Creates a variable for what happens when the mouse is off the button
        btn.config(bg = "#d8d3c9") #Makes the background of the button grayish orange

    btn.bind("<Enter>", on_enter) #Makes it so that when the mouse is hovering over the button it changes the outline of the button
    btn.bind("<Leave>", on_leave) #Makes it so that when the mouse is not hovering over the button it goes back to normal

home_page() #Runs the code in the home_page def function

Questions_answers = [ #Questions and answers for my quiz
    {"Questions": "What is the capital of Canada?", "Options": ["Montreal","Toronto","Vancouver","Ottawa"], "Answer": "Ottawa", "Background": "Image_Gallery/Q1.png"},
    {"Questions": "What country is this?", "Options": ["India","China","Japan","Indonesia"], "Answer": "India", "Background": "Image_Gallery/Q2.png"},
    {"Questions": "What is this famous landmark?", "Options": ["Statue of liberty","Stonehenge","Christ The Redeemer", "Colosseum"], "Answer": "Christ The Redeemer", "Background": "Image_Gallery/Q3.png"},
    {"Questions": "The ________ desert is the largest desert in the world", "Options": ["Antarctic","Arctic","Sahara","Arabian"],"Answer": "Antarctic", "Background": "Image_Gallery/Q4.png"},
    {"Questions": "What is the only continent on Earth that contains land in all four hemispheres?", "Options": ["North America","South America","Africa","Asia"],"Answer": "Africa", "Background": "Image_Gallery/Q5.png"},
    {"Questions": "What is the capital of Japan?", "Options": ["Osaka", "Tokyo", "Sapporo", "Nagasaki"], "Answer": "Tokyo", "Background": "Image_Gallery/Q6.png"},
    {"Questions": "What country is this?", "Options": ["Sweden", "Norway", "Denmark", "England"], "Answer": "Sweden", "Background": "Image_Gallery/Q7.png"},
    {"Questions": "What is this famous landmark?", "Options": ["Neuschwanstein Castle", "Mont-Saint-Michel", "Potala Palace", "Petra"], "Answer": "Mont-Saint-Michel", "Background": "Image_Gallery/Q8.png"},
    {"Questions": "_______ is the country with the highest population", "Options": ["USA","Russia","China","India"], "Answer": "India", "Background": "Image_Gallery/Q9.png"},
    {"Questions": "What is the largest ocean on Earth?", "Options": ["Atlantic","Indian","Pacific","Arctic"], "Answer": "Pacific", "Background": "Image_Gallery/Q10.png"},
]

question_index = 0

def open_questions_page(): #Creates a def function for the questions page
    new_window = tk.Toplevel(root) #Creates a secondary window
    new_window.title("Questions page") #Creates the title of the second window
    next_image = Image.open("Image_Gallery/Q1.png") #Opens the image from image gallery folder
    next_photo = ImageTk.PhotoImage(next_image) #Converts an image to a tkinter compatible format
    image_label = tk.Label(new_window, image=next_photo) #Creates a widget that displays an image instead of text
    image_label.image = next_photo #Attaches the label to the image so that is not deleted by pythons memory cleanup
    image_label.pack() #Makes the image for the questions page appear

    current_question = Questions_answers[question_index] #A variable current_question is created which contains the line of the dictionary that corresponds to the number from question_index

    def next_question(): #Creates a def function for the user to move on to the next question
        global question_index
        nonlocal selected_answer, selected_button

        if selected_answer is None:
            messagebox.showinfo("Error", "Please select an answer!")

        question_index +=1 #Adds 1 to the question_index so that it corresponds to the next question

        current_question = Questions_answers[question_index] #Current_question is updated as the question_index increased by 1

        if question_index < len(Questions_answers): #If the question_index number is within the number of questions that are in the dictionary
            btn1.config(text= current_question["Options"][0]) #Makes button 1 show the multichoice answer for the current question the user is on
            btn2.config(text=current_question["Options"][1]) #Makes button 2 show the multichoice answer for the current question the user is on
            btn3.config(text=current_question["Options"][2]) #Makes button 3 show the multichoice answer for the current question the user is on
            btn4.config(text=current_question["Options"][3]) #Makes button 4 show the multichoice answer for the current question the user is on

            image = Image.open(current_question["Background"]) #Opens image from the background part of the dictionary for the current question the user is on
            photo = ImageTk.PhotoImage(image) #Converts an image to a tkinter compatible format

            image_label.config(image=photo) #Makes sure python doesn't clear the image from memory
            image_label.image = photo #Makes sure python doesn't clear the image from memory

            btn1.config(bg="white")
            btn2.config(bg="white")
            btn3.config(bg="white")
            btn4.config(bg="white")

    def check_answer(selected_answer): #Creates a def function for the answer that the user selects to be checked whether it is right or wrong the selected_answer variable is created and holds the choice the user made
        current_question = Questions_answers[question_index]
        if selected_answer == current_question["Answer"]: #If the answer the user has selected is the same as the answer for the current question from the dictionary
            print("Correct")
        else: #If the answer the user has selected is not the same as the answer for the current question from the dictionary
            print("Wrong")

    Answer1_button = tk.PhotoImage(file="Image_Gallery/Answer1.png") #Converts the Answer1_button image into tkinter compatible format
    btn1 = tk.Button(new_window, image=Answer1_button, cursor="hand2", text= current_question["Options"][0]  #Creates a button with the Answer1_button image that turns the mouse into the pointer when it is hovered over and displays the text for the current question
    , compound="center", font=("Arial", 14, "bold"), relief="flat", fg="white", command=lambda: select_answer(btn1)) #The button text is set to display directly on top of the button, the font is changed, the button becomes flat, the text becomes white, and the answer is checked using the check_answer def function
    btn1.image = Answer1_button
    btn1.place(relx=0.38, rely=0.75, anchor="center")

    Answer2_button = tk.PhotoImage(file="Image_Gallery/Answer2.png") #Converts the Answer1_button image into tkinter compatible format
    btn2 = tk.Button(new_window, image=Answer2_button, cursor="hand2", text= current_question["Options"][1] #Creates a button with the Answer2_button image that turns the mouse into the pointer when it is hovered over and displays the text for the current question
    , compound="center", font=("Arial", 14, "bold"), relief="flat", fg="white", command=lambda: select_answer(btn2)) #The button text is set to display directly on top of the button, the font is changed, the button becomes flat, the text becomes white, and the answer is checked using the check_answer def function
    btn2.image = Answer2_button
    btn2.place(relx=0.625, rely=0.75, anchor="center")

    Answer3_button = tk.PhotoImage(file="Image_Gallery/Answer3.png") #Converts the Answer1_button image into tkinter compatible format
    btn3 = tk.Button(new_window, image=Answer3_button, cursor="hand2", text= current_question["Options"][2] #Creates a button with the Answer3_button image that turns the mouse into the pointer when it is hovered over and displays the text for the current question
    , compound="center", font=("Arial", 14, "bold"), relief="flat",  fg="white", command=lambda: select_answer(btn3)) #The button text is set to display directly on top of the button, the font is changed, the button becomes flat, the text becomes white, and the answer is checked using the check_answer def function
    btn3.image = Answer3_button
    btn3.place(relx=0.38, rely=0.92, anchor="center")

    Answer4_button = tk.PhotoImage(file="Image_Gallery/Answer4.png") #Converts the Answer1_button image into tkinter compatible format
    btn4 = tk.Button(new_window, image=Answer4_button, cursor="hand2", text= current_question["Options"][3] #Creates a button with the Answer2_button image that turns the mouse into the pointer when it is hovered over and displays the text for the current question
    , compound="center", font=("Arial", 14, "bold"), relief="flat",  fg="white", command=lambda: select_answer(btn4)) #The button text is set to display directly on top of the button, the font is changed, the button becomes flat, the text becomes white, and the answer is checked using the check_answer def function
    btn4.image = Answer4_button
    btn4.place(relx=0.625, rely=0.92, anchor="center")

    selected_button = None
    selected_answer = None

    def select_answer(button):
        nonlocal selected_button, selected_answer

        if selected_button:
            selected_button.config(bg="white")

        selected_button = button
        btn1.config(bg="white")
        btn2.config(bg="white")
        btn3.config(bg="white")
        btn4.config(bg="white")
        selected_button.config(bg="black")
        selected_answer = button["text"]

    def hover_on(event):
        event.widget.config(bg="#A9A9A9")

    def hover_off(event):
        event.widget.config(relief="flat")

    btn1.bind("<Enter>", hover_on)
    btn1.bind("<Leave>", hover_off)

    btn2.bind("<Enter>", hover_on)
    btn2.bind("<Leave>", hover_off)

    btn3.bind("<Enter>", hover_on)
    btn3.bind("<Leave>", hover_off)

    btn4.bind("<Enter>", hover_on)
    btn4.bind("<Leave>", hover_off)

    def exit_to_home():
        new_window.destroy()
        name_entry.delete(0, tk.END)
        outcome_label.config(text="Please enter your name", fg="black")
        root.deiconify()

    Exit_button = tk.PhotoImage(file="Image_Gallery/Exit_button.png")
    btn = tk.Button(new_window, image=Exit_button, cursor="hand2", command=exit_to_home)
    btn.image = Exit_button
    btn.place(relx=0.05, rely=0.09, anchor="center")

    Next_button = tk.PhotoImage(file="Image_Gallery/Next_button.png")
    btn = tk.Button(new_window, image=Next_button, cursor="hand2", command=next_question)
    btn.image = Next_button
    btn.place(relx=0.80, rely=0.845, anchor="center")

    def help_popup():
        messagebox.showinfo(
    "Quiz help",
"Welcome to the Geography Quiz!\n\n" 
        "- Select the one answer you believe to be correct for each question\n\n" 
        "- Press the next button to submit your answer and move on to the next page\n\n"
        "- You cannot change your answer after it has been submited\n\n"
        "- There are 10 questions in total\n\n"
        "- You need to get at least 7 out of 10 questions correct to pass the quiz\n")

    Help_button = tk.PhotoImage(file="Image_Gallery/Help_button.png")
    btn = tk.Button(new_window, image=Help_button, cursor="hand2", command= help_popup)
    btn.image = Help_button
    btn.place(relx=0.955, rely=0.09, anchor="center")


    root.withdraw()

root.mainloop()