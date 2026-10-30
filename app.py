
import streamlit as st
from phishing_checker import inspect_url

st.set_page_config(
    page_title="Phishing URL Awareness Checker",
    page_icon="🔐"
)

st.title("🔐 Phishing URL Awareness Checker")

st.write(
    "Check a URL for common phishing warning signs. "
    "This tool checks URL text only and does not visit websites."
)

url = st.text_input("Enter a website URL:")

if st.button("Check URL"):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        warnings = inspect_url(url)

        st.subheader("Security Results")

        if warnings:
            st.error("REVIEW CAREFULLY")

            for number, warning in enumerate(warnings, start=1):
                st.write(f"{number}. {warning}")
        else:
            st.success("No listed warning signs were detected.")

        st.info(
            "This tool cannot prove whether a website is safe "
            "or malicious. Always verify websites using trusted sources."
        )
