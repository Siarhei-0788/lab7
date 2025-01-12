import tkinter as tk
from tkinter import ttk

# Задание 1
fio_list = [
    {
        "FIO": "Макаров Дмитрий Андреевич",
        "Addresses": [
            {"town": "Гомель", "street": "Гагарина", "house": 88},
            {"town": "Гомель", "street": "Лермонтова", "house": 12},
        ],
    },
    {
        "FIO": "Коваленко Екатерина Игоревна",
        "Addresses": [
            {"town": "Витебск", "street": "Победы", "house": 42},
            {"town": "Витебск", "street": "Кирова", "house": 5},
        ],
    },
    {
        "FIO": "Сидорова Ольга Васильевна",
        "Addresses": [
            {"town": "Гродно", "street": "Советская", "house": 76},
            {"town": "Гродно", "street": "Кирова", "house": 32},
        ],
    },
]


# Задание 2
class UserAddressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Адреса пользователей")

        # Создание элементов интерфейса
        self.user_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
        self.address_treeview = ttk.Treeview(
            root, columns=("town", "street", "house"), show="headings"
        )
        self.init_button = tk.Button(
            root, text="Инициализировать", command=self.initialize_data
        )
        self.reset_button = tk.Button(root, text="Сбросить", command=self.reset_data)
        self.label = tk.Label(root, text="Выберите пользователя")
        self.menu_bar = tk.Menu(root)
        self.menu_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_file.add_command(
            label="Инициализировать", command=self.initialize_data
        )
        self.menu_file.add_command(label="Сбросить", command=self.reset_data)
        self.menu_bar.add_cascade(label="Опции", menu=self.menu_file)
        self.root.config(menu=self.menu_bar)
        self.check_button_var = tk.BooleanVar()
        self.check_button = tk.Checkbutton(
            root,
            text="Дополнительный функционал",
            variable=self.check_button_var,
            command=self.additional_functionality,
        )

        # Размещение элементов на форме
        self.label.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.W)
        self.user_listbox.grid(row=1, column=0, padx=5, pady=5)
        self.address_treeview.grid(row=1, column=1, padx=5, pady=5)
        self.init_button.grid(row=2, column=0, padx=5, pady=5)
        self.reset_button.grid(row=2, column=1, padx=5, pady=5)
        self.check_button.grid(row=3, column=0, columnspan=2, pady=5, sticky=tk.W)

        # Настройка Listbox

        self.user_listbox.bind("<<ListboxSelect>>", self.on_user_select)

        # Настройка Treeview
        self.address_treeview.heading("town", text="Город")
        self.address_treeview.heading("street", text="Улица")
        self.address_treeview.heading("house", text="Дом")

        self.address_treeview.column("town", width=100, anchor=tk.CENTER)
        self.address_treeview.column("street", width=150, anchor=tk.CENTER)
        self.address_treeview.column("house", width=75, anchor=tk.CENTER)

    def on_user_select(self, event):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_user = fio_list[selected_index]
            self.populate_address_table(selected_user["Addresses"])

    def populate_address_table(self, addresses):
        self.address_treeview.delete(*self.address_treeview.get_children())
        for address in addresses:
            self.address_treeview.insert(
                "",
                tk.END,
                values=(address["town"], address["street"], address["house"]),
            )

    def initialize_data(self):
        self.reset_data()
        for user in fio_list:
            self.user_listbox.insert(tk.END, user["FIO"])
        self.user_listbox.selection_clear(0, tk.END)
        self.user_listbox.selection_set(0)
        self.on_user_select(None)

    def reset_data(self):
        self.user_listbox.delete(0, "end")
        self.address_treeview.delete(*self.address_treeview.get_children())

    def additional_functionality(self):
        if self.check_button_var.get():
            print("Дополнительный функционал активирован!")
        else:
            print("Дополнительный функционал деактивирован.")


if __name__ == "__main__":
    root = tk.Tk()
    app = UserAddressApp(root)
    root.mainloop()

main()
discard_buffers(DocTestFinder(verbose=False, parser=DocTestParser, ))
SIG_DFL
