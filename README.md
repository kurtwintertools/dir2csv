# dir2csv

A simple Python script that converts the text output of a Windows `dir /s` command into a CSV file.  
Each row in the CSV contains:

- **FullPath**: the full path and filename (with extension)  
- **SizeBytes**: the file size in bytes  

This makes it easy to analyze directory listings, import them into Excel, or process them further.

---

## ✨ Features
- Parses standard `dir /s` output text files
- Extracts file paths and sizes
- Generates a CSV file with the same base name as the input `.txt`
- Processes all `.txt` files in the current folder automatically

---

## 📂 Example Workflow

1. Run `dir /s` in a Windows command prompt and redirect output to a text file:

   ```powershell
   dir /s > myfiles.txt
