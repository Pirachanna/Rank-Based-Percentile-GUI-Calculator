from tkinter import *

# Function to calculate percentile
def getPercentile():
    try:
        students = int(total_participantField.get())
        rank = int(rankField.get())

        if students <= 0 or rank <= 0 or rank > students:
            raise ValueError

        result = round((students - rank) / students * 100, 3)
        percentileField.config(state="normal", fg="#ffffff")
        percentileField.delete(0, END)
        percentileField.insert(0, str(result) + " %")
        percentileField.config(state="readonly")
    except ValueError:
        percentileField.config(state="normal", fg="#ffffff")
        percentileField.delete(0, END)
        percentileField.insert(0, "Invalid Input")
        percentileField.config(state="readonly")

# Function to clear all fields
def Clear():
    rankField.delete(0, END)
    total_participantField.delete(0, END)
    percentileField.config(state="normal", fg="#ffffff")
    percentileField.delete(0, END)
    percentileField.config(state="readonly")

# GUI setup
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="#1f242d")  # ✅ your requested background
    gui.title("Rank Based Percentile Calculator")
    gui.geometry("600x300")

    # Title
    Label(gui, text="Rank Based Percentile Calculator", font=("Arial", 16, "bold"),
          bg="#1f242d", fg="#0ef").pack(pady=10)

    # Inputs
    form_frame = Frame(gui, bg="#1f242d")
    form_frame.pack(pady=10)

    Label(form_frame, text="Rank:", bg="#1f242d", fg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    rankField = Entry(form_frame, font=("Arial", 12), bg="#323946", fg="#ffffff", insertbackground="white")
    rankField.grid(row=0, column=1, padx=10, pady=5)

    Label(form_frame, text="Total Participants:", bg="#1f242d", fg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    total_participantField = Entry(form_frame, font=("Arial", 12), bg="#323946", fg="#ffffff", insertbackground="white")
    total_participantField.grid(row=1, column=1, padx=10, pady=5)

    # Buttons
    button_frame = Frame(gui, bg="#1f242d")
    button_frame.pack(pady=10)

    Button(button_frame, text="Find Percentile", bg="#0e639c", fg="white", font=("Arial", 12), command=getPercentile).grid(row=0, column=0, padx=20)
    Button(button_frame, text="Clear", bg="#d13438", fg="white", font=("Arial", 12), command=Clear).grid(row=0, column=1, padx=20)

    # Output
    output_frame = Frame(gui, bg="#1f242d")
    output_frame.pack(pady=10)

    Label(output_frame, text="Percentile:", bg="#1f242d", fg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=10)
    percentileField = Entry(
        output_frame,
        font=("Arial", 12),
        bg="#323946",              
        fg="#ffffff",              
        readonlybackground="#323946", 
        insertbackground="white",
        state="readonly",
        width=20
    )
    percentileField.grid(row=0, column=1, padx=10)

    gui.mainloop()
