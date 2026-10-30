
# Phishing URL Awareness Checker

## Project Description

This is a Python-based cybersecurity project that checks website URLs for common phishing warning signs.

The user enters a website URL, and the program checks it for suspicious characteristics. It displays warning messages when it finds any of the six warning signs.

## Project Objectives

1. To understand phishing attacks.
2. To identify suspicious URL patterns.
3. To develop a URL checking program using Python.
4. To improve awareness about online security.

## Technologies Used

- Python
- Visual Studio Code
- urllib.parse library
- ipaddress library

## Features

The program checks six warning signs:

1. Presence of the @ symbol.
2. Unusually long URLs (more than 75 characters).
3. IP address instead of a domain name.
4. Five or more hostname segments.
5. Punycode domain containing xn--.
6. HTTP instead of HTTPS.

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

   python phishing_checker.py

5. Enter a website URL.
6. Read the results displayed by the program.

## Testing

The program was tested using six sample URLs. All six tests produced the expected results.

The test cases are available in tests/test_samples.md.

## Limitations

- The program uses basic URL checking rules.
- It does not use an online phishing database.
- It cannot prove whether a website is safe or malicious.
- A website without warning signs may still be dangerous.

## Conclusion

Through this project, I learned how to use Python to identify common phishing URL warning signs. I also improved my understanding of Python libraries, conditional statements, and cybersecurity awareness.
