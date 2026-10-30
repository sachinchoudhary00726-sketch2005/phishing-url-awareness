# Phishing URL Awareness Checker - Test Samples

## Project Information

- **Project Name:** EWB Phishing URL Awareness Checker
- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Operating System:** Windows
- **Python Version:** Enter your installed Python version
- **Testing Date:** 30 October 2026

## Test 1: URL Containing @ Symbol

**Input:** `https://example.com@fake.com`

**Expected Result:**
- URL contains an @ symbol.

**Actual Result:** Passed.

**Status:** PASS

## Test 2: Long URL

**Input:** `https://example.com/this/is/a/very/long/example/path/for/testing/the/project/url/checker`

**Expected Result:**
- URL is unusually long (over 100 characters).

**Actual Result:** Passed.

**Status:** PASS

## Test 3: IP Address

**Input:** `http://192.168.1.1/login`

**Expected Result:**
- URL uses an IP address instead of a domain name.
- URL uses HTTP instead of HTTPS.

**Actual Result:** Passed.

**Status:** PASS

## Test 4: Five or More Hostname Segments

**Input:** `http://a.b.c.d.example.com`

**Expected Result:**
- Hostname contains five or more segments.
- URL uses HTTP instead of HTTPS.

**Actual Result:** Passed.

**Status:** PASS

## Test 5: Punycode

**Input:** `http://xn--example-ova.com`

**Expected Result:**
- Hostname contains a Punycode segment (`xn--`).
- URL uses HTTP instead of HTTPS.

**Actual Result:** Passed.

**Status:** PASS

## Test 6: Normal URL

**Input:** `https://example.com`

**Expected Result:**
- No listed warning signs are detected.

**Actual Result:** Passed.

**Status:** PASS

## Test 7: Streamlit Web Application

**Input:** `http://192.0.2.10/account`

**Expected Result:**
- URL uses an IP address instead of a domain name.
- URL uses HTTP instead of HTTPS.
- Application displays the REVIEW CAREFULLY result.

**Actual Result:** Both warning signs and the REVIEW CAREFULLY result were displayed in the local Streamlit web application.

**Status:** PASS

## Testing Notes

1. The command-line application was tested using six sample URLs.
2. The Streamlit web application was tested locally using the sample IP address URL.
3. The application checks URL text only and does not visit or open websites.
4. The results are intended for educational phishing awareness and do not guarantee website safety.
