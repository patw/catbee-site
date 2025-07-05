import requests
from flask import Flask, render_template

app = Flask(__name__)

# GitHub API endpoint for user repos
GITHUB_API_URL = "https://api.github.com/users/patw/repos"

def fetch_all_repos():
    """Fetch all repositories from GitHub API with pagination"""
    all_repos = []
    current_url = GITHUB_API_URL

    for _ in range(3):  # Fetch up to 3 pages
        try:
            response = requests.get(current_url)
            response.raise_for_status()

            # Add the current page of results
            page_repos = response.json()
            all_repos.extend(page_repos)

            # Check if there are more pages
            if 'Link' in response.headers:
                link_header = response.headers['Link']
                # Find the "next" link
                next_link = None
                for link in link_header.split(','):
                    if 'rel="next"' in link:
                        next_link = link.split(';')[0].strip()[1:-1]
                        break

                if next_link:
                    current_url = next_link
                else:
                    break  # No more pages
            else:
                break  # No more pages

        except requests.exceptions.RequestException as e:
            print(f"Error fetching GitHub repos: {e}")
            break

    return all_repos

@app.route('/')
def index():
    try:
        # Fetch all repos (with pagination)
        repos = fetch_all_repos()

        # Sort repos by star count (descending)
        repos.sort(key=lambda r: r.get('stargazers_count', 0), reverse=True)
    except Exception as e:
        repos = []
        print(f"Error: {e}")

    return render_template('index.html', repos=repos)

if __name__ == '__main__':
    app.run(debug=True)
