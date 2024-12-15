import os
from base64 import b64decode

def decode_filename(encoded_name: str) -> str:
    try:
        # Decode the base64-encoded filename
        original_name = b64decode(encoded_name.encode()).decode('utf-8')
        return original_name
    except Exception as e:
        print(f"Error decoding filename {encoded_name}: {e}")
        return None

def decode_directory(path: str):
    try:
        for entry in os.scandir(path):
            if entry.is_dir():
                # Recurse into subdirectories
                decode_directory(entry.path)
            elif entry.is_file():
                # Split the filename and extension
                encoded_name, extension = os.path.splitext(entry.name)
                original_name = decode_filename(encoded_name)
                if original_name:
                    # Build the new file name
                    new_file_path = os.path.join(os.path.dirname(entry.path), f"{original_name}{extension}")
                    # Rename the file
                    os.rename(entry.path, new_file_path)
                    print(f"Decoded file: {entry.path} -> {new_file_path}")
    except Exception as e:
        print(f"Error processing directory {path}: {e}")

# Get the directory to decode from the user
path = input("Enter the directory path to decode filenames: ")

# Check if the path is valid
if not os.path.exists(path) or not os.path.isdir(path):
    print("Invalid path. Please provide a valid directory.")
else:
    decode_directory(path)
