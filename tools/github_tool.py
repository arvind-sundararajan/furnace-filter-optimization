```json
{
    "tools/github_tool.py": {
        "content": "
import logging
from typing import Dict, List
from smolagents import ToolCallingAgent
from agentops import AgentOpsAPI
import os
import requests
from requests.exceptions import RequestException

class GitHubTool:
    """
    A tool for interacting with the GitHub API.
    """

    def __init__(self, api_key: str):
        """
        Initialize the GitHub tool.

        Args:
        - api_key (str): The API key for the GitHub API.
        """
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)

    def get_repository(self, repository_name: str) -> Dict:
        """
        Get a repository from GitHub.

        Args:
        - repository_name (str): The name of the repository.

        Returns:
        - Dict: The repository data.
        """
        try:
            self.logger.info(f'Getting repository {repository_name}')
            response = requests.get(f'https://api.github.com/repos/{repository_name}', headers={'Authorization': f'token {self.api_key}'})
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            self.logger.error(f'Error getting repository {repository_name}: {e}')
            return {}

    def get_commit_history(self, repository_name: str) -> List:
        """
        Get the commit history of a repository.

        Args:
        - repository_name (str): The name of the repository.

        Returns:
        - List: The commit history.
        """
        try:
            self.logger.info(f'Getting commit history for {repository_name}')
            response = requests.get(f'https://api.github.com/repos/{repository_name}/commits', headers={'Authorization': f'token {self.api_key}'})
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            self.logger.error(f'Error getting commit history for {repository_name}: {e}')
            return []

    def create_issue(self, repository_name: str, title: str, body: str) -> Dict:
        """
        Create a new issue in a repository.

        Args:
        - repository_name (str): The name of the repository.
        - title (str): The title of the issue.
        - body (str): The body of the issue.

        Returns:
        - Dict: The issue data.
        """
        try:
            self.logger.info(f'Creating issue in {repository_name} with title {title} and body {body}')
            response = requests.post(f'https://api.github.com/repos/{repository_name}/issues', headers={'Authorization': f'token {self.api_key}'}, json={'title': title, 'body': body})
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            self.logger.error(f'Error creating issue in {repository_name}: {e}')
            return {}

def main():
    # Load the API key from the environment
    api_key = os.environ['AGENTOPS_API_KEY']

    # Create a new GitHub tool
    github_tool = GitHubTool(api_key)

    # Get a repository
    repository_name = 'smolagents/agentops'
    repository = github_tool.get_repository(repository_name)
    print(repository)

    # Get the commit history
    commit_history = github_tool.get_commit_history(repository_name)
    print(commit_history)

    # Create a new issue
    title = 'Test issue'
    body = 'This is a test issue'
    issue = github_tool.create_issue(repository_name, title, body)
    print(issue)

if __name__ == '__main__':
    main()
",
        "commit_message": "feat: implement specialized github_tool logic"
    }
}
```