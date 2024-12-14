###  Analyzing Social Media Controversy for SSC-CGL-2024 Tier-1 Result Fairness

#### This project aims to perform a comprehensive data analysis on the results of the SSC-CGL 2024 Tier-1 examination, focusing on fairness and transparency. Being closely connected to the aspirations of Indian youth and government job seekers, this analysis seeks to provide valuable insights into the examination process, which is a gateway for graduate candidates to secure Group B and Group C posts in various government departments.

---

## Data Description

- **List_3**: Contains details of **165,240 candidates** who qualified in the SSC-CGL 2024 Tier-1 examination.
- **List_2**: Contains details of **2,833 candidates**, representing a subset of qualifiers from specific examination centers or groups under scrutiny.

---
## Core Objectives

### Highlighting Examination Centers
- Identifying centers where an unusually high number of candidates qualified, which could suggest potential irregularities.
- This analysis is purely exploratory and is not intended for legal evidence.

### Exploring Other Insights
1. **Number of Candidates Qualified Under Different Filters**:
   - Age groups.
   - Location, based on examination centers.
   - Gender (Male, Female).
   - PwD (Persons with Disabilities) status.
2. **Selection Probability**:
   - Estimating the percentage chance of candidates clearing Tier-1.
3. **Reappearance Trends**:
   - Probability of candidates appearing multiple times.
4. **Statewise Selection Patterns**:
   - Distribution of qualifiers across different states.
5. **Fairness Reality Check**:
   - Estimating fairness based on data patterns.

---

## Phases of Analysis

### Data Collection
- Converting examination result PDFs to CSV format using the **PyPDF2** library for structured data analysis.
  -  python script for the data extraction and writing to csv file :
```python
    def writeCsv(input_file_path, output_file_path):
    with open(input_file_path, "rb") as f:
      reader = PyPDF2.PdfReader(f)
      with open(output_file_path, "w", encoding="utf-8", newline="") as f:
       csv_writer = csv.writer(f)
       csv_writer.writerow(["Page Number", "Text Content"])
       for page_number,page in enumerate(reader.pages,start=1) :
          csv_writer.writerow([page_number,page.extract_text()])
   ```
  - output console which calculates duration to execute the script : 
```bash
PS K:\DataAnalyst\SSC-CGL-2024-RESULT-ANALYSIS\.venv\Scripts> python.exe ../../collect.py
Total time taken to write data for LIST_2 (sec) :  5.281536102294922
Total time taken to write data for LIST_3 (sec) :  210.1253786087036
```
  - csv data preview : 
  ```csv
  Text Content
1," 
                                                                                                          Page No :   1  
                                           COMBINED GRADUATE LEVEL EXAM., 2024 (TIER -I)                                
 
                             LIST OF CANDIDATES QUALIFIED IN TIER -I FOR TIER -II (PAPER -I & PAPER -II)     
                             FOR THE POST OF STATISTICAL INVESTIGATOR                       (LIST -2)     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
Record#  ROLL       NAME                                    FATHERNAME                          MOTHERNAME                          DOB        CAT1 CAT2 CAT3  
      1  1004000700  MEHRAJ U DIN                             NOOR U DIN CHOWDHERY                NASEEMA                             13/01/1998 2           
      2  1004007636 NANCY SHARMA                             VINOD KUMAR                         VIPEN DEVI                          10/03/1999 2           
      3  1004015889 MANEESHA SINGH                           JITENDRA KUMAR KUSHWAHA             PADMA                               03/09/1999 6           
      4  1004016556 SWEETY PANDEY                            SUSHIL PANDEY                       ARUNA DEVI                          11/08/1997 0           
      5  1004020483 ABINASH CHOUDHARY                        KHARAYTI LAL                        SUNITA CHOUDHARY                    02/04/2001 2           
      6  1004022553 RAHUL CHALOTRA                           NATHA RAM                           VAISHNO DEVI                        07/09/2000 9         7  
      7  1007000681 AAQIB RASHID                             AB RASHID LONE                      NISA RA BEGUM                        08/01/1994 9         5  
      8  1007001854 ZAHID AHMAD TANTRAY                      GHULAM MOHAMMAD TANTRAY             SHAHZADA BANU                       15/12/1997 9         8  
      9  1010000855 POOJA RANI                               VINOD GARG                          POONAM DEVI                         05/02/1997 9           
     10  1010001001 AVINAB SHARMA                            AJEET KUMAR                         MADHU SHARMA                        19/01/200 2 9           
     11  1010001028 ROSHAN KUMAR                             YOGENDRA PRASAD SINGH               REENA DEVI                          28/04/1994 6           
     12  1010001641 SHANKI DHILLON                           TEJVIR SINGH                        SUNITA DEVI                         12/06/1995 9           
     13  1010001833 JATIN JAIN                               VINOD JAIN                          KAMLESH RANI                        05/02/2000 0           
     14  1010001984 AMAN K UMAR                               NARENDRA KUMAR                      MANJU                               05/03/1997 6           
     15  1010003192 GAURAV KUMAR                             NIRANJAN CHAUDHARY                  PADMA DEVI                          18/09/1997 6           
     16  1010003824 GIRRAJ PRASAD PROHIT                     RAMESHWAR SHARMA                    RAMWATI DEVI                        01/07/1997 0           
     17  1010003940 DEEPANKAR DUTTA                          KEWAL KUMAR                         KIRAN BALA                          19/03/2000 2           
  ```

### Data Cleaning and Transformation
- Preparing data for insights extraction.

### Insight Generation
- Applying statistical and exploratory analysis techniques to derive meaningful trends.

### Visualization
- Presenting findings in **Power BI dashboards** for easy interpretation.

---

This project serves as a **data-driven approach** to support transparency and improve public trust in the examination process, ensuring fairness for all candidates.
