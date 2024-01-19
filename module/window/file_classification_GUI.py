import os
import shutil
import tkinter as tk
import webbrowser
from tkinter import filedialog
from tkinter import messagebox

def open_link():
    webbrowser.open("https://taskautomation.tistory.com")

def organize_files():
    folder_path = path_entry.get()
    
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "The specified path does not exist.")
        return

    os.chdir(folder_path)

    for file in os.listdir(folder_path):
        if os.path.isfile(file):
            extension = file.split('.')[-1]
            directory = os.path.join(folder_path, extension)
            if not os.path.exists(directory):
                os.makedirs(directory)
            shutil.move(file, os.path.join(directory, file))

    messagebox.showinfo("Complete", "Files have been organized!")

def browse_folder():
    folder_path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_path)



# GUI setup
root = tk.Tk()
root.title("File Organizer")

# Path entry
path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=20)

# Browse button
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=5)

# Organize button
organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.pack(pady=10)

# Contact label with hyperlink
contact_label1 = tk.Label(root, text="문의 메일: gettenmd@gmail.com", fg="blue")
contact_label2 = tk.Label(root, text="업무 자동화 블로그 : https://taskautomation.tistory.com", fg="blue", cursor="hand2")
contact_label1.pack(pady=10)
contact_label2.pack(pady=10)
contact_label2.bind("<Button-1>", lambda e: open_link())

root.mainloop()
