# Secure-Data-Hiding-in-Image-Using-Steganography

## 📌 Overview  
This project implements a **steganography-based technique** to securely hide messages within an image. By modifying pixel values, secret data is embedded without altering the image's visual appearance. Additionally, **passcode protection** ensures that only authorized users can decrypt the hidden message.  

---

## 🚀 Features  
✅ **Secure Message Hiding** – Embed text within an image without noticeable changes.  
✅ **Passcode Protection** – Only users with the correct password can decrypt the message.  
✅ **Lightweight & Fast** – Uses minimal storage and processing power.  
✅ **Cross-Platform Compatibility** – Works on Windows, Linux, and macOS.  

---

## 🛠️ Technologies Used  
- **Python** – Core programming language  
- **OpenCV (cv2)** – Image processing  
- **OS Module** – File handling  
- **Dictionary Mapping** – Character encoding  

---

## 📂 Installation  

### 🔹 Prerequisites  
Ensure **Python 3.x** is installed. You can download it from [Python's official site](https://www.python.org/).  

### 🔹 Install Dependencies
pip install opencv-python

---

## 🚀 Usage
### 🔹 1. Hiding a Message in an Image
- Place the image (e.g., Vinayak.jpg) in the project folder.
- Run the script: 
stego.py
- Enter your secret message and passcode when prompted.
- The encrypted image (encryptedImage.jpg) will be generated.
### 🔹 2. Retrieving the Hidden Message
- Run the script again.
- Enter the correct passcode to decrypt the message.
- The hidden message will be displayed.

---

## 🎯 Future Scope
-  **Stronger Encryption** – Implement AES/RSA before embedding messages.
-  **Support for Multiple Formats** – Extend support to PNG, BMP, and TIFF.
-  **Graphical Interface** – Create a user-friendly GUI using Tkinter/PyQt.
-  **Video Steganography** – Extend the project to hide messages in video frames.
-  **Cloud-Based Application** – Develop a web-based tool for online encoding & decoding.

---

##  💡 Contributing
Pull requests are welcome! Feel free to fork the repository and improve upon it.

---

## 💻 Developed by Vinayak Mehta 🚀
