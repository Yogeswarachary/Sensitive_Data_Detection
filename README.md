# Sensitive Data Detection & Compliance Assistant
## Setup Instructions
To set up the Sensitive Data Detection & Compliance Assistant, follow these steps:
1. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.
2. Ensure you have the necessary dependencies installed, including `streamlit`, `pandas`, `pdfplumber`, and `python-dotenv`.
3. Clone the repository and navigate to the project directory.

## Architecture Overview
The Sensitive Data Detection & Compliance Assistant is built using Streamlit and consists of the following components:
* `app.py`: The main application file that handles user input and displays the results.
* `core/`: A directory containing the core functionality of the application, including:
	+ `detector.py`: Contains the sensitive data detection logic.
	+ `file_loader.py`: Contains the file loading logic.
	+ `patterns.py`: Contains the regular expression patterns for sensitive data detection.
	+ `risk_classifier.py`: Contains the risk classification logic.
	+ `summary.py`: Contains the compliance observation, security risk, and remediation step generation logic.
	+ `qa.py`: Contains the question answering logic.

## AI/ML Approach Used
The Sensitive Data Detection & Compliance Assistant uses a rule-based approach to detect sensitive data in uploaded files. The application utilizes regular expression patterns to identify various types of sensitive data, including Aadhaar, PAN, email, phone, credit card, IFSC, UPI, API keys, and employee IDs.

## Challenges Faced
The development of the Sensitive Data Detection & Compliance Assistant posed several challenges, including:
* Developing accurate regular expression patterns to detect sensitive data.
* Handling different file formats, such as PDF, TXT, and CSV.
* Classifying the overall document risk level based on the detected sensitive data types.
* Generating compliance observations, security risks, and suggested remediation steps.

## Future Improvements
To further improve the Sensitive Data Detection & Compliance Assistant, the following enhancements can be made:
* Integrating machine learning algorithms to improve the accuracy of sensitive data detection.
* Supporting additional file formats, such as DOCX and XLSX.
* Developing a more sophisticated risk classification system.
* Enhancing the user interface to provide a more intuitive user experience.

## Working Prototype Deployment Link
[https://sensitivedatadetection-hniecahjqb7icrqbrgyivm.streamlit.app/](https://sensitivedatadetection-hniecahjqb7icrqbrgyivm.streamlit.app/)
