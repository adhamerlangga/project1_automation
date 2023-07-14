from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json

book1 = Book(
    'Title test',
    'Ini subject test',
    None,
    '1345-4533',
    'Adham',
    '081818118'
)

book2 = Book(
    'Title test',
    'Ini subject test',
    None,
    '1345-4533',
    'Erlangga',
    '081818118'
)

book3 = Book(
    'Title test',
    'Ini subject test',
    None,
    '1345-4533',
    'Siwi',
    '081818118'
)
magazine1 = Magazine(
    'media cnn test',
    'edisi 14 july 2023',
    None,
    'volume 1',
    '-'
)

magazine2 = Magazine(
    'media cnbc',
    'edisi 14 july 2023',
    None,
    'volume 2',
    '-'
)

dvd1 = Dvd(
    'test dvd 1',
    'edisi 14 july 2023',
    None,
    'tom hanks',
    'kylian murphy',
    'action'
)



# collect data  per jenis
book = [book1,book2,book3]
magazine = [magazine1,magazine2]
dvd = [dvd1]
cd = []

# get data from json
f = open('files/catalog.json')
data_json = json.load(f)

# create object from data json

for item in data_json:
    if item["source"] == "book":
        book.append(Book(
            title = item['title'], 
            subject = item['subject'], 
            upc = item['upc'], 
            issbn = item['issbn'], 
            authors = item['authors'], 
            dds_number = item['dds_number']))
        
    elif item["source"] == "cd":
        cd.append(Cd(
            title = item['title'], 
            subject = item['subject'], 
            upc = item['upc'], 
            artist = item['artist']))
    # elif ...

# collect all data
catalog_all = [book, magazine, dvd, cd]

# run search & result
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result}')