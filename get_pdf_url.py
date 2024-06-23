import requests
from bs4 import BeautifulSoup

def get_pdf_url(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the div tag with the class 'pdf-container loaded'
        div_tag = soup.find('div', class_='pdf-container loaded')
        if div_tag:
            # Extract the value of the data-file attribute
            pdf_url = div_tag.get('data-file')
            return pdf_url
        else:
            print("Div tag with class 'pdf-container loaded' not found.")
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")

# Example usage
url = "https://github.com/jthaller/resume_url_hosting/blob/main/Jeremy_Thaller_Resume.pdf"
pdf_url = get_pdf_url(url)

if pdf_url:
    print(f"The PDF URL is: {pdf_url}")
else:
    print("Failed to retrieve the PDF URL.")
