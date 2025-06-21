# from urllib.request import urlopen
# import json
# import csv
# from datetime import datetime


# #Open the URL
# url = "http://olympus.realpython.org/profiles/aphrodite"
# webPage = urlopen(url)


# # Read the page data
# # Use uft-8 coding
# htmlRawData = webPage.read()
# htmlData = htmlRawData.decode("utf-8")
# # UTF-8 is a character encoding standard used to represent Unicode 
# # characters as a sequence of 1 to 4 bytes

# # Extact the text 
# # Find the title tag index and length to extract it 

# titleIndex = htmlData.find("<title>")
# startIndex = titleIndex + len("<title>")
# endIndex = htmlData.find("</title>")
# title = htmlData[startIndex:endIndex]

# print(title)


n = 5
formula = 0

for i in range(n):
  if( i == 0):
    formula += 0
  elif (i == 1 or i == 2):
    formula += 1
  else:
    formula += (formula - (i - 1)) + (formula - (i - 2))


print(formula)
# print(0-1)
