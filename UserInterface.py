import tkinter as tk
from tkinter import messagebox

def start_ui(model):
    root = tk.Tk()
    root.title('Student Performance Prediction')
    root.geometry('500x600')
    root.configure(bg='#595959')

    def create_predict_window():
        try:
            student_id = studentID_entry.get().strip()
            gender = gender_entry.get().strip()
            sh = float(studyHour_entry.get())
            ar = float(attendanceRate_entry.get())
            pg = float(previousGrade_entry.get())
            ps = int(participationScore_entry.get())

            student_data = {
                'gender': gender,
                'study_hours': sh,
                'attendance_rate': ar,
                'previous_grade': pg,
                'participation_score': ps,
            }

            result = model.predict(student_data)
            messagebox.showinfo("Prediction", f"Student ID: {student_id}\nPredicted Final Grade: {result}")

        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    
    frame = tk.Frame(root, bg='#595959')
    frame_label = tk.Label(frame, text="Performance Prediction System", bg='#595959', fg='#FFFFFF', font=('arial', 20, 'bold'))
    frame_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Widgets
    labels = ["Student ID", "Gender", "Study Hour", "Attendance Rate", "Previous Grade", "Participation Score"]
    entries = []

    for i, label in enumerate(labels):
            lbl = tk.Label(frame, text=f"{label}:", bg='#595959', fg='#FFFFFF', font=('arial', 14))
            entry = tk.Entry(frame, font=('arial', 14))
            lbl.grid(row=i+1, column=0, sticky='e', pady=5)
            entry.grid(row=i+1, column=1, pady=5)
            entries.append(entry)

    studentID_entry, gender_entry, studyHour_entry, attendanceRate_entry, previousGrade_entry, participationScore_entry = entries

    tk.Button(frame, text='Predict', font=('arial', 14), command=create_predict_window).grid(row=7, column=0, columnspan=2, pady=20)
    
    frame.pack()
    root.mainloop()
