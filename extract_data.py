import os
import zipfile

# Define file paths
stego_image = "stego_image.png"
extracted_zip = "extracted_data.zip"
extracted_folder = "extracted_files"  # Folder for extracted files

# Read the stego image
with open(stego_image, "rb") as stego:
    data = stego.read()

# Ask for the PIN to extract data
user_pin = input("Enter the 4-digit PIN to unlock the data: ").encode()

# Find the hidden ZIP data inside the image
zip_signature = b"PK\x03\x04"  # ZIP file signature
zip_index = data.find(zip_signature)

if zip_index != -1:
    # Extract the PIN and ZIP data
    extracted_pin = data[zip_index - 4:zip_index]  # Get stored PIN
    zip_data = data[zip_index:]  # Extract ZIP data

    # Check if the entered PIN matches
    if user_pin == extracted_pin:
        with open(extracted_zip, "wb") as zip_file:
            zip_file.write(zip_data)

        # Extract ZIP contents
        with zipfile.ZipFile(extracted_zip, "r") as zipf:
            zipf.extractall(extracted_folder)
        os.remove(extracted_zip)  # Delete zip after extraction

        print(f"✅ Hidden data extracted to '{extracted_folder}'.")
    else:
        print("❌ Incorrect PIN. Access Denied.")
else:
    print("❌ No hidden data found in the image.")
