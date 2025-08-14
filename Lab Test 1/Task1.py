import re

def extract_urls(text):
    # Regex pattern to match URLs (http, https, www)
    url_pattern = r'(https://www.example.com)'
    urls = re.findall(url_pattern, text)
    return urls

# Example usage:
if __name__ == "__main__":
    sample_text = """
    Here are some links: https://www.example.com, http://test.org/page, and www.sample.net.
    Also, check out https://sub.domain.com/path?query=1.
    """
    found_urls = extract_urls(sample_text)
    print("Extracted URLs:", found_urls)
