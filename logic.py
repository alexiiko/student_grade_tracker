import tkinter as tk


class Logic(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.subject_list = ["English"]
        self.subjects_avgs = [0, 0, 0, 0, 0]

        self.create_subject_subjects_avgs(master)

        self.window = master

        self.create_column_button = tk.Button(
            master=master, text="Add new grade", command=self.create_new_grade_column
        ).grid(row=0, column=0, columnspan=2)

        self.grade_counter = 0

    """
    current bugs: the function counts the first row too (where the button is and the labels for the grades)
                  the function does not add the column_sum and the entry_number to the variables (idk why)
                  
    potential fixes: make two frames for the first row (with the button and the grade labels) so that the grades and the lables
                     are seperated from each other 
                     make the calc_avg function run constantly (so that it always checks in real time)
    """

    def calc_avg(self):
        for row_counter in range(self.window.grid_size()[1]):
            column_sum = 0
            entry_number = 0
            for column in range(self.window.grid_size()[0]):
                widgets = self.window.grid_slaves(column=column, row=row_counter)
                for widget in widgets:
                    if isinstance(widget, tk.Entry):
                        if widget.get().isdigit():
                            if int(widget.get()) > 1 or int(widget.get()) < 7:
                                column_sum += int(widget.get())
                                entry_number += 1
            print(entry_number, column_sum)
            if not column_sum == 0 or not entry_number == 0:
                avg = column_sum / entry_number
                print(f"Endgrade in subject {self.subject_list[row_counter]} is: {avg}")

    def create_new_grade_column(self):
        self.grade_counter += 1
        tk.Label(master=self.window, text=f"Grade {self.grade_counter}").grid(
            column=self.grade_counter + 2, row=0
        )  # 2 because after the avgs the grades get shown

        for entry in range(len(self.subject_list)):
            grade_entry = tk.Entry(master=self.window)
            grade_entry.grid(
                column=self.grade_counter + 2, row=entry + 1
            )  # 2 because after the avgs the grades get shown

        self.calc_avg()

    def create_subject_subjects_avgs(self, window):
        for label in range(len(self.subject_list)):
            tk.Label(master=window, text=self.subject_list[label]).grid(
                column=0, row=label + 1
            )
            tk.Label(master=window, text=self.subjects_avgs[label]).grid(
                column=1, row=label + 1
            )
