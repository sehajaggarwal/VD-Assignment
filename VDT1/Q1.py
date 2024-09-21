#QUESTION 1 
#----------------

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to check if a link is for an article or not
def is_relevant_link(link, title):
    # Filter out media-related links or irrelevant sections
    if any(keyword in link.lower() for keyword in ['video', 'watch', 'media', 'live', 'logo', 'contact', 'about', 'privacy', 'terms', 'home', 'settings' 'newletters']) or \
       any(keyword in title.lower() for keyword in ['video', 'watch', 'media']):
        return False
    
    if any(keyword in link.lower() for keyword in ['news', 'article', '202', 'story']):
        return True
    
    return False

# Function to scrape latest article titles and URLs
def scrape_latest_articles(url):
    # Send a request to fetch the content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page with status code: {response.status_code}")
        return []
    
    # Parse the content
    parsed_content = BeautifulSoup(response.content, 'html.parser')
    
    # Find all anchor tags
    # Note: this is a general approach, and it needs to be adjusted based on webpage structure
    anchors = parsed_content.find_all('a')
    
    articles = []
    for anchor in anchors:
        #extract title and URL
        link = anchor.get('href')
        title = anchor.get_text().strip()
        
        # Ignore empty titles and irrelevant links
        if link and title and is_relevant_link(link, title):
            # Construct full URL if needed
            full_link = urljoin(url, link)  
            articles.append({'title': title, 'url': full_link})
    
    return articles


#Test the solution
if __name__ == "__main__":
    url="https://www.nbcnews.com"
    articles = scrape_latest_articles(url)

    # Display the results
    if articles:
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}")
            print("-"*50)
    else:
        print("No relevant articles found.")
