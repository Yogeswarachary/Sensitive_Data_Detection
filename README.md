# Sensitive Data Detection & Compliance Assistant
## Key Features
The Sensitive Data Detection & Compliance Assistant is a Streamlit application designed to detect sensitive data in uploaded files (PDF, TXT, CSV) and provide compliance observations, security risks, and suggested remediation steps. The key features include:
* Detection of various sensitive data types such as Aadhaar, PAN, email, phone, credit card, IFSC, UPI, API keys, and employee IDs
* Classification of overall document risk level based on detected sensitive data types
* Generation of compliance observations, security risks, and suggested remediation steps
* Support for rule-based question answering over the document

## Installation Instructions
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```
The `requirements.txt` file includes the necessary dependencies:
```markdown
streamlit>=1.30.0
pandas>=1.5.0
pdfplumber>=0.7.6
python-dotenv>=1.0.0
```
## Usage Examples
To use the application, simply upload a file (PDF, TXT, or CSV) and the application will detect sensitive data and provide compliance observations, security risks, and suggested remediation steps.
```python
import streamlit as st

# Upload a file
uploaded_file = st.file_uploader(
    "Upload a file (PDF/TXT/CSV)",
    type=["pdf", "txt", "csv"]
)

# Detect sensitive data and generate compliance observations, security risks, and suggested remediation steps
if uploaded_file is not None:
    raw_text, df = read_file(uploaded_file)
    findings = detect_pii(raw_text)
    stats = aggregate_stats(findings)
    risk_info = classify_risk(findings)
    summary = build_compliance_summary(findings, risk_info)

    # Display the results
    st.subheader("Detected Sensitive Data (Findings)")
    if findings:
        st.write(f"Total findings: {len(findings)}")
        st.dataframe(findings)
    else:
        st.write("No sensitive data detected with current patterns.")

    st.subheader("Compliance Observations")
    for line in summary["compliance_observations"]:
        st.write(f"- {line}")

    st.subheader("Security Risks")
    if summary["security_risks"]:
        for line in summary["security_risks"]:
            st.write(f"- {line}")
    else:
        st.write("- No specific security risks identified by current rules.")

    st.subheader("Suggested Remediation Steps")
    for line in summary["remediation_steps"]:
        st.write(f"- {line}")
```
You can also ask questions about the document using the question answering feature:
```python
# Ask a question
user_question = st.text_input(
    "Type your question (e.g., 'What sensitive data exists in the document?')"
)

if user_question:
    answer = answer_question(
        question=user_question,
        text=raw_text,
        findings=findings,
        risk_info=risk_info,
    )
    st.markdown("**Answer:**")
    st.text(answer)
```
## Project Structure
The project consists of the following files and directories:
* `app.py`: The main application file
* `core/`: A directory containing the core functionality of the application
	+ `detector.py`: Contains the sensitive data detection logic
	+ `file_loader.py`: Contains the file loading logic
	+ `patterns.py`: Contains the regular expression patterns for sensitive data detection
	+ `risk_classifier.py`: Contains the risk classification logic
	+ `summary.py`: Contains the compliance observation, security risk, and remediation step generation logic
	+ `qa.py`: Contains the question answering logic
* `requirements.txt`: A file containing the required dependencies for the application