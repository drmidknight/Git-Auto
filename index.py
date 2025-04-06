import requests

# Replace with your GitHub username
USERNAME = ''

# Replace with your GitHub Personal Access Token
TOKEN = ''

# List your repository names exactly (no typos!)
repositories_to_delete = [
    'Titanic-Boston-housing-dataset',
    'nextjs-course',
    'google-it-support',
    'profile',
    'json-server',
    'JavaScript-Guide'
    'Interview-questions',
    'netflix-web',
]

for repo in repositories_to_delete:
    url = f'https://api.github.com/repos/{USERNAME}/{repo}'
    response = requests.delete(url, auth=(USERNAME, TOKEN))

    if response.status_code == 204:
        print(f'Successfully deleted: {repo}')
    else:
        print(
            f'Failed to delete: {repo} — {response.status_code}: {response.text}')
