# Secure Data Hiding in Image Using Steganography

## 📌 Overview  
This project implements an **image steganography technique** to securely hide messages within an image using pixel manipulation. It provides a **user-friendly graphical interface** with separate encoding and decoding sections. Additionally, **passcode protection** ensures that only authorized users can decrypt the hidden message, adding an extra layer of security.

---

## 🚀 Features  
✅ **Secure Message Hiding** – Embed text within an image without altering its visual appearance.  
✅ **Passcode Protection** – Ensures only users with the correct password can decode the message.  
✅ **Enhanced GUI** – Separate interfaces for encoding and decoding with a clean, modern design.  
✅ **Cross-Platform Compatibility** – Works on Windows, Linux, and macOS.  
✅ **Background Images & Theming** – Updated UI with visually appealing colors and backgrounds.  

---

## 🛠️ Technologies Used  
- **Python** – Core programming language.  
- **OpenCV (cv2)** – For image processing and manipulation.  
- **Tkinter** – For building an interactive GUI.  
- **PIL (Pillow)** – For handling and displaying images.  
- **NumPy** – For efficient pixel manipulation.  
- **OS Module** – For file handling and opening the generated encrypted image.  

---

## 📂 Installation  

### 🔹 Prerequisites  
Ensure **Python 3.x** is installed. You can download it from [Python's official site](https://www.python.org/).  

### 🔹 Install Dependencies  
```sh
pip install opencv-python
pip install opencv-python pillow numpy
```

---

## 🚀 Usage  

### 🔹 1. Hiding a Message in an Image  
1. Run the script:  
   ```sh
   python stego.py
   ```
2. Select **Encoding** from the home screen.
3. Choose an image file from your system.
4. Enter your **secret message** and **passcode**.
5. Click **"Encode Message"** to hide the message within the image.
6. The **encrypted image** (encryptedImage.png) will be generated.

### 🔹 2. Retrieving the Hidden Message  
1. Run the script again:  
   ```sh
   python stego.py
   ```
2. Select **Decoding** from the home screen.
3. Choose the **encrypted image**.
4. Enter the **correct passcode**.
5. The **hidden message** will be displayed.

---

## 🎯 Future Scope  
- **Advanced Encryption** – Integrate AES/RSA encryption for added security.  
- **Support for Multiple Formats** – Extend support to BMP, GIF, and TIFF.  
- **Mobile Application** – Develop an Android/iOS app using Flutter or React Native.  
- **Cloud-Based Storage** – Enable secure cloud storage for encrypted images.  
- **Video Steganography** – Extend the project to hide messages in video frames.  

---

## 📌 Conclusion  
This project successfully implements a secure steganography system using image pixel manipulation. By providing a **password-protected, user-friendly GUI**, it allows users to easily encode and decode secret messages within images. Future enhancements can further improve security and usability.

---


## 💡 Contributing  
Pull requests are welcome! Feel free to **fork the repository** and improve upon it.

---

## 💻 Developed by **Vinayak Mehta** 🚀


