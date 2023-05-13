import pyshorteners
url = input("Enter your URL : ")
#author prabhas
def shorteningURL(url):
    p = pyshorteners.Shortener()
    print(p.tinyurl.short(url))
shorteningURL(url)
