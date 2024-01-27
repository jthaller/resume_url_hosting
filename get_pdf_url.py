import requests
from bs4 import BeautifulSoup

def get_dynamic_pdf_url(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the div with class 'pdf-container' and get the 'data-file' attribute
        pdf_container = soup.find('div', class_='pdf-container')
        if pdf_container:
            dynamic_pdf_url = pdf_container.get('data-file')
            return dynamic_pdf_url
        else:
            print("PDF container not found on the page.")
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")

url = 'https://github.com/jthaller/resume_url_hosting/blob/main/Jeremy_Thaller_Resume.pdf'
dynamic_pdf_url = get_dynamic_pdf_url(url)

if dynamic_pdf_url:
    print(f"The dynamic PDF URL is: {dynamic_pdf_url}")
else:
    print("Failed to retrieve the dynamic PDF URL.")
