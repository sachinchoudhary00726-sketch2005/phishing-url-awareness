
# Phishing URL Awareness Checker - Test Samples

## Test 1: URL containing @ symbol

Input: https://example.com@fake.com

Expected Result: URL contains @ symbol.

Actual Result: Passed.

## Test 2: Long URL

Input: https://example.com/this/is/a/very/long/example/path/for/testing/the/project/url/checker

Expected Result: URL is unusually long.

Actual Result: Passed.

## Test 3: IP address

Input: http://192.168.1.1/login

Expected Result:
- URL uses an IP address instead of a domain name.
- URL uses HTTP instead of HTTPS.

Actual Result: Passed.

## Test 4: Five or more hostname segments

Input: http://a.b.c.d.example.com

Expected Result:
- Hostname contains five or more segments.
- URL uses HTTP instead of HTTPS.

Actual Result: Passed.

## Test 5: Punycode

Input: http://xn--example-ova.com

Expected Result:
- Hostname contains a Punycode segment.
- URL uses HTTP instead of HTTPS.

Actual Result: Passed.

## Test 6: Normal URL

Input: https://example.com

Expected Result: No warning signs detected.

Actual Result: Passed.
