import tkinter as tk
from tkinter import messagebox


tkw = tk.Tk()
tkw.title('Login Page')
tkw.geometry('500x600')
tkw.configure(bg='#595959')


#Add 4 more student ID from the data sample
def create_predict_window():
    id = 'S001'
    gender = 'Male'
    sh = '15.5'
    ar = '95.0'
    pg = '3.7'
    ps = '8'

    if studentID_entry.get()==id and gender_entry.get()==gender and studyHour_entry.get()==sh and attendanceRate_entry.get()==ar and previousGrade_entry.get()==pg and previousGrade_entry.get()==ps:
        messagebox.showinfo("Your Predicted Grade is")
    else:
        messagebox.showerror("Unable to predict grade", "Please check your input information again")


frame = tk.Frame(bg='#595959')

#Create widgets = First Window
login_label = tk.Label(frame, text="Performance Prediction System", bg='#595959', fg='#FFFFFF', font=('arial', 30, 'bold'))
studentID_label = tk.Label(frame, text="Student ID: ", bg='#595959', fg='#FFFFFF', font=('arial', 16))
studentID_entry = tk.Entry(frame, font=('arial', 16))
gender_label = tk.Label(frame, text="Gender: ", bg='#595959', fg='#FFFFFF', font=('arial', 16))
gender_entry = tk.Entry(frame, font=('arial', 16))
studyHour_label = tk.Label(frame, text="Study Hour: ", bg='#595959', fg='#FFFFFF', font=('arial', 16))
studyHour_entry = tk.Entry(frame, font=('arial', 16))
attendanceRate_label = tk.Label(frame, text="Attendance Rate: ", bg='#595959', fg='#FFFFFF', font=('arial', 16))
attendanceRate_entry = tk.Entry(frame, font=('arial', 16))
participationScore_label = tk.Label(frame, text="Participation Score: ", bg='#595959', fg='#FFFFFF', font=('arial', 16))
participationScore_entry = tk.Entry(frame, font=('arial', 16))
previousGrade_label = tk.Label(frame, text="Previous Grade: ", bg='#595959', fg='#FFFFFF', font=('arial', 16))
previousGrade_entry = tk.Entry(frame, font=('arial', 16))
predict_button = tk.Button(frame, text='Predict', bg='#595959', fg='#000000', font=('arial', 16), command=create_predict_window)


#Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
studentID_label.grid(row=1, column=0)
studentID_entry.grid(row=1, column=1, pady=10)
gender_label.grid(row=2, column=0)
gender_entry.grid(row=2, column=1, pady=10)
studyHour_label.grid(row=3, column=0)
studyHour_entry.grid(row=3, column=1, pady=10)
attendanceRate_label.grid(row=4, column=0)
attendanceRate_entry.grid(row=4, column=1, pady=10)
participationScore_label.grid(row=5, column=0)
participationScore_entry.grid(row=5, column=1, pady=10)
previousGrade_label.grid(row=6, column=0)
previousGrade_entry.grid(row=6, column=1, pady=10)
predict_button.grid(row=7, column=0, columnspan=2, pady=30)

frame.pack()
tkw.mainloop()
