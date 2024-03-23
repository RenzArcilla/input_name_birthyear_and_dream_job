from tkinter import *
# pseudocode

# ask user to input name
user_name = input("Please enter your name: ")

# ask user to input birth year
user_birth_year = input("Please enter your birth year: ")

# ask user to input dream job
user_dream_job = input("Please enter your dream job: ")

# merge name and birth year into 1 string
user_name_and_birth_year = f"{user_name} ({user_birth_year})"

# create window
window = Tk()
window.title("FUTURE CAREER")
window.geometry("900x300")

# display name, birthyear, and dreamjob in window
label = Label(window, text = ("\n" * 3) + user_name_and_birth_year + "\n" + "<< " + user_dream_job + " >>", font=("Times New Roman", 20, "bold"))
label.pack()
window.mainloop()