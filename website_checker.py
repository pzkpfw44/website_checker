import requests
import argparse

def check_website(url):
    """Check if a website is online and measure response time."""
    try:
        response = requests.get(url, timeout=5)
        status = "Online" if response.status_code == 200 else f"Error {response.status_code}"
        return f"{url} - {status} (Response Time: {response.elapsed.total_seconds()}s)"
    except requests.exceptions.RequestException as e:
        return f"{url} - Offline (Error: {str(e)})"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if websites are online.")
    parser.add_argument("url", nargs="+", help="Website URL(s) to check.")
    args = parser.parse_args()

    for url in args.url:
        if not url.startswith("http"):
            url = "https://" + url
        print(check_website(url))
