import os
import zipfile

# Define file paths
cover_image = "cover_image.png"  # Base image
stego_image = "stego_image.png"  # Output image with hidden data
hidden_data_zip = "hidden_data.zip"  # Zip file containing hidden files
secret_folder = "secret_files"  # Folder containing files to be hidden

# Ask for a secret message and PIN
secret_message = input("Enter a secret message: ")
secret_pin = input("Enter a 4-digit PIN: ")

# Create a ZIP file containing hidden data
with zipfile.ZipFile(hidden_data_zip, "w") as zipf:
    zipf.writestr("message.txt", secret_message)  # Save secret message in ZIP
    
    # Add all files from the 'secret_files' folder
    if os.path.exists(secret_folder):
        for file in os.listdir(secret_folder):
            file_path = os.path.join(secret_folder, file)
            if os.path.isfile(file_path):
                zipf.write(file_path, arcname=file)  # Add file with just its name
    else:
        print(f"❌ Error: Folder '{secret_folder}' not found.")
        exit()

# Read the cover image
with open(cover_image, "rb") as img_file:
    image_data = img_file.read()

# Read the ZIP file data
with open(hidden_data_zip, "rb") as zip_file:
    zip_data = zip_file.read()

# Hide the PIN inside the ZIP data
encoded_pin = secret_pin.encode()
secured_data = encoded_pin + zip_data  # PIN + Hidden ZIP data

# Merge image and secured data
stego_data = image_data + secured_data

# Save the stego image
try:
    with open(stego_image, "wb") as stego:
        stego.write(stego_data)
    print(f"✅ Data hidden successfully in '{stego_image}'.")
except Exception as e:
    print(f"❌ Error: {e}")

# Clean up temporary ZIP file
os.remove(hidden_data_zip)
