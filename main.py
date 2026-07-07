import tkinter as tk #Tells python to load the tkinter module
from PIL import Image, ImageTk #Makes it so that I can use Image and ImageTK modules from the pillow library, this allows images to be processed
from tkinter import messagebox #Makes it so that I can use the messagebox in tkinter for my code

root = tk.Tk() #Creates the tkinter window
root.title("Home page") #Gives the title of my first window

question_index = 0 #Sets the number for the question to zero
score=0 #Sets the users score to zero
no_answer = False #Sets the no_answer message box to false
help_message = False #Sets the help_message message box to false
root.geometry("1145x645") #Changes the size of the home page window
root.resizable(False, False) #Makes it so that the maximise button is disabled so that the home page cannot be resized

def home_page(): #Creates a def function for all elements in the home page
    image = Image.open("Image_Gallery/Homepage.png") #Opens image from image gallery folder
    photo = ImageTk.PhotoImage(image) #Converts an image to a tkinter compatible format
    label = tk.Label(root, image=photo) #Creates a widget that displays an image instead of text
    label.image = photo #Attaches the label to the image so that is not deleted by pythons memory cleanup
    label.pack()  #Makes the image for the homepage appear

    global name_entry, outcome_label, name_checker #Makes the name_entry and outcome_label variables global so they can be used anywhere in the code
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
            play_btn.config(command=lambda: None) #Disables the play button after it has been pressed
            root.after(1750, open_questions_page) #Lets the user move on to the next page using the open_questions_page command and makes it happen after a short period of time

    global play_btn #Makes the play_btn variables global so it can be used anywhere in the code
    play_button = tk.PhotoImage(file="Image_Gallery/Play_button.png") #Coverts the image of the play button into a tkinter compatible format
    play_btn = tk.Button(root, image=play_button,  cursor="hand2", command= name_checker) #Creates a button with the play button image that turns the mouse into the pointer when it is hovered over and goes through the name_checker def function when clicked
    play_btn.image = play_button #Makes the play button have the attributes of the button
    play_btn.place(relx=0.5, rely=0.77, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def on_enter(enter): #Creates a variable for what happens when the mouse is on the button
        play_btn.config(bg = "#000000") #Makes the background of the button black

    def on_leave(leave): #Creates a variable for what happens when the mouse is off the button
        play_btn.config(bg = "#d8d3c9") #Makes the background of the button grayish orange

    play_btn.bind("<Enter>", on_enter) #Makes it so that when the mouse is hovering over the button it changes the outline of the button
    play_btn.bind("<Leave>", on_leave) #Makes it so that when the mouse is not hovering over the button it goes back to normal

home_page() #Runs the code in the home_page def function

Questions_answers = [ #Creates a dictionary which stores the questions, options, answers, and backgrounds for each question of my quiz
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

def open_questions_page(): #Creates a def function for the questions page
    global new_window, question_index #Makes new_window and question_index variables global so it can be used anywhere in the code
    root.withdraw() #Hides the home page window
    new_window = tk.Toplevel(root) #Creates a secondary window
    new_window.title("Questions page") #Creates the title of the second window
    new_window.geometry("1145x645")  #Changes the size of the questions page window
    new_window.resizable(False, False) #Makes it so that the maximise button is disabled so that the home page cannot be resized
    next_image = Image.open("Image_Gallery/Q1.png") #Opens the image from image gallery folder
    next_photo = ImageTk.PhotoImage(next_image) #Converts an image to a tkinter compatible format
    image_label = tk.Label(new_window, image=next_photo) #Creates a widget that displays an image instead of text
    image_label.image = next_photo #Attaches the label to the image so that is not deleted by pythons memory cleanup
    image_label.pack() #Makes the image for the questions page appear

    #Creates a label with a specific text, font, font colour, background, and makes it so that it appears in the new window. It displays what question the user is currently on
    question_label = tk.Label(new_window, text=f"{question_index + 1}/10", font=("Arial", 60), bg="black", fg="white")
    question_label.place(relx=0.10, rely=0.9, anchor="center") #Aligns the label to the centre of the screen and moves it to a suitable position

    # Creates a label with a specific font and background, and makes it so that it appears in the new window. It will display whether the answer the user submitted is correct or not
    result_label = tk.Label(new_window, font=("Arial", 14), bg="white")
    result_label.place(relx=0.8, rely=0.63, anchor="center") #Aligns the label to the centre of the screen and moves it to a suitable position
    result_label.place_forget() #Hides the label so that it is not seen

    def question_number(): #Creates a def function for the question number
        question_label.config(text=f"{question_index + 1}/10") #Updates the question number each time the def function is called

    current_question = Questions_answers[question_index] #A variable current_question is created which contains the line of the dictionary that corresponds to the number from question_index

    def check_answer(selected_answer): #Creates a def function for the answer that the user selects to be checked whether it is right or wrong the selected_answer variable is created and holds the choice the user made
        current_question = Questions_answers[question_index] #A variable current_question is created which contains the line of the dictionary that corresponds to the number from question_index
        if selected_answer == current_question["Answer"]: #If the answer the user has selected is the same as the answer for the current question from the dictionary
            result_label.config(text="Your answer is correct!", fg="green", bg="white") #Updates the result labels text, font colour, and background if the answer submitted is correct
            global score #Makes the score variable global so it can be used anywhere in the code
            score+=1 #Adds 1 to the users score if they get the answer correct
        else: #If the answer the user has selected is not the same as the answer for the current question from the dictionary
            result_label.config(text="Your answer is wrong!", fg="red", bg="white") #Updates the result labels text, font colour, and background if the answer submitted is wrong

    def next_question(): #Creates a def function for the user to move on to the next question
        global question_index, no_answer, help_message #Makes the question_index, no_answer, and help_message variables global so it can be used anywhere in the code

        def load_question(): #Creates a def function for the question to be loaded
            global question_index # Makes the question_index, no_answer, and help_message variables global so it can be used anywhere in the code
            nonlocal selected_answer, selected_button #Makes the selected_answer and selected_button variables nonlocal so it can be used anywhere within the open_questions_page def function
            question_index +=1 #Adds 1 to the question_index so that it corresponds to the next question

            if question_index >= len(Questions_answers): #If the question index number is higher than the number of questions in the dictionary
                new_window.destroy() #The questions page window is destroyed
                if score >= 7: #If the score is greater or equal to 7
                    pass_window() #Runs the code in the pass_window def function
                    return #Makes it so that only the code from the pass_window runs now
                elif score <7: #If the score is less than 7
                    fail_window() #Runs the code in the fail_window def function
                    return #Makes it so that only the code from the fail_window runs now

            result_label.place_forget() #Hides the result label so the user cannot see it
            question_number() #Runs the question number def function

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

                selected_answer = None #Sets the selected_answer variable to none when there is no answer selected
                selected_button = None #Sets the selected_button variable to none when there is no answer selected

                btn1.config(bg="white") #Changes the btn1 back to how it was without a hover effect for each question
                btn2.config(bg="white") #Changes the btn2 back to how it was without a hover effect for each question
                btn3.config(bg="white") #Changes the btn3 back to how it was without a hover effect for each question
                btn4.config(bg="white") #Changes the btn4 back to how it was without a hover effect for each question

        new_window.after(700, load_question) #Makes it so that it takes 700 milliseconds for the next question to be loaded, this means the user has time to see the result label

        if selected_answer is None: #If the user has not selected any answer
            if no_answer: #If no_answer message is already on screen
                return #Returns back

            no_answer = True #Makes the no_answer variable true so that the message box can be opened

            messagebox.showinfo("Error", "Please select an answer!", parent = new_window) #Creates a message box with specific title, message, and makes it so that it appears over the new_window
            no_answer = False #Makes the no_answer variable false so that multiple message boxes can't be opened
            return #Repeats the if statement

        check_answer(selected_answer) #Runs the def function def check_answer(selected_answer)
        result_label.place(relx=0.8, rely=0.63, anchor="center") #Aligns the label to the centre of the screen and moves it to a suitable position

    answer1_button = tk.PhotoImage(file="Image_Gallery/Answer1.png") #Converts the Answer1_button image into tkinter compatible format
    btn1 = tk.Button(new_window, image=answer1_button, cursor="hand2", text= current_question["Options"][0]  #Creates a button with the Answer1_button image that turns the mouse into the pointer when it is hovered over and displays the text for the current question
    , compound="center", font=("Arial", 15, "bold"), relief="flat", fg="white", command=lambda: select_answer(btn1)) #The button text is set to display directly on top of the button, the font is changed, the button becomes flat, the text becomes white, and the answer is checked using the check_answer def function
    btn1.image = answer1_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
    btn1.place(relx=0.38, rely=0.75, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    answer2_button = tk.PhotoImage(file="Image_Gallery/Answer2.png") #Converts the Answer1_button image into tkinter compatible format
    btn2 = tk.Button(new_window, image=answer2_button, cursor="hand2", text= current_question["Options"][1] #Creates a button with the Answer2_button image that turns the mouse into the pointer when it is hovered over and displays the text for the current question
    , compound="center", font=("Arial", 15, "bold"), relief="flat", fg="white", command=lambda: select_answer(btn2)) #The button text is set to display directly on top of the button, the font is changed, the button becomes flat, the text becomes white, and the answer is checked using the check_answer def function
    btn2.image = answer2_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
    btn2.place(relx=0.625, rely=0.75, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    answer3_button = tk.PhotoImage(file="Image_Gallery/Answer3.png") #Converts the Answer1_button image into tkinter compatible format
    btn3 = tk.Button(new_window, image=answer3_button, cursor="hand2", text= current_question["Options"][2] #Creates a button with the Answer3_button image that turns the mouse into the pointer when it is hovered over and displays the text for the current question
    , compound="center", font=("Arial", 15, "bold"), relief="flat",  fg="white", command=lambda: select_answer(btn3)) #The button text is set to display directly on top of the button, the font is changed, the button becomes flat, the text becomes white, and the answer is checked using the check_answer def function
    btn3.image = answer3_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
    btn3.place(relx=0.38, rely=0.92, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    answer4_button = tk.PhotoImage(file="Image_Gallery/Answer4.png") #Converts the Answer1_button image into tkinter compatible format
    btn4 = tk.Button(new_window, image=answer4_button, cursor="hand2", text= current_question["Options"][3] #Creates a button with the Answer2_button image that turns the mouse into the pointer when it is hovered over and displays the text for the current question
    , compound="center", font=("Arial", 15, "bold"), relief="flat",  fg="white", command=lambda: select_answer(btn4)) #The button text is set to display directly on top of the button, the font is changed, the button becomes flat, the text becomes white, and the answer is checked using the check_answer def function
    btn4.image = answer4_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
    btn4.place(relx=0.625, rely=0.92, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    selected_button = None #Sets the selected_answer variable to none when there is no answer selected
    selected_answer = None #Sets the selected_button variable to none when there is no answer selected

    def select_answer(button): #Creates a def function for the answer button to be selected
        nonlocal selected_button, selected_answer #Makes the selected_answer and selected_button variables nonlocal so it can be used anywhere within the open_questions_page def function

        btn1.config(bg="white") #Changes the btn1 back to how it was without a hover effect when it is not hovered over
        btn2.config(bg="white") #Changes the btn2 back to how it was without a hover effect when it is not hovered over
        btn3.config(bg="white") #Changes the btn3 back to how it was without a hover effect when it is not hovered over
        btn4.config(bg="white") #Changes the btn4 back to how it was without a hover effect when it is not hovered over

        selected_button = button #Makes the selected_button equal button
        selected_button.config(bg="black") #Changes the selected button background to black

        selected_answer = button["text"] #Makes the selected answer equal to the text on the selected button

    def hover_on(event): #Creates a def function for the buttons to be hovered over
        if event.widget != selected_button: #If the widget the user just hovered over is the selected button
            event.widget.config(bg="#A9A9A9") #Change the background of the button to grey

    def hover_off(event): #Creates a def function for when the buttons are not hovered over
        if event.widget != selected_button: #If the widget the user just hovered over is the selected button
            event.widget.config(bg="white") #Change the background of the button to white

    btn1.bind("<Enter>", hover_on) #When the mouse is hovered over btn1 the hover_on def function is called
    btn1.bind("<Leave>", hover_off) #When the mouse is hovered off btn1 the hover_off def function is called

    btn2.bind("<Enter>", hover_on) #When the mouse is hovered over btn2 the hover_on def function is called
    btn2.bind("<Leave>", hover_off) #When the mouse is hovered off btn2 the hover_off def function is called

    btn3.bind("<Enter>", hover_on) #When the mouse is hovered over btn3 the hover_on def function is called
    btn3.bind("<Leave>", hover_off) #When the mouse is hovered off btn3 the hover_off def function is called

    btn4.bind("<Enter>", hover_on) #When the mouse is hovered over btn4 the hover_on def function is called
    btn4.bind("<Leave>", hover_off) #When the mouse is hovered off btn4 the hover_off def function is called

    def questions_page_to_home(): #Creates a def function for the command for the exit button
        global question_index, score #Makes the question_index and score variables global so it can be used anywhere in the code
        new_window.destroy() #The questions page window is destroyed
        name_entry.delete(0, tk.END) #Clears the name_entry box
        play_btn.config(command=name_checker) #Makes the play btn call the command name_checker when clicked
        outcome_label.config(text="Please enter your name", fg="black")  #Changes the outcome label text to what it was before
        question_index = 0 #Sets the number for the question to zero
        score = 0 #Sets the users score to zero
        root.deiconify() #The home page window is shown again

    exit_button = tk.PhotoImage(file="Image_Gallery/Exit_button.png") #Converts the exit_button image into tkinter compatible format
    # Creates a button with the exit_button image that turns the mouse into the pointer when it is hovered over and calls the command questions_page_to_home
    exit_btn = tk.Button(new_window, image=exit_button, cursor="hand2", command=questions_page_to_home)
    exit_btn.image = exit_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
    exit_btn.place(relx=0.05, rely=0.09, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    next_button = tk.PhotoImage(file="Image_Gallery/Next_button.png") #Converts the next_button image into tkinter compatible format
    # Creates a button with the next_button image that turns the mouse into the pointer when it is hovered over and calls the command next_question
    next_btn = tk.Button(new_window, image=next_button, cursor="hand2", command= next_question)
    next_btn.image = next_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
    next_btn.place(relx=0.80, rely=0.845, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def help_popup(): #Creates a def function for the help_popup message box
        global help_message #Makes the help_message variable global so it can be used anywhere in the code
        if help_message: #If help_message message is already on screen
            return #Returns back

        help_message = True #Makes the help_message variable true so that the message box can be opened

        #Creates a message box with specific title, message, and makes it so that it appears over the new_window
        messagebox.showinfo(
    "Quiz help",
"Welcome to the Geography Quiz!\n\n" 
        "- Select the one answer you believe to be correct for each question\n\n" 
        "- Press the next button to submit your answer and move on to the next question\n\n"
        "- You cannot change your answer after it has been submitted\n\n"
        "- There are 10 questions in total\n\n"
        "- You need to get at least 7 out of 10 questions correct to pass the quiz\n\n"
        "- You can exit to the home page by pressing the x in the top left corner ", parent = new_window)

        help_message = False #Makes the help_message variable false so that multiple message boxes can't be opened
        return #Repeats the if statement

    help_button = tk.PhotoImage(file="Image_Gallery/Help_button.png") #Converts the next_button image into tkinter compatible format
    #Creates a button with the help_button image that turns the mouse into the pointer when it is hovered over and calls the command help_popup
    help_btn = tk.Button(new_window, image=help_button, cursor="hand2", command= help_popup)
    help_btn.image = help_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
    help_btn.place(relx=0.955, rely=0.09, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

def pass_window(): #Creates the def function pass_window
    global score #Makes the score variable global so it can be used anywhere in the code
    pass_window = tk.Toplevel(root)  #Creates a secondary window
    pass_window.title("Pass page")  #Creates the title of the second window
    pass_window.geometry("1145x645")  #Changes the size of the home page window
    pass_window.resizable(False, False) #Makes it so that the maximise button is disabled so that the home page cannot be resized
    image = Image.open("Image_Gallery/Pass_page.png")  #Opens image from image gallery folder
    pass_photo = ImageTk.PhotoImage(image)  #Converts an image to a tkinter compatible format
    label = tk.Label(pass_window, image=pass_photo)  #Creates a widget that displays an image instead of text
    label.image = pass_photo  #Attaches the label to the image so that is not deleted by pythons memory cleanup
    label.pack()  #Makes the image for the pass_window to appear

    pass_message = tk.Label(pass_window, text=f"Your score is {score}/10", font = ("Arial",50), fg="green", bg="black") #Creates a label with a specific message, font, font size, font colour and background
    pass_message.place(relx=0.5, rely=0.412, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def play_again(): #Creates the def function for the user to play again
        play_again_button = tk.PhotoImage(file="Image_Gallery/Play_again_button.png") #Converts the play_again_button image into tkinter compatible format
        #Creates a button with the play_again_button image that turns the mouse into the pointer when it is hovered over and calls the command pass_window_to_home
        play_again_btn = tk.Button(pass_window, image=play_again_button, cursor="hand2", command=pass_window_to_home)
        play_again_btn.image = play_again_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
        play_again_btn.place(relx=0.59, rely=0.75, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def pass_window_to_home(): #Creates a def function for the command for the play again button
        global question_index, score  # Makes the question_index and score variables global so it can be used anywhere in the code
        pass_window.destroy() #The pass window is destroyed
        name_entry.delete(0, tk.END) #Clears the name_entry box
        play_btn.config(command=name_checker) #Makes the play btn call the command name_checker when clicked
        outcome_label.config(text="Please enter your name", fg="black") #Changes the outcome label text to what it was before
        question_index = 0 #Sets the number for the question to zero
        score = 0 #Sets the users score to zero
        root.deiconify() #The home page window is shown again

    play_again() #Runs the play_again def function

    def no_play_again(): #Creates the def function for the user to not play again
        no_play_again_button = tk.PhotoImage(file="Image_Gallery/No_play_again_button.png") #Converts the no_play_again_button image into tkinter compatible format
        #Creates a button with the no_play_again_button image that turns the mouse into the pointer when it is hovered over and calls the command pass_window_exit
        no_play_again_btn = tk.Button(pass_window, image=no_play_again_button, cursor="hand2", command=pass_window_exit)
        no_play_again_btn.image = no_play_again_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
        no_play_again_btn.place(relx=0.39, rely=0.75, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def pass_window_exit(): #Creates a def function for the command for the no play again button
        root.destroy() #Destroys all the windows which ends the quiz

    no_play_again() #Runs the no_play_again def function

def fail_window(): #Creates the def function fail_window
    global score #Makes the score variable global so it can be used anywhere in the code
    fail_window = tk.Toplevel(root)  #Creates a secondary window
    fail_window.title("Fail page")  #Creates the title of the second window
    fail_window.geometry("1145x645")  #Changes the size of the home page window
    fail_window.resizable(False, False) #Makes it so that the maximise button is disabled so that the home page cannot be resized
    image = Image.open("Image_Gallery/Fail_page.png")  #Opens image from image gallery folder
    fail_photo = ImageTk.PhotoImage(image)  #Converts an image to a tkinter compatible format
    label = tk.Label(fail_window, image=fail_photo)  #Creates a widget that displays an image instead of text
    label.image = fail_photo  #Attaches the label to the image so that is not deleted by pythons memory cleanup
    label.pack()  #Makes the image for the fail_window appear

    fail_message = tk.Label(fail_window, text=f"Your score is {score}/10", font=("Arial", 50), fg="red", bg="black") #Creates a label with a specific message, font, font size, font colour and background
    fail_message.place(relx=0.5, rely=0.412, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def play_again(): #Creates the def function for the user to play again
        play_again_button = tk.PhotoImage(file="Image_Gallery/Play_again_button.png")  #Converts the play_again_button image into tkinter compatible format
        # Creates a button with the play_again_button image that turns the mouse into the pointer when it is hovered over and calls the command fail_window_to_home
        play_again_btn = tk.Button(fail_window, image=play_again_button, cursor="hand2", command=fail_window_to_home)
        play_again_btn.image = play_again_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
        play_again_btn.place(relx=0.59, rely=0.75, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def fail_window_to_home(): #Creates a def function for the command for the play again button
        global question_index, score # Makes the question_index and score variables global so it can be used anywhere in the code
        fail_window.destroy() #The fail window is destroyed
        name_entry.delete(0, tk.END) #Clears the name_entry box
        play_btn.config(command=name_checker) #Makes the play btn call the command name_checker when clicked
        outcome_label.config(text="Please enter your name", fg="black") #Changes the outcome label text to what it was before
        question_index = 0  #Sets the number for the question to zero
        score = 0  #Sets the users score to zero
        root.deiconify()  #The home page window is shown again

    play_again() #Runs the play_again def function

    def no_play_again(): #Creates the def function for the user to not play again
        no_play_again_button = tk.PhotoImage(file="Image_Gallery/No_play_again_button.png") #Converts the no_play_again_button image into tkinter compatible format
        #Creates a button with the no_play_again_button image that turns the mouse into the pointer when it is hovered over and calls the command fail_window_exit
        no_play_again_btn = tk.Button(fail_window, image=no_play_again_button, cursor="hand2", command=fail_window_exit)
        no_play_again_btn.image = no_play_again_button #Attaches the button to the image so that is not deleted by pythons memory cleanup
        no_play_again_btn.place(relx=0.39, rely=0.75, anchor="center") #Aligns the button to the centre of the screen and moves it to a suitable position

    def fail_window_exit(): #Creates a def function for the command for the no play again button
        root.destroy() #Destroys all the windows which ends the quiz

    no_play_again() #Runs the no_play_again def function

    root.withdraw() #Hides all the windows to end the quiz

root.mainloop() #Run the loop to keep the window open