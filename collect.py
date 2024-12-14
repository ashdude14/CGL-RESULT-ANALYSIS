import PyPDF2
import csv
import time

LIST_2 = "../../data/LIST-2.pdf"
LIST_3 = "../../data/LIST-3.pdf"
DATA_3 = "../../data/data-3.csv"
DATA_2 = "../../data/data-2.csv"


# Function to write extracted pages into a CSV file
def writeCsv(input_file_path, output_file_path):
    with open(input_file_path, "rb") as f:
      reader = PyPDF2.PdfReader(f)
      with open(output_file_path, "w", encoding="utf-8", newline="") as f:
         csv_writer = csv.writer(f)
         csv_writer.writerow(["Page Number", "Text Content"])
         for page_number,page in enumerate(reader.pages,start=1) :
          csv_writer.writerow([page_number,page.extract_text()])
        


start=time.time()
writeCsv(LIST_2, DATA_2)
end=time.time()
print("Total time taken to write data for LIST_2 (sec) : ",end-start)

start1=time.time()
writeCsv(LIST_3, DATA_3)
end1=time.time()
print("Total time taken to write data for LIST_3 (sec) : ",end1-start1)




