#Day 16: Web Scraping with BeautifulSoup
#Project: Scraping News Headlines from a Website
#A project to demonstrate how to extract and display website data using BeautifulSoup.

#Step 1: Import required libraries
import requests
from bs4 import BeautifulSoup  

#Step 2: Define a function to fetch and parse the webpage
def scrape_news(url):
#Step 3: Send a request to the website
    response = requests.get(url)  

#Step 4: Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Unable to fetch page. Status Code: {response.status_code}")
        return

#Step 5: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")  

#Step 6: Find and extract the headlines (modify based on website structure)
    headlines = soup.find_all("h2")  #Change the tag if needed (e.g., <h3>, <a>, etc.)

#Step 7: Display the extracted headlines
    print("\nLatest News Headlines:")
    for index, headline in enumerate(headlines[:10], start=1):  # Display only first 10 headlines
        print(f"{index}. {headline.get_text(strip=True)}")  

#Step 8: Define the main function to run the scraper
if __name__ == "__main__":
    news_url = "https://www.bbc.com/news"  #Example: BBC News website
    scrape_news(news_url)  