import requests
from bs4 import BeautifulSoup
import json

def get_dynamic_pdf_url(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the script tag with the specified data-target attribute
        script_tag = soup.find('script', {'data-target': 'react-app.embeddedData'})
        if script_tag:
            # Extract the content of the script tag
            script_content = script_tag.string

            # Parse the JSON content
            try:
                json_data = json.loads(script_content)
                
                # Extract the PDF URL from the JSON
                pdf_url = json_data['payload']['fileTree']['']['items'][2]['path']
                return f"https://github.com/jthaller/resume_url_hosting/raw/main/{pdf_url}"
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON: {e}")
        else:
            print("Script tag with data-target 'react-app.embeddedData' not found.")
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")

# Example usage
url = "view-source:https://github.com/jthaller/resume_url_hosting/blob/main/Jeremy_Thaller_Resume.pdf"
dynamic_pdf_url = get_dynamic_pdf_url(url)

if dynamic_pdf_url:
    print(f"The dynamic PDF URL is: {dynamic_pdf_url}")
else:
    print("Failed to retrieve the dynamic PDF URL.")
