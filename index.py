from __future__ import unicode_literals

import xml.etree.ElementTree as Xet
import pandas as pd
import os
from hazm import *


cols = ["category", "text"]
rows = []

# Parsing the XML file
xml_files = [file for file in os.listdir('./Corpus_Clear') if file.endswith('.xml')]
xml_files.sort()
for file in xml_files:
    print(f'File {file} is being processed')
    xml_parse = Xet.parse(f'./Corpus_Clear/{file}')
    root = xml_parse.getroot()
    for i in root:
        # print(i.tag)
        if i.tag == 'DOC':
            category = i.find("CAT").text
            category = category.replace(' ', '')
            if category == 'اجتماعی' or category == 'اجتماعی.معارف':
                category = 0
            if category == 'ادبوهنر' or category == 'ادبوهنر.ادبیات' or category == 'ادبوهنر.هنر' or \
                    category == 'ادبوهنر.هنر.تئاتر' or category == 'ادبوهنر.هنر.سینما' or \
                    category == 'ادبوهنر.هنر.موسیقی':
                category = 1
            if category == 'اقتصاد' or category == 'اقتصاد.بورسوبانک':
                category = 2
            if category == 'سیاسی' or category == 'سیاسی.سیاستداخلی':
                category = 3
            if category == 'علمیفرهنگی' or category == 'علمیفرهنگی.علمی' or \
                    category == 'علمیفرهنگی.علمی.ارتباطاتوفناوریاطلاعات' or \
                    category == 'علمیفرهنگی.علمی.پزشکیودرمان' or category == 'علمیفرهنگی.علمی.کتاب':
                category = 4
            if category == 'ورزش':
                category = 5
            if category == 'گردشگری':
                category = 6
            if category == 'گوناگون' or category == 'گوناگون.حوادث' or category == 'گوناگون.خارجی' or \
                    category == 'گوناگون.شهری':
                category = 7

            text = i.find("TEXT").text
            text = text.replace('\n', '')

            # clearing text from stopwords
            with open('persian.stop.txt', 'r') as f:
                stopwords = f.read().splitlines()
                tokenized = word_tokenize(text)

                for word in tokenized:
                    if word in stopwords:
                        text = text.replace(word, '')

            rows.append({"category": category,
                         "text": text,
                         })

    df = pd.DataFrame(rows, columns=cols)

    df.to_csv(f'./Corpus_CSV/FinalData.csv', index=False)


# text = "من علی هستم اصغر اجماع کلی [] . : برای تست"
# with open('persian.stop.txt', 'r') as f:
#     stopwords = f.read().splitlines()
#
#     tokenized = word_tokenize(text)
#
#     for word in tokenized:
#         if word in stopwords:
#             print(word)
#             text = text.replace(word, '')
#     print(text)
