# .STA data conversion
This is a Python script that converts files with the ".STA" extension. The script reads all files in the "to_change" directory, and for each file, it looks for any lines that start with "<38" and "<24". If both of these lines exist, the script swaps their contents.

The converted files are then saved in the "changed" directory with the same file name as the original file. If a file with the same name already exists in the "changed" directory, the script appends a number to the beginning of the new file name.

## Requirements 
- Python 3.x

## How to use
1. Place your .STA files in the "to_change" directory.
2. Run the script.
3. The converted files will be in the "changed" directory.

## Note
- The script will create the needed folders if they do not exist.
- If a file with the same name already exists, the script will add a number to the file name to avoid overwriting the existing file.