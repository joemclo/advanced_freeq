#!/usr/bin/env python3


import os
import numpy as np
import pandas as pd
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

path_to_open = "./"

files = os.listdir(os.path.expanduser(path_to_open))
print(files)

word_list = pd.read_csv("./word_list.csv", names=["Word"])

df_master = word_list

for fileName in files:

    if not fileName.endswith(".pdf"):
        continue

    filePath = os.path.expanduser(path_to_open) + fileName

    output_filename = "%s_words.csv" % fileName

    if not os.path.exists(output_filename):

        def convert_pdf_to_txt(path):
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            codec = "utf-8"
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
            fp = open(path, "rb")
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0
            caching = True
            pagenos = set()
            for page in PDFPage.get_pages(
                fp,
                pagenos,
                maxpages=maxpages,
                password=password,
                caching=caching,
                check_extractable=False,
            ):
                interpreter.process_page(page)
            fp.close()
            device.close()
            str = retstr.getvalue()
            retstr.close()
            with open(".book.txt", "w") as book:
                book.write("%s" % str)

        convert_pdf_to_txt(filePath)
        os.system("./freeq.py -i .book.txt -o .book_freeq.csv")

        os.system("sed -i 's/^ *//g' .book_freeq.csv")
        os.system("sed -i 's/ /,/g' .book_freeq.csv")

        df_book = pd.read_csv(".book_freeq.csv", names=[fileName, "Word"])
        f = lambda x: len(str(x)) > 2
        df_book = df_book[df_book["Word"].apply(f)]

        print(word_list["Word"])

        df_freq = df_book[df_book["Word"].isin(word_list["Word"])]

        df_freq = df_freq.sort_values("Word")

        word = df_freq["Word"]
        df_freq.drop(labels=["Word"], axis=1, inplace=True)
        df_freq.insert(0, "Word", word)

        df_master = pd.merge(df_master, df_freq, how="outer", on="Word")

        print(df_master)

df_master = df_master.replace(np.NaN, 0)
df_master.to_csv("word_occurrences.csv", index=None)
