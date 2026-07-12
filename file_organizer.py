import os
import shutil

# Define the directory to track (e.g., Downloads folder)
TRACK_FOLDER = os.path.expanduser("~/Downloads")
DEST_IMAGES = os.path.expanduser("~/Downloads/Organized_Images")
DEST_DOCS = os.path.expanduser("~/Downloads/Organized_Documents")

# Create folders if they don't exist
for folder in [DEST_IMAGES, DEST_DOCS]:
    if not os.path.exists(folder):
        os.makedirs(folder)

def organize_folder():
    for filename in os.listdir(TRACK_FOLDER):
        source = os.path.join(TRACK_FOLDER, filename)
        
        # Skip directories
        if os.path.isdir(source):
            continue
            
        # Sort based on file extensions
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            shutil.move(source, os.path.join(DEST_IMAGES, filename))
            print(f"Moved Image: {filename}")
        elif filename.lower().endswith(('.pdf', '.docx', '.txt', '.xlsx')):
            shutil.move(source, os.path.join(DEST_DOCS, filename))
            print(f"Moved Document: {filename}")

if __name__ == "__main__":
    print("Starting automated folder organization...")
    organize_folder()
    print("Organization complete!")
