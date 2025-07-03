from flask import Flask, render_template
import requests

app = Flask(__name__)

# GitHub API endpoint for user repos
GITHUB_API_URL = "https://api.github.com/users/patw/repos"

@app.route('/')
def index():
    try:
        # Fetch repos from GitHub API
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        repos = response.json()
        
        # Sort repos by star count (descending)
        repos.sort(key=lambda r: r.get('stargazers_count', 0), reverse=True)
    except requests.exceptions.RequestException as e:
        repos = []
        print(f"Error fetching GitHub repos: {e}")
    
    return render_template('index.html', repos=repos)

if __name__ == '__main__':
    app.run(debug=True)
