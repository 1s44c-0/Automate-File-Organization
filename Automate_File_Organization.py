import os
import shutil

# Define the directory to organize
directory = "/path/to/your/directory"

# Define file type categories
categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
}

def organize_files(directory, categories):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in categories.items():
                if file_ext in extensions:
                    category_path = os.path.join(directory, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(filepath, category_path)
                    print(f"Moved: {filename} to {category}/")
                    moved = True
                    break
            if not moved:
                print(f"No category for: {filename}")

if __name__ == "__main__":
    organize_files(directory, categories)
