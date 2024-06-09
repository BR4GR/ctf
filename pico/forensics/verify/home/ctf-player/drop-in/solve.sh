#!/bin/bash

# Directory containing the files
directory="files"

# Loop through all files in the directory
for file in "$directory"/*; do
    # Check if it is a file
    if [ -f "$file" ]; then
        echo "Attempting to decrypt $file..."
        
        # Attempt to decrypt the file
        if openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "$file" -k picoCTF > /dev/null 2>&1; then
            echo "Success! The file $file was decrypted successfully."
            openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "$file" -k picoCTF
            break
        else
            echo "Failed to decrypt $file."
        fi
    fi
done

echo "Script completed."
