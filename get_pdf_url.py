import requests
import sys

def get_latest_commit_sha(repo, branch='main'):
    url = f"https://api.github.com/repos/{repo}/commits/{branch}"
    response = requests.get(url)
    
    if response.status_code == 200:
        commit_sha = response.json().get('sha')
        if commit_sha:
            return commit_sha
        else:
            print("Commit SHA not found.", file=sys.stderr)
    else:
        print(f"Failed to fetch the latest commit. Status code: {response.status_code}", file=sys.stderr)

    sys.exit(1)

def get_pdf_url(latest_commit_hash: str) -> str:
    return f"https://raw.githubusercontent.com/jthaller/resume_url_hosting/{latest_commit_hash}/Jeremy_Thaller_Resume.pdf"


if __name__ == "__main__":
    repo = "jthaller/resume_url_hosting"
    latest_commit_hash = get_latest_commit_sha(repo)
    pdf_url = get_pdf_url(latest_commit_hash)
    print(pdf_url)  # Print the PDF URL to capture it in the GitHub Actions workflow
