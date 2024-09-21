import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the input and results
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=1, column=15, columnspan=4)

        # Buttonspyth
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, col):
        button = tk.Button(self, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result_var.get()
                result = str(eval(expression))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif char == 'C':
            self.result_var.set("")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
