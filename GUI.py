import tkinter as tk
from tkinter import ttk
import IpGenerator

# progress_bar = None


def get_data():
    window = tk.Tk()
    window.title("Network Scanner")
    ip = tk.StringVar(value='10.182.16.59')
    subnet_mask = tk.StringVar(value='255.255.255.0')

    # ip box
    ip_label = tk.Label(window, text="IP Adress: ")  # mozna dodac parametr font
    ip_label.grid(row=0, column=0)  # siatka
    ip_textbox = ttk.Entry(window, textvariable=ip)  # 1 arg, to okno w ktorym ma sie znalezc
    ip_textbox.grid(row=1, column=0)

    # mac box
    mac_label = tk.Label(window, text="Subnet Mask: ")
    mac_label.grid(row=2, column=0)
    mac_textbox = ttk.Entry(window, textvariable=subnet_mask)
    mac_textbox.grid(row=3, column=0)

    for widget in window.winfo_children():
        widget.grid_configure(padx=20, pady=5)  # padding x i padding y (wypelnienie)

    def on_click():
        ip_str = ip.get()
        subnet_mask_str = subnet_mask.get()
        window.destroy()
        # progress_window(subnet_mask_str)
        my_computer = IpGenerator.IpGenerator(subnet_mask_str, ip_str)
        my_computer.scan()
        main_window()

    submit_button = tk.Button(window, text="Scan",
                              command=on_click)
    submit_button.grid(row=4, column=0, padx=5, pady=10)

    window.mainloop()  # okno jest otwarte dopoki go nie zamkniemy


# 192.168.1.78
# 255.255.255.0

# def progress_window(subnet_mask):
#     window = tk.Tk()
#     window.title("Network Scanner")
#     maxi = IpGenerator.ip_to_int('255.255.255.255') + 1 - IpGenerator.ip_to_int(subnet_mask)
#     global progress_bar
#     progress_bar = ttk.Progressbar(window, maximum=maxi)
#     progress_bar.grid(column=0, row=0)


def main_window():
    window = tk.Tk()
    window.title("Network Scanner")

    columns = ["Id", "IP Adress", "Mac Adress", "Mac Producer"]

    table = ttk.Treeview(window, columns=columns, show='headings')

    table.column("Id", anchor='center')
    table.column("IP Adress", anchor='center')
    table.column("Mac Adress", anchor='center')
    table.column("Mac Producer", anchor='center')

    table.heading("Id", text="Id")
    table.heading("IP Adress", text="Ip Adress")
    table.heading("Mac Adress", text="Mac Adress")
    table.heading("Mac Producer", text="Mac Producer")

    i = 0
    for device in IpGenerator.devices:
        i += 1
        table.insert(parent='', index='end', values=(i, device.ip, device.mac, device.producer))

    table.pack(padx=20, pady=20)

    window.mainloop()
