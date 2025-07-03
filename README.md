# Catbee Projects Website

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Flask web application that displays GitHub repositories in a card-based layout. This project showcases open source repositories from the Catbee organization in an attractive, responsive interface.

## Features

- Fetches repository data directly from GitHub API
- Responsive card layout using Bootstrap 5
- Language-specific color coding
- Sort by star count
- Clean, modern design with hover effects

## Screenshot

![Screenshot](static/catbee-logo.png)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/patw/catbee-projects.git
cd catbee-projects
```

2. Install dependencies:
```bash
pip install flask requests
```

3. Run the application:
```bash
python app.py
```

## Configuration

The application is configured to fetch repositories from `https://api.github.com/users/patw/repos` by default. To change this:

1. Edit `app.py` and modify the `GITHUB_API_URL` variable
2. For private repositories, you'll need to add GitHub authentication

## Customization

You can customize the look and feel by editing:

- `templates/index.html` - Main page layout and styling
- `static/` - For adding custom CSS/JS/images

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Bootstrap 5](https://getbootstrap.com/) for responsive design
- [GitHub API](https://docs.github.com/en/rest) for repository data
