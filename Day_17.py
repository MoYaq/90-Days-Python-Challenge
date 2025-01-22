#Day 17: HTML and HTTP Basics
#Project: Build a simple HTTP Request Handler
# A project to demonstrate how to fetch and display webpage content using Python.

#Step 1: Import required library
import requests  

#Step 2: Define a function to fetch webpage content
def fetch_webpage(url):
    print(f"\nFetching content from: {url}\n")

    try:
#Step 3: Send an HTTP GET request
        response = requests.get(url)  

#Step 4: Check if the request was successful
        if response.status_code == 200:
            print("Successfully fetched the webpage!\n")
            print("Page Content (First 500 characters):\n")
            print(response.text[:500])  # Display first 500 characters
        else:
            print(f"Error: Unable to fetch the page. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

#Step 5: Define the main function
if __name__ == "__main__":
    print("Welcome to the HTTP Request Handler!\n")
    
#Step 6: User inputs a URL to fetch
    user_url = input("Enter a website URL (e.g., https://www.example.com): ").strip()
    
#Step 7: Fetch and display webpage content
    fetch_webpage(user_url)