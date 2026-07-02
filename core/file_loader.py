import io
from typing import Tuple

import pandas as pd
import pdfplumber  # make sure to install: pip install pdfplumber


def read_txt_file(uploaded_file) -> str:
    """
    Read a text (.txt) file from Streamlit's UploadedFile and return plain text.
    """
    # uploaded_file.read() gives you the raw bytes (binary data)
    raw_bytes = uploaded_file.read()
    # decode bytes into a string using UTF-8 encoding
    text = raw_bytes.decode("utf-8", errors="ignore")
    return text


def read_csv_file(uploaded_file) -> Tuple[str, pd.DataFrame]:
    """
    Read a CSV file and return both:
    - raw_text: everything converted into one big string
    - df: the pandas DataFrame for any future structured analysis
    """
    # uploaded_file can be passed directly to pandas
    df = pd.read_csv(uploaded_file)
    # convert entire DataFrame into a single text string
    raw_text = df.to_string()
    return raw_text, df


def read_pdf_file(uploaded_file) -> str:
    """
    Read a PDF file using pdfplumber and return the extracted text.
    Note: works for text-based PDFs, not scanned image-only PDFs.
    """
    # Streamlit gives a file-like object; we read its bytes
    pdf_bytes = uploaded_file.read()

    # pdfplumber expects a file-like object, so we wrap bytes in BytesIO
    pdf_file_like = io.BytesIO(pdf_bytes)

    all_text = ""

    # open the PDF with pdfplumber
    with pdfplumber.open(pdf_file_like) as pdf:
        # pdf.pages is a list of pages; we iterate over each page
        for page in pdf.pages:
            # extract_text() tries to read visible text from the page
            page_text = page.extract_text()
            if page_text:
                # add a newline between pages for readability
                all_text += page_text + "\n"

    return all_text


def read_file(uploaded_file) -> Tuple[str, pd.DataFrame | None]:
    """
    Main function:
    - Detect file type by extension
    - Call appropriate reader
    - Always return raw_text and optionally a DataFrame (for CSV).
    """
    filename = uploaded_file.name
    # lower() to avoid issues like .PDF vs .pdf
    filename_lower = filename.lower()

    if filename_lower.endswith(".txt"):
        raw_text = read_txt_file(uploaded_file)
        return raw_text, None

    elif filename_lower.endswith(".csv"):
        raw_text, df = read_csv_file(uploaded_file)
        return raw_text, df

    elif filename_lower.endswith(".pdf"):
        raw_text = read_pdf_file(uploaded_file)
        return raw_text, None

    else:
        # unsupported file type
        raise ValueError("Unsupported file type. Please upload a PDF, TXT, or CSV file.")