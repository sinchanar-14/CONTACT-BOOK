import tkinter as tk
from tkinter import messagebox, simpledialog

# Data structure to store contacts
contacts = {}

# Functions
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"Contact '{name}' added!")
    update_listbox()
    clear_fields()

def view_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No contact selected.")
        return
    name = listbox.get(selected[0])
    contact = contacts[name]
    messagebox.showinfo(name,
        f"Phone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")

def search_contact():
    keyword = search_entry.get().strip().lower()
    listbox.delete(0, tk.END)
    for name, info in contacts.items():
        if keyword in name.lower() or keyword in info["Phone"]:
            listbox.insert(tk.END, name)

def update_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a contact to update.")
        return

    name = listbox.get(selected[0])
    contact = contacts[name]

    new_phone = simpledialog.askstring("Update Phone", f"Current: {contact['Phone']}")
    new_email = simpledialog.askstring("Update Email", f"Current: {contact['Email']}")
    new_address = simpledialog.askstring("Update Address", f"Current: {contact['Address']}")

    contacts[name] = {
        "Phone": new_phone or contact['Phone'],
        "Email": new_email or contact['Email'],
        "Address": new_address or contact['Address']
    }
    messagebox.showinfo("Updated", f"Contact '{name}' updated.")
    update_listbox()

def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a contact to delete.")
        return
    name = listbox.get(selected[0])
    confirm = messagebox.askyesno("Confirm Delete", f"Delete contact '{name}'?")
    if confirm:
        del contacts[name]
        update_listbox()
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")

def update_listbox():
    listbox.delete(0, tk.END)
    for name in contacts:
        listbox.insert(tk.END, name)

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Layout
root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x550")

# Input Fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root, width=50)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contact", command=view_contact).pack()
tk.Button(root, text="Update Contact", command=update_contact).pack()
tk.Button(root, text="Delete Contact", command=delete_contact).pack()

# Search and Listbox
tk.Label(root, text="Search by Name or Phone:").pack(pady=5)
search_entry = tk.Entry(root, width=40)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

# Run the app
root.mainloop()
