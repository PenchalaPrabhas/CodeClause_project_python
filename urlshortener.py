import pyshorteners
url = input("Enter your URL : ")
#function to shorten the URL
def shorteningURL(url):
    p = pyshorteners.Shortener()
    print(p.tinyurl.short(url))
shorteningURL(url)
