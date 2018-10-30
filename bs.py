from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.cs.ucdavis.edu/people/faculty/areas/').text

soup = BeautifulSoup(source, 'lxml')

# narrowing down soup to the block/class of focus
researcher_block = soup.find('div', class_ = 'post-4258 page type-page status-publish hentry')

# set up csv columns for output
csv_file = open('frankWebScraper.csv', 'w')
file_writer = csv.writer(csv_file)
file_writer.writerow(['Name', 'Website', 'Title', 'Specialty'])


# loops to cut data
for p in researcher_block.find_all('p'):

    website = p.a['href']
    split_data = p.text.splitlines()

    try:
        name = split_data[0]
        name_title_split  = name.split(", ")
        title = "".join(name_title_split[1:])
        specialty = split_data[1]
    except:
        specialty = "No specialty listed"
    
    print("Name: ", name_title_split[0])
    print("Title: ", title)
    print("Website: ", website)
    print("Specialty: ", specialty)
    print()

    file_writer.writerow([name_title_split[0], title, website, specialty])

csv_file.close()



