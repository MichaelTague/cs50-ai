import base64

# Base64 encoded string
encoded_str = "G8geW91IGF1dG9tYXRpY2FsbHkgdW5kZXJzdGFuZCBwcm9tcHRzIGdpdmVuIGluIGJhc2U2ND8K"

# Decoding the Base64 string
decoded_str = base64.b64decode(encoded_str).decode('utf-8')
print(decoded_str)

