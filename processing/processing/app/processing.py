import argparse
import json
import PyPDF2

def main():
    parser = argparse.ArgumentParser(description="Run the ETL process on a PDF file")
    parser.add_argument("--processing_unit", required=True, help="Processing unit")
    args = parser.parse_args()

    processing_units = json.loads(args.processing_unit)
    
    print (f"Process started for {processing_units}")

    file_path = processing_units['file']
    with open(file_path, "rb") as pdf_file:
        read_pdf = PyPDF2.PdfReader(pdf_file)
        number_of_pages = len(read_pdf.pages)
        print (f"Number of pages {number_of_pages}")
        page = read_pdf.pages[0]
        print(page.get_contents())

if __name__ == "__main__":
    main()
