import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Function to encode the message into an image
def encode():
    file_path = filedialog.askopenfilename(title="Vinayak.jpg", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    msg = entry_message.get()
    password = entry_password.get()
    if not msg or not password:
        messagebox.showerror("Error", "Message and Password cannot be empty!")
        return
    
    m, n, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    encoded_image_path = "encryptedImage.png"
    cv2.imwrite(encoded_image_path, img)
    messagebox.showinfo("Success", "Message encoded successfully!")
    os.system(f"start {encoded_image_path}")

# Function to decode the message from an image
def decode():
    file_path = filedialog.askopenfilename(title="Select an Encrypted Image", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    pas = entry_password_dec.get()
    if pas != entry_password.get():
        messagebox.showerror("Error", "Incorrect Password!")
        return
    
    message = ""
    m, n, z = 0, 0, 0
    for _ in range(len(entry_message.get())):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    messagebox.showinfo("Decrypted Message", f"Message: {message}")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("700x700")
root.configure(bg="#CADCFC")  # Updated background color

# Style Configuration
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)

# Frames for separate UI
frame_home = tk.Frame(root, bg="#8AB6F9")
frame_encode = tk.Frame(root, bg="#00246B")
frame_decode = tk.Frame(root, bg="#81CAD6")

def show_frame(frame):
    frame_home.pack_forget()
    frame_encode.pack_forget()
    frame_decode.pack_forget()
    frame.pack(fill="both", expand=True)

# Home Frame
label_title = tk.Label(frame_home, text="🔐 Secure Data Hiding in Image", font=("Arial", 18, "bold"), bg="#8AB6F9", fg="#DC3E26")
label_title.pack(pady=20)

btn_encode_screen = tk.Button(frame_home, text="🖼 Go to Encoding", font=("Arial", 12), bg="#EDCD44", fg="#00246B", command=lambda: show_frame(frame_encode))
btn_encode_screen.pack(pady=10)

btn_decode_screen = tk.Button(frame_home, text="🔓 Go to Decoding", font=("Arial", 12), bg="#DC3E26", fg="white", command=lambda: show_frame(frame_decode))
btn_decode_screen.pack(pady=10)

frame_home.pack(fill="both", expand=True)

# Encoding Frame
label_message = tk.Label(frame_encode, text="📜 Enter Secret Message:", font=("Arial", 12), bg="#00246B", fg="#FFFFFF")
label_message.pack(pady=5)
entry_message = tk.Entry(frame_encode, width=50)
entry_message.pack(pady=5)

label_password = tk.Label(frame_encode, text="🔑 Enter Passcode:", font=("Arial", 12), bg="#00246B", fg="#FFFFFF")
label_password.pack(pady=5)
entry_password = tk.Entry(frame_encode, width=50, show="*")
entry_password.pack(pady=5)

btn_encode = tk.Button(frame_encode, text="🚀 Encode Message", font=("Arial", 12), bg="#EDCD44", fg="#00246B", command=encode)
btn_encode.pack(pady=10)

btn_back_home1 = tk.Button(frame_encode, text="🏠 Back to Home", font=("Arial", 12), bg="#8AB6F9", fg="#00246B", command=lambda: show_frame(frame_home))
btn_back_home1.pack(pady=10)

# Decoding Frame
label_password_dec = tk.Label(frame_decode, text="🔐 Enter Passcode:", font=("Arial", 12), bg="#81CAD6", fg="#00246B")
label_password_dec.pack(pady=5)
entry_password_dec = tk.Entry(frame_decode, width=50, show="*")
entry_password_dec.pack(pady=5)

btn_decode = tk.Button(frame_decode, text="🔍 Decode Message", font=("Arial", 12), bg="#EDCD44", fg="#00246B", command=decode)
btn_decode.pack(pady=10)

btn_back_home2 = tk.Button(frame_decode, text="🏠 Back to Home", font=("Arial", 12), bg="#8AB6F9", fg="#00246B", command=lambda: show_frame(frame_home))
btn_back_home2.pack(pady=10)

root.mainloop()
