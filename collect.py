import PyPDF2
import csv

LIST_2 = "../../data/LIST-2.pdf"
LIST_3 = "../../data/LIST-3.pdf"
DATA_3 = "../../data/data-3.csv"
DATA_2 = "../../data/data-2.csv"

# PDF extractor function
def readPdf(input_file_path):
    output = ""  # Initialize the output as an empty string
    with open(input_file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            output += page.extract_text()  # Extract text from each page
    return output

# Function to write extracted pages into a CSV file
def writeCsv(input_file_path, output_file_path):
    text_data = readPdf(input_file_path)  # Read the PDF content
    with open(output_file_path, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)
        for line in text_data.splitlines():  
            # Assuming each line contains comma-separated values; process it
            structured_data = line.split(",")  
            csv_writer.writerow(structured_data) 


#writeCsv(LIST_2, DATA_2)

