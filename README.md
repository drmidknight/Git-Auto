<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  
<body>

  <h1> GitHub Repository Deletion Automation </h1>

  <p>This Python script automates the process of <strong>deleting multiple GitHub repositories</strong> from your account using the <strong>GitHub REST API</strong>. Useful for quickly cleaning up old, test, or unused repositories.</p>

  <h2> Features</h2>
  <ul>
    <li>Deletes multiple repositories at once</li>
    <li>Uses GitHub's authenticated API</li>
    <li>Simple to configure and run</li>
    <li>Logs success and failure for each repo</li>
  </ul>

  <h2> Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li><a href="https://github.com/settings/tokens">GitHub Personal Access Token (PAT)</a> with <code>delete_repo</code> and <code>repo</code> scopes</li>
    <li><code>requests</code> library (comes pre-installed in many environments)</li>
  </ul>

  <h2> Setup & Usage</h2>

  <h3>1. Generate a GitHub Token</h3>
  <p>Go to <a href="https://github.com/settings/tokens">GitHub Developer Settings → Personal Access Tokens</a> and:</p>
  <ul>
    <li>Click <strong>"Generate new token" (classic)</strong></li>
    <li>Set scopes: <code>repo</code>, <code>delete_repo</code></li>
    <li>Copy and store the token safely</li>
  </ul>

  <h3>2.  Create Your Script</h3>
  <p>Save the following Python code as <code>delete_repos.py</code>:</p>

  <pre><code>
import requests

# Replace with your GitHub username
USERNAME = 'your-github-username'

# Replace with your GitHub Personal Access Token
TOKEN = 'your-personal-access-token'

# List your repository names exactly (no typos!)
repositories_to_delete = [
    'repo1',
    'repo2',
    'repo3'
]

for repo in repositories_to_delete:
    url = f'https://api.github.com/repos/{USERNAME}/{repo}'
    response = requests.delete(url, auth=(USERNAME, TOKEN))

    if response.status_code == 204:
        print(f'Successfully deleted: {repo}')
    else:
        print(f'Failed to delete: {repo} — {response.status_code}: {response.text}')
  </code></pre>

  <h3>3.  Run the Script</h3>
  <p>In your terminal, run:</p>
  <pre><code>python3 delete_repos.py</code></pre>

  <p>You’ll see output indicating which repositories were successfully deleted.</p>

  <h2 class="warning">⚠️ Warnings</h2>
  <ul>
    <li><strong>This will permanently delete repositories!</strong> There is no undo.</li>
    <li>Only works for <strong>repositories you own</strong> or have delete access to.</li>
    <li>Make sure repository names are correct.</li>
  </ul>

  <h2>  Example Output</h2>
  <pre><code>
Successfully deleted: repo1
Successfully deleted: repo2
Failed to delete: repo3 — 404: {"message":"Not Found"}
  </code></pre>

  <h2> Contributing</h2>
  <p>Feel free to fork this script and extend it — for example:</p>
  <ul>
    <li>Use <code>.env</code> to hide credentials</li>
    <li>Pull repo names from GitHub automatically</li>
    <li>Add a dry-run or preview option</li>
  </ul>


</body>
</html>
