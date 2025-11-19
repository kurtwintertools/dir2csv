import csv
import os
import re

# Regex to match file lines from dir /s output
file_line_pattern = re.compile(
    r'^\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}\s+[AP]M\s+([\d,]+)\s+(.+)$'
)

# Get current working directory
folder = os.getcwd()

# Loop through all .txt files in the folder
for filename in os.listdir(folder):
    if filename.lower().endswith(".txt"):
        input_path = os.path.join(folder, filename)
        output_path = os.path.join(folder, os.path.splitext(filename)[0] + ".csv")

        rows = []
        current_path = ""

        with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                # Detect directory headers
                if line.lower().startswith("directory of"):
                    current_path = line.split(" ", 2)[-1]
                    continue

                # Match file lines
                match = file_line_pattern.match(line)
                if match:
                    size_str, fname = match.groups()
                    size_bytes = int(size_str.replace(",", ""))
                    full_path = os.path.join(current_path, fname)
                    rows.append([full_path, size_bytes])

        # Write CSV
        with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["FullPath", "SizeBytes"])
            writer.writerows(rows)

        print(f"Processed {filename} → {output_path} ({len(rows)} entries)")
