from bs4 import BeautifulSoup
import os

xml_files = [file for file in os.listdir('./Corpus') if file.endswith('.xml')]
xml_files.sort()
for file in xml_files:
    print(f'File {file} is being processed')
    soup = BeautifulSoup(open(f'./Corpus/{file}'), 'xml')
    for ext in soup.find_all('IMAGE'):
        print("-> Cleared")
        removed = ext.extract()

    output = open(f'./Corpus_Clear/{file}', 'w')
    output.write(str(soup))
    output.close()
