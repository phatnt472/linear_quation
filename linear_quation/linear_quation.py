from tkinter import *
from time import *

def calc_action():
    try:
        a = float(string_a.get())
        b = float(string_b.get())
        if a == 0 and b == 0:
            string_kq.set("Vô số nghiệm")
        elif b != 0 and a == 0:
            string_kq.set("Vô nghiệm")
        else:
            kq = 0 if b == 0 and a != 0 else -b/a
            string_kq.set(f"{kq}")

    except:
        string_kq.set(f"Nhập sai")


def delete_action():
    string_a.set("")
    string_b.set("")
    string_kq.set("")


if __name__ == "__main__":
    root = Tk()
    string_a = StringVar()
    string_b = StringVar()
    string_kq = StringVar()

    root.title("PTB1")
    root.resizable(height=False, width=False)
    root.minsize(height=250, width=300)

    Label(root, text="Phương Trình Bậc 1", fg="red", justify=CENTER, font="Tahoma", height=2).grid(row=0, columnspan=3)
    Label(root, text="Hệ số a:", width=10, height=3, fg="blue").grid(row=1, columnspan=2)
    Label(root, text="Hệ số b:", width=10, height=3, fg="blue").grid(row=2, columnspan=2)
    Label(root, text="Kết quả:", width=10, height=3, fg="blue").grid(row=4, columnspan=2)

    Entry(root, width=20, justify=CENTER, textvariable=string_a).grid(row=1, column=2)
    Entry(root, width=20, justify=CENTER, textvariable=string_b).grid(row=2, column=2)
    Entry(root, width=20, justify=CENTER, textvariable=string_kq).grid(row=4, column=2)

    frame_button = Frame()
    Button(frame_button, text="Giải", width=4, height=2, padx=10, command=calc_action).grid(row=3, column=0)
    Button(frame_button, text="Xoá", width=4, height=2, padx=10, command=delete_action).grid(row=3, column=1)
    Button(frame_button, text="Thoát", width=4, height=2, padx=10, command=root.quit).grid(row=3, column=2)
    frame_button.grid(row=3, columnspan=3)

    root.mainloop()
