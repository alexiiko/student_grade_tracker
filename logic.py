import tkinter as tk


class Logic(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.subject_list = ["English", "Math"]
        self.subjects_avgs = []

        self.create_subject_avgs(master)

        self.window = master

        self.create_column_button = tk.Button(
            master=master, text="Add new grade", command=self.create_new_grade_column
        ).grid(row=0, column=0, columnspan=2)

        self.grade_counter = 0

    """
    potential fixes: make two frames for the first row (with the button and the grade labels) so that the grades and the lables
                     are seperated from each other 
                     make the calc_avg function run constantly (so that it always checks in real time)
    """

    def calc_avg(self):
        self.subjects_avgs.clear()
        for _ in self.subject_list:
            self.subjects_avgs.append(0)

        grid_row_size = self.window.grid_size()[1]
        grid_col_size = self.window.grid_size()[0]
        for row_counter in range(1, grid_row_size + 1):
            column_sum = 0
            entry_number = 0
            for column in range(1, grid_col_size + 1):
                widgets = self.window.grid_slaves(column=column, row=row_counter)
                for widget in widgets:
                    if (
                        isinstance(widget, tk.Entry)
                        and widget.get().isdigit()
                        and int(widget.get()) > 1
                        and int(widget.get()) < 7
                    ):
                        print("Got entry name grid")
                        column_sum += int(widget.get())
                        entry_number += 1

            if not entry_number == 0:
                avg = column_sum / entry_number
                self.subjects_avgs[row_counter - 1] = round(avg, 2)
                print(self.subjects_avgs)

            print(len(self.subjects_avgs))

        for idx, avg in enumerate(self.subjects_avgs):
            row_idx = idx + 1
            widgets = self.window.grid_slaves(column=1, row=row_idx)
            for widget in widgets:
                widget.config(text=str(avg))

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

    def create_subject_avgs(self, window):
        for label in range(len(self.subject_list)):
            tk.Label(master=window, text=self.subject_list[label]).grid(
                column=0, row=label + 1
            )
            tk.Label(master=window).grid(column=1, row=label + 1)
