import tkinter as tk
def zrob_cos():
    if label['text'] == 'Hi!':
        label.configure(text = 'Ha!')
    elif label['text'] == 'Ha!':
        label.configure(text = 'Ho!')
    elif label['text'] == 'Ho!':
        label.configure(text = 'Hi!')
    p = tk.Button(root, text=entry.get())
    p.pack()

root = tk.Tk()
label = tk.Label(root, text="Hi!")
label.pack()
przycisk = tk.Button(root, text="Kliknij!", command=zrob_cos)
przycisk.pack()
entry = tk.Entry(root)
entry.pack()
root.mainloop()