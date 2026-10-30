
from urllib.parse import urlparse
import re


def inspect_url(raw_url):
    """
    Check a URL for common phishing warning signs.
    This program checks URL text only. It does not visit websites.
    """

    candidate = raw_url.strip()

    # Check whether the input is empty
    if not candidate:
        return ["Please enter a URL."]

    # Add HTTP if the user does not provide a scheme
    if "://" not in candidate:
        candidate = "http://" + candidate

    # Handle malformed URLs
    try:
        parsed_url = urlparse(candidate)
        hostname = parsed_url.hostname
    except ValueError:
        return ["Invalid or malformed URL."]

    # Check whether hostname exists
    if not hostname:
        return ["Invalid URL: hostname not found."]

    warnings = []

    # Check 1: @ symbol
    if "@" in candidate:
        warnings.append(
            "URL contains an @ symbol."
        )

    # Check 2: URL length greater than 100 characters
    if len(candidate) > 100:
        warnings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IPv4-looking hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
        warnings.append(
            "URL uses an IP address instead of a domain name."
        )

    # Check 4: Five or more hostname segments
    segments = hostname.split(".")
    if len(segments) >= 5:
        warnings.append(
            "Hostname contains five or more segments."
        )

    # Check 5: Punycode domain
    if "xn--" in hostname.lower():
        warnings.append(
            "Hostname contains a Punycode segment (xn--)."
        )

    # Check 6: HTTP instead of HTTPS
    if parsed_url.scheme.lower() == "http":
        warnings.append(
            "URL uses HTTP instead of HTTPS."
        )

    return warnings


def main():
    print("==========================================")
    print("       EWB PHISHING URL AWARENESS CHECKER")
    print("==========================================")

    print("\nThis tool checks URL text for common warning signs.")
    print("It does not open or visit websites.")
    print("Type q to quit the program.")

    # Improvement 1: Allow multiple URL checks
    while True:
        raw_url = input("\nEnter a website URL: ").strip()

        if raw_url.lower() == "q":
            print("\nThank you for using the checker.")
            break

        warnings = inspect_url(raw_url)

        print("\n==========================================")
        print("             SECURITY RESULTS")
        print("==========================================")

        if warnings:
            print("\nWarning signs detected:")

            for number, warning in enumerate(warnings, start=1):
                print(str(number) + ". " + warning)

            # Improvement 2: Clear review message
            print("\nResult: REVIEW CAREFULLY.")
            print("This URL contains warning signs.")

        else:
            print("\nNo listed warning signs were detected.")
            print("Result: No listed warning signs found.")

        print("\nImportant reminder:")
        print("This tool cannot prove whether a website is safe")
        print("or malicious. Always verify websites using")
        print("trusted official sources.")

        print("\n==========================================")


if __name__ == "__main__":
    main()
