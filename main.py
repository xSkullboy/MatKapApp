import tkinter as tk
import tkinter.ttk as ttk

# Калькулятор долей по материнскому капиталу
class MatKapApp:
    def __init__(self, root):
        self.root = root
        root.geometry("400x450")
        self.root.title("Калькулятор долей по МСК")

        self.price_input = ttk.Spinbox(root, from_=0, to=50000000, increment=100000)
        self.sum_label1 = tk.Label(root, text="Сумма объекта недвижимости")

        self.capital_sum_input = ttk.Spinbox(root, from_=0, to=2000000, increment=50000)
        self.sum_label2 = tk.Label(root, text="Сумма использованного материнского капитала")

        self.persons_input = ttk.Spinbox(root, from_=0, to=20, increment=1)
        self.sum_label3 = tk.Label(root, text="Общее количество членов семьи")

        self.child_input = ttk.Spinbox(root, from_=0, to=20, increment=1)
        self.sum_label5 = tk.Label(root, text="Количество детей")

        self.parents_input = ttk.Spinbox(root, from_=0, to=2, increment=1)
        self.sum_label8 = tk.Label(root, text="Количество родителей")

        self.calc_button = tk.Button(root, text="Рассчитать долю", command=self.calculate)

        self.change_button = tk.Button(root, text="Уравнять доли родителей", command=self.change_share)

        self.sum_label4 = tk.Label(root, text="")
        self.sum_label6 = tk.Label(root, text="")
        self.sum_label7 = tk.Label(root, text="")
        self.sum_label9 = tk.Label(root, text="")

        self.sum_label1.pack(pady=2)
        self.price_input.pack(pady=2)
        self.sum_label2.pack(pady=2)
        self.capital_sum_input.pack(pady=2)
        self.sum_label3.pack(pady=2)
        self.persons_input.pack(pady=2)
        self.sum_label5.pack(pady=2)
        self.child_input.pack(pady=2)
        self.sum_label8.pack(pady=2)
        self.parents_input.pack(pady=2)
        self.calc_button.pack(pady=2)
        self.change_button.pack(pady=2)
        self.sum_label4.pack(pady=2)
        self.sum_label6.pack(pady=2)
        self.sum_label7.pack(pady=2)
        self.sum_label9.pack(pady=2)

    def calculate(self):
        price = float(self.price_input.get())
        capital = float(self.capital_sum_input.get())
        persons = int(self.persons_input.get())
        child = int(self.child_input.get())
        parents = int(self.parents_input.get())
        min_share = round(float((100 / price * capital) / persons))
        self.change_button.pack()
        self.sum_label4.configure(text=f"Минимальная доля в объекте недвижимости на одного ребенка: {min_share}/100")
        parents_share = (100 - (min_share*child))
        self.sum_label6.configure(text=f"Доля родителей в объекте недвижимости: {parents_share}/100")
        one_parent_share = round(parents_share/parents)
        scnd_parent_share = round(parents_share - one_parent_share)
        self.sum_label7.configure(text=f"Доля первого родителя: {one_parent_share}/100")
        self.sum_label9.configure(text=f"Доля второго родителя: {scnd_parent_share}/100")
        if parents < 2:
            self.sum_label6.configure(text=f"Доля родителя в объекте недвижимости: {parents_share}/100")
            self.sum_label7.configure(text=f" ")
            self.sum_label9.configure(text=f" ")
            self.change_button.pack_forget()

    def change_share(self):
        price = float(self.price_input.get())
        capital = float(self.capital_sum_input.get())
        persons = int(self.persons_input.get())
        child = int(self.child_input.get())
        parents = int(self.parents_input.get())
        min_share = round(float((100 / price * capital) / persons))
        self.sum_label4.configure(text=f"Минимальная доля в объекте недвижимости на одного ребенка: {min_share}/100")
        parents_share = (100 - (min_share * child))
        self.sum_label6.configure(text=f"Доля родителей в объекте недвижимости: {parents_share}/100")
        self.sum_label7.configure(text=f"Доля первого родителя: {parents_share}/200")
        self.sum_label9.configure(text=f"Доля второго родителя: {parents_share}/200")


root = tk.Tk()
app = MatKapApp(root)
root.mainloop()
