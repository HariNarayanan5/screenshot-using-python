import time
import tkinter as tk
from tkinter import filedialog, messagebox

import pyautogui
from PIL import Image, ImageTk


def take_screenshot():
    try:
        user_confirmation = messagebox.askyesno("Confirmation", "Do you want to save the screenshot?")
        if user_confirmation:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                screenshot = pyautogui.screenshot()
                screenshot.save(file_path)
                feedback_label.config(text=f"Screenshot saved to:\n{file_path}")
                display_preview(screenshot)
            else:
                feedback_label.config(text="Screenshot not saved.")
        else:
            feedback_label.config(text="Screenshot not saved.")
    except Exception as e:
        feedback_label.config(text=f"Error: {e}", fg='red')

def display_preview(image):
    image.thumbnail((200, 200))
    img = ImageTk.PhotoImage(image)
    preview_label.config(image=img)
    preview_label.image = img

def delayed_screenshot():
    try:
        delay_time = int(delay_entry.get())
        if delay_time > 0:
            feedback_label.config(text=f"Taking screenshot in {delay_time} seconds...", fg='blue')
            progress_label.place(x=120, y=200)
            for i in range(delay_time, 0, -1):
                progress_label.config(text=f"Taking screenshot in {i} seconds...")
                root.after(i * 1000, lambda: progress_label.config(text=f"Taking screenshot in {i-1} seconds..."))
            root.after(delay_time * 1000, take_screenshot)
        else:
            feedback_label.config(text="Please enter a valid positive number.", fg='red')
    except ValueError:
        feedback_label.config(text="Please enter a valid number.", fg='red')

def cancel_delayed_screenshot():
    feedback_label.config(text="Delayed screenshot canceled.", fg='orange')

def on_hover_enter(event):
    event.widget.config(bg='lightblue')

def on_hover_leave(event):
    event.widget.config(bg='white')

root = tk.Tk()
root.title("Screenshot Taker")
root.geometry('500x450')
root.configure(bg='lightblue')

# Welcome animation
welcome_label = tk.Label(root, text="Welcome to Screenshot Taker", font=("Arial", 24), bg='lightblue')
welcome_label.pack(pady=30)

def welcome_animation():
    for _ in range(3):
        welcome_label['bg'] = 'lightgreen'
        root.update()
        time.sleep(0.5)
        welcome_label['bg'] = 'lightblue'
        root.update()
        time.sleep(0.5)

root.after(1000, welcome_animation)

# Capture button animation
def button_animation():
    for i in range(3):
        delay_button.config(bg='lightblue')
        root.update()
        time.sleep(0.5)
        delay_button.config(bg='lightgreen')
        root.update()
        time.sleep(0.5)

delay_label = tk.Label(root, text="Enter delay time (in seconds):", bg='lightblue')
delay_label.pack()
delay_entry = tk.Entry(root)
delay_entry.pack()

delay_button = tk.Button(root, text="Take Delayed Screenshot", command=delayed_screenshot, bg='lightgreen')
delay_button.pack(pady=10)

cancel_button = tk.Button(root, text="Cancel Delayed Screenshot", command=cancel_delayed_screenshot, bg='salmon')
cancel_button.pack(pady=10)

preview_label = tk.Label(root, bg='lightblue')
preview_label.pack(pady=10)

feedback_label = tk.Label(root, text="", bg='lightblue', fg='green')
feedback_label.pack()

progress_label = tk.Label(root, text="", font=("Arial", 12), bg='lightblue')

status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

delay_button.bind("<Enter>", on_hover_enter)
delay_button.bind("<Leave>", on_hover_leave)
cancel_button.bind("<Enter>", on_hover_enter)
cancel_button.bind("<Leave>", on_hover_leave)

def about():
    messagebox.showinfo("About", "Screenshot Taker App v1.0")

def help_info():
    messagebox.showinfo("Help", "This app allows you to capture screenshots.\n\n"
                                "1. Click 'Take Delayed Screenshot' to capture a screenshot after a delay.\n"
                                "2. Click 'Cancel Delayed Screenshot' to stop the countdown.")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Help", command=help_info)

root.mainloop()
