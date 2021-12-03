#
# README.py - read the apps.csv file for apps on Google Play 
#

fileobj = open("apps.csv", "r")
data = fileobj.readlines()
fileobj.close()

app = []
category = []
rating = []
reviews = []
installs = []
price = []

for line in data: 
    splitline = line.strip().split(',')
    if len(splitline) == 1: 
        continue 
    app.append(splitline[0])
    category.append(splitline[1])
    rating.append(splitline[2])
    reviews.append(splitline[3])
    installs.append(splitline[4])
    price.append(splitline[5])


