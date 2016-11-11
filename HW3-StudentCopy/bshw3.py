# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
from bs4 import BeautifulSoup

url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# picture of myself
picture = 'my_pic.jpg'

# create an empty HTML file
f = open('index.html', 'w')

# converting text in soup into strings
pretty_soup = soup.prettify()

# replacing 'student' with 'AMAZING student'
pretty_soup = pretty_soup.replace('student', 'AMAZING student')

# replacing the main picture with a picture of myself
pretty_soup = pretty_soup.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', picture)

# replacing local image with image in media folder
pretty_soup = pretty_soup.replace('logo2.png', 'media\logo.png')

# write into HTML file
f.write(pretty_soup)