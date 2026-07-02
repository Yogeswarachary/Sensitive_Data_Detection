import streamlit as st

from core.file_loader import read_file
from core.detector import detect_pii, aggregate_stats
from core.risk_classifier import classify_risk
from core.summary import build_compliance_summary
from core.qa import answer_question

st.title("Sensitive Data Detection & Compliance Assistant (Rule-based)")

uploaded_file = st.file_uploader(
    "Upload a file (PDF/TXT/CSV)",
    type=["pdf", "txt", "csv"]
)

if uploaded_file is not None:
    raw_text, df = read_file(uploaded_file)

    st.subheader("Raw Text (first 1000 characters)")
    st.text(raw_text[:1000])

    # PII detection
    findings = detect_pii(raw_text)
    stats = aggregate_stats(findings)

    st.subheader("Detected Sensitive Data (Findings)")
    if findings:
        st.write(f"Total findings: {len(findings)}")
        st.dataframe(findings)
    else:
        st.write("No sensitive data detected with current patterns.")

    st.subheader("Summary Counts by Type")
    st.json(stats)

    # Risk classification
    risk_info = classify_risk(findings)
    st.subheader("Risk Classification")
    st.write(f"Risk level: {risk_info['risk_level']}")
    st.write(f"Reason: {risk_info['reason']}")

    # Compliance & security summary
    summary = build_compliance_summary(findings, risk_info)

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

    if df is not None:
        st.subheader("CSV Preview")
        st.dataframe(df)

    # Q&A Section
    st.subheader("Ask Questions About This Document")

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