# Importing Libraries.
from bs4 import BeautifulSoup
import requests

# Instagram URL.
URL = 'https://www.instagram.com/{}/'

# Parse Function
def parse_data(s):

    # Creating a Dictionary.
    data = {}

    # Splitting the content.
    # Then taking first part.
    s = s.split("-")[0]

    # Again splitting the content.
    s = s.split(" ")

    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]

    # Returning the dictionary.
    return data

# Scrape Function
def scrape_data(username):

    # Getting the request from URL.
    r = requests.get(URL.format(username))

    # Converting the text.
    s = BeautifulSoup(r.text, "html.parser")

    # Finding meta info.
    meta = s.find("meta", property="og:description")

    # Calling parse method.
    return parse_data(meta.attrs['content'])

# Main Function.
if __name__ == "__main__":

    # username
    username = input("Enter Instagram Username: ")

    # Calling scrape function.
    data = scrape_data(username)

    # Printing the info.
    print("This Account has: ", data["Followers"], "followers")
    print("This Account has: ", data["Following"], "following")
    print("This Account has: ", data["Posts"], "posts")
