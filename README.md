# Aicte-Cyber
Secure Data Hiding in Images using Steganography
📌 Overview
This project allows users to securely hide and retrieve multiple file types (images, videos, PDFs, audio, and text) inside an image using steganography.
The hidden data is protected by a 4-digit PIN, ensuring that only authorized users can extract the information.
![Screenshot 2025-02-16 174703](https://github.com/user-attachments/assets/d99bd5c1-0bf0-4282-850e-0ab54e42ea57)

🚀 Features
✅ Supports Multiple File Types – Hide images, videos, PDFs, audio, and text in one image
✅ PIN Protection – Data can only be extracted using the correct 4-digit PIN
✅ No Suspicious Traces – The output image looks normal, with no noticeable alterations
✅ Fully Automated – Detects and hides all files inside the secret_files folder
✅ Extracts Data Securely – Only authorized users can retrieve the information

⚙️ Installation & Setup
1️⃣ Install Dependencies
Make sure you have Python installed, then install the required libraries:


pip install opencv-python
2️⃣ Prepare Your Files
Place the files you want to hide inside the secret_files folder.
Ensure your cover image is named cover_image.png and is in the same directory as the scripts.
3️⃣ Run the Script to Hide Data

python hide_data.py
Enter a secret message when prompted.
Enter a 4-digit PIN to protect the hidden data.
This will generate a stego_image.png containing the hidden files.
4️⃣ Extract Hidden Data

python extract_data.py
Enter the correct PIN to extract the files.
The extracted files will be saved in the extracted_files folder.

🛠️ How It Works
The script compresses all files inside secret_files into a ZIP archive.
The 4-digit PIN is securely embedded inside the ZIP data.
The ZIP data is then appended to the cover image to create a stego_image.png.
During extraction, the script verifies the PIN before extracting the hidden files.

🔒 Security Measures
✅ PIN is Not Stored in Plain Text – It is embedded within the steganographic data.
✅ Files Remain Completely Hidden – The output file appears as a normal image.
✅ Unauthorized Users Cannot Detect the Hidden Data – Without the PIN, extraction is impossible.

📌 Future Scope
🔹 AES Encryption – Encrypt the hidden data before embedding it in the image
🔹 Cloud Integration – Store and retrieve stego images securely online
🔹 Mobile App – Implement this technique on Android & iOS
🔹 AI-based Steganalysis – Detect hidden files in images automatically
