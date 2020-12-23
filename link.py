import pyshorteners
link = input("Entre your URL")
s = pyshorteners.Shortener().tinyurl.short(link)
print("Your LINK ==>", s)