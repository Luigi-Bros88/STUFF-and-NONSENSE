import tkinter as tk

def remove_strings():
    text = entry_text.get()
    removals = entry_remove.get()

    # remove user-defined strings
    remove_list = [r.strip() for r in removals.split(",")]

    for r in remove_list:
        text = text.replace(r, "")

    # remove extra commas (,,, → , or delete completely if you prefer)
    while ",," in text:
        text = text.replace(",,", ",")

    # optional: remove leading/trailing commas that might remain
    text = text.strip(",")

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, text)
    output_box.config(state="disabled")


def clear_all():
    entry_text.delete(0, tk.END)
    entry_remove.delete(0, tk.END)

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.config(state="disabled")


# window
root = tk.Tk()
root.title("String Remover")
root.geometry("420x260")

tk.Label(root, text="Enter main string:").pack()
entry_text = tk.Entry(root, width=55)
entry_text.pack()

tk.Label(root, text="Strings to remove (comma-separated):").pack()
entry_remove = tk.Entry(root, width=55)
entry_remove.pack()

tk.Button(root, text="Remove Strings", command=remove_strings).pack(pady=5)
tk.Button(root, text="Clear", command=clear_all).pack(pady=5)

tk.Label(root, text="Output:").pack()

output_box = tk.Text(root, height=5, width=55)
output_box.pack()
output_box.config(state="disabled")

root.mainloop()