# Selective-copy


To copy .txt files from source folder and subfolder into destination folder using regex and shutil


The program uses shutil and re module.

Algorithm:

1. Create a Regex obj  for .txt file pattern.
2. Get a current folder,subfolder and file name in os.walk by passing current dir path os.walk
3. Check if a file exists or not in subfolder,if yes then check if file is .txt file or not.
4. If file in subfolder is a .txt file and file is not present in target folder then copy using shutil.copy.
5. Similarly, check for files present in folder if they are .txt or not. If .txt file is not present at target folder then copy .txt file to target folder. 
