import requests
from bs4 import BeautifulSoup

# make a request to the site and get it as a string
markup = requests.get(f'https://reach24.net/public_events/UnVSBUINPi1N75dp3cHxIA==').text

# pass the string to a BeatifulSoup object
soup = BeautifulSoup(markup, 'html.parser')

scrappedData = []

def driverSectionScrapper():
    tableOne = soup.find_all('div', attrs = {'class':'row flexi-row'})[1]

    driver = {}
    driverRowData = tableOne.find_all('div', class_="flexi-div")

    for label in driverRowData:
        driver[label.find('label', class_="info-label").get_text().replace("\n","").replace(":","")] = label.find('p', class_="info-value").get_text().replace("\n","").replace("\xa0","")
    scrappedData.append(driver)
driverSectionScrapper()


def eventSectionScrapper():
    tableTwo = soup.find_all('div', attrs = {'class':'row flexi-row'})[2]

    event = {}
    rowData = tableTwo.find_all('div', class_="flexi-div")

    for label in rowData:
        event[label.find('label', class_="info-label").get_text().replace("\n","").replace(":","")] = label.find('p', class_="info-value").get_text().replace("\n","").replace("\xa0","")

    scrappedData.append(event)
eventSectionScrapper()


def billingSectionScrapper():
    tableThree = soup.find_all('div', attrs = {'class':'row flexi-row'})[3]
    # print(tableThree.prettify())

    billing = {}
    rowData = tableThree.find_all('div', class_="flexi-div")

    for label in rowData:
        billing[label.find('label', class_="info-label").get_text().replace("\n","").replace(":","")] = label.find('p', class_="info-value").get_text().replace("\n","").replace("\xa0","")

    scrappedData.append(billing)
billingSectionScrapper()



def serviceLineItemsFirstSection():
    # Wheels, lugs and rims 1
    tableFour = soup.find('div', attrs = {'class':'show_service_line_items'})
    tableFour = soup.select('#service_line_items .panel .panel-body .col-md-12 .col-sm-6 .control-label')
    tableFour = soup.select('#service_line_items .panel .panel-body .col-md-12 .col-sm-6 .info')
    tableFour = soup.select('#service_line_items .panel .panel-body .col-md-12 .col-sm-6')
    tableFour = soup.find('div', attrs = {'id':'service_line_items'}).find_all('div', attrs = {'class':'panel'})

    service_line_items_one = {}
    rowData = tableThree.find_all('div', class_="flexi-div")

    firstRow = tableFour[0].find('div', attrs = {'class': 'panel-body'}).find('div', attrs = {'class': 'col-md-12'}).find_all('label', attrs = {'class': 'control-label'})
    secondRow = tableFour[0].find('div', attrs = {'class': 'panel-body'}).find('div', attrs = {'class': 'col-md-12'}).find_all('p', attrs = {'class': 'info'})

    for idx,label in enumerate(firstRow):
        if idx==3:
            print()
        else:
            service_line_items_one[label.get_text().replace("\n","")] = secondRow[idx].get_text().replace("\n","")

    scrappedData.append(service_line_items_one)
serviceLineItemsFirstSection()


tableFour = soup.find('div', attrs = {'id':'service_line_items'}).find_all('div', attrs = {'class':'panel'})
secondRowWheelsTable = tableFour[0].find('div', attrs = {'class': 'panel-body'}).find_all('div', attrs = {'class': 'col-md-12'})[1]

rowData = secondRowWheelsTable.find_all('div', class_="col-sm-4")

for idx,label in enumerate(rowData):
    valueTableTitleWheelOne = label.find_all('label', attrs = {'class': 'control-label'})
    valueTableDataWheelOne = label.find_all('p', attrs = {'class': 'info'})
 
    for val in valueTableTitleWheelOne:
        service_line_items_one[val.get_text().replace("\n","")] = ''


print(scrappedData)
