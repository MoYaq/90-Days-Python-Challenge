#Day 14: Working with APIs
#Project: Fetch GitHub User Profile, Profile README, Followers, and Following
#A program to demonstrate how to send requests to APIs and handle JSON responses.

#Step 1: Import the requests library to make API calls.
import requests

#Step 2: Define API endpoints
GITHUB_API_URL = "https://api.github.com/users/"
GITHUB_REPO_API_URL = "https://api.github.com/repos/"

#Step 3: Function to fetch GitHub user profile data
def get_github_user_data(username):
    """Fetches GitHub user profile data like name, bio, location, public repos, followers, and following."""
    try:
        url = f"{GITHUB_API_URL}{username}"
        response = requests.get(url)
        
#Check if the request is successful
        if response.status_code == 200:
            user_data = response.json()
            print(f"\n🔹 GitHub User Profile: {username} 🔹")
            print(f"👤 Name: {user_data.get('name', 'N/A')}")
            print(f"📄 Bio: {user_data.get('bio', 'N/A')}")
            print(f"📍 Location: {user_data.get('location', 'N/A')}")
            print(f"📂 Public Repos: {user_data.get('public_repos', 0)}")
            print(f"👥 Followers: {user_data.get('followers', 0)}")
            print(f"🔗 Following: {user_data.get('following', 0)}")
            print(f"🔗 GitHub Profile: {user_data.get('html_url')}")
        elif response.status_code == 404:
            print(f"\n❌ Error: GitHub user '{username}' not found.")
        else:
            print(f"\n⚠️ Error: Unable to fetch user data. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"🚨 Error: {err}")

#Step 4: Function to fetch GitHub profile README
def get_github_profile_readme(username):
    """Fetches the README file from a user's GitHub profile repository."""
    try:
        url = f"{GITHUB_REPO_API_URL}{username}/{username}/readme"
        headers = {"Accept": "application/vnd.github.v3.raw"} #Request raw README content

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            readme_content = response.text
            print(f"\n📜 GitHub Profile README for {username}:\n")
            print(readme_content[:3000]) #Print first 3000 characters for readability
        elif response.status_code == 404:
            print(f"\nℹ️ No profile README found for {username}. They may not have a profile repository.")
        else:
            print(f"\n⚠️ Error: Unable to fetch README. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"🚨 Error: {err}")

#Step 5: Main program execution
if __name__ == "__main__":
    print("🔍 Welcome to the GitHub Profile Info & README Fetcher! 🔍")

#Prompt user to enter a GitHub username
    username = input("Enter a GitHub username: ").strip()

#Fetch and display user profile data
    get_github_user_data(username)

#Fetch and display profile README if available
    get_github_profile_readme(username)
