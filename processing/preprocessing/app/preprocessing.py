import argparse
import json
from pathlib import Path
from pypdf import PdfReader, PdfWriter

def main():
    parser = argparse.ArgumentParser(description="Run the ETL process on a PDF file")
    parser.add_argument("--file_path", required=True, help="Name of the PDF file to process")
    parser.add_argument("--output_path", required=True, help="Output path")
    args = parser.parse_args()

    print ("Data workflow - preprocessing")

    file_path = Path(args.file_path)
    output_path = Path(args.output_path)
    input_pdf = PdfReader(file_path)

    processing = []
    for i in range(int(len(input_pdf.pages))):
        page_writer = PdfWriter()
        page_writer.add_page(input_pdf.pages[i])
        page_file_name = output_path / f"{file_path.stem}_{i}{file_path.suffix}"
        with open(page_file_name, "wb") as f:
            page_writer.write(f)
        processing.append({"file": page_file_name.absolute().as_posix()})
        
    f = open("processing_split.txt", "w")
    f.write(json.dumps(processing))
    f.close()


if __name__ == "__main__":
    main()
