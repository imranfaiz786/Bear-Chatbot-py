import tkinter as tk
from tkinter import messagebox
from transformers import pipeline
from PIL import Image, ImageTk

# Initialize the chatbot model using the text-generation pipeline
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Function to handle sending a message
def send_message():
    user_input = user_input_box.get()
    if user_input != "":
        # Display User Message in Light Pink Box (no border)
        user_message = tk.Label(chat_log_frame, text=f"YOU: {user_input}", bg="#FFB6C1", fg="white", font=("Comic Sans MS", 12), 
        wraplength=350, anchor="w", width=50, justify="left")
        user_message.pack(anchor="w", fill="x")
        user_input_box.delete(0, tk.END)
        
        # Use the model to generate a response
        response = chatbot(user_input, max_length=1000, num_return_sequences=1)
        
        # Display Bot Message in Soft Peach Box (no border)
        bot_message = tk.Label(chat_log_frame, text=f"BEAR: {response[0]['generated_text']}", bg="#FFD1DC", fg="black", font=("Comic Sans MS", 12), 
        wraplength=350, anchor="w", width=50, justify="left")
        bot_message.pack(anchor="w", fill="x")
        
        # Ensure the scrollbar scrolls to the bottom when new messages appear
        chat_log_frame.update_idletasks()
        chat_log_canvas.yview_moveto(1)

# Function to handle the close button click event
def close_chat():
    response = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if response:
        root.quit()

# Initialize the main window
root = tk.Tk()
root.title("Bear Chat")

# Set a nice icon for the window (optional)
try:
    root.iconphoto(False, ImageTk.PhotoImage(Image.open('assets/logo.png')))
except Exception as e:
    print(f"Error setting icon: {e}")

# Set window size and position
root.geometry("500x600")
root.resizable(False, False)

# Outer Frame for the chat interface with soft pink background
frame = tk.Frame(root, bg="#FF69B4", padx=40, pady=20)  # Set background color of the outer frame to light pink
frame.pack(fill="both", expand=True)  # This ensures the outer frame expands to fill the window

# Scrollbar for the chat log with pink color
chat_log_canvas = tk.Canvas(frame, bg="#FFD1DC")  # Light pink background for canvas
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=chat_log_canvas.yview)
chat_log_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_log_canvas.config(yscrollcommand=scrollbar.set)

# Create a frame to hold the chat messages with white background
chat_log_frame = tk.Frame(chat_log_canvas, bg="white")  # Set background color of chat log frame to white
chat_log_canvas.create_window((0, 0), window=chat_log_frame, anchor="nw")

# User input box with rounded corners and soft pink color
user_input_box = tk.Entry(root, width=40, font=("Comic Sans MS", 12), bd=2, relief="solid", fg="#FF1493", bg="#FFF0F5")  # Light pink background
user_input_box.pack(pady=10)

# Bottom Frame for the entire lower section with a pink background
bottom_frame = tk.Frame(root, bg="#FF69B4", padx=40, pady=20)  # Add a pink frame at the bottom
bottom_frame.pack(side=tk.BOTTOM, fill="x", pady=10)

# Send button with rounded corners, soft pink, and gradient effect
send_button = tk.Button(bottom_frame, text="Send", font=("Comic Sans MS", 12), command=send_message, width=15, height=2, bg="#C71585", fg="white", bd=0, 
relief=tk.RAISED, activebackground="#8B008B", activeforeground="white")
send_button.grid(row=0, column=0, padx=5)

# Exit button with dark pinkish red and hover effect
exit_button = tk.Button(bottom_frame, text="Exit", font=("Comic Sans MS", 12), command=close_chat, width=15, height=2, bg="#C71585", fg="white", bd=0, 
relief=tk.RAISED, activebackground="#8B008B", activeforeground="white")
exit_button.grid(row=0, column=1, padx=5)

# Start the main event loop
root.mainloop()
