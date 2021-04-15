########################################################################################
########################################################################################
##
## DATA PRE PROCESSING TECHNIQUES
##
########################################################################################
########################################################################################
import os
import string
import time
from io import StringIO

import folderstats
from bs4 import BeautifulSoup
from tika import parser

millis = lambda: int(round(time.time() * 1000))


class DataPreProcessingTechniques:

    def __init__(self, stop_list=""):
        self.stop_list = stop_list

    ########################################################################################
    ## REMOVE STOP WORDS
    ## input: content that stop words not removed
    ## output: content that stop words removed
    ########################################################################################
    def remove_stop_words(self, text):
        clean_text = []
        stop_list = self.stop_list
        for word in text.split(' '):
            if word not in stop_list and (len(word) > 2):
                clean_text.append(word)

        return ' '.join(clean_text)

    ########################################################################################
    ## LEMMATIZER
    ## input: content that not lemmatized
    ## output: content that lemmatized
    ########################################################################################
    def lemmatizer(self, text):
        import spacy
        nlp = spacy.load('en')

        sent = []
        doc = nlp(text)
        for word in doc:
            wl = word.lemma_
            sent.append(wl)
        return " ".join(sent)

    ########################################################################################
    ## STEMMING
    ## input: content that not stemmed
    ## output: content that stemmed
    ########################################################################################
    def stemming(self, text):
        from nltk.stem.porter import PorterStemmer
        stemmer = PorterStemmer()

        word_list = []
        for word in text.split(' '):
            sw = stemmer.stem(word)
            word_list.append(sw)
        return ' '.join(word_list)

    ########################################################################################
    ## TIKA PDF EXTRACTION
    ## input: PDF Files
    ## output: Parsed Text in .pkl
    ########################################################################################

    def find_data_files(self, directory):
        df = folderstats.folderstats(directory, ignore_hidden=True)
        df_files = df[df['folder'] == False]
        df_pdf_files = df_files[df_files['extension'] == 'pdf']
        df_pdf_files_in_depth_1 = df_pdf_files[df_pdf_files['depth'] == 1]

        return df_pdf_files_in_depth_1['path']

    def reorder_columns(self, dataframe):
        cols = list(dataframe.columns.values)
        page_cols = [k for k in cols if k.startswith('page_')]
        cols.remove('file_path')
        cols.remove('total_page_count')

        meta_cols = list(set(cols) - set(page_cols))

        dataframe[['file_path', 'total_page_count'] + cols + meta_cols].head()
        return dataframe

    def word_count(self, text):
        return sum([i.strip(string.punctuation).isalpha() for i in text.split()])

    # Extracting plain text page by page: https://github.com/chrismattmann/tika-python/issues/191
    # Tika example usage and Metadata extraction: https://cbrownley.wordpress.com/2016/06/26/parsing-pdfs-in-python-with-tika/
    def tika_extract_pages(self, pages_txt, data, max_page_count):
        xhtml_data = BeautifulSoup(data['content'])
        all_data = xhtml_data.find_all('div', attrs={'class': 'page'})
        pages_txt['total_page_count'] = len(all_data)
        for i, content in enumerate(all_data):
            page = i + 1
            # Parse PDF data using TIKA (xml/html)
            # It's faster and safer to create a new buffer than truncating it
            # https://stackoverflow.com/questions/4330812/how-do-i-clear-a-stringio-object
            _buffer = StringIO()
            _buffer.write(str(content))
            parsed_content = parser.from_buffer(_buffer.getvalue())

            # Add pages
            text = parsed_content['content'].strip() if parsed_content['content'] else ''
            pages_txt['page_' + str(page)] = text
            pages_txt['page_' + str(page) + '_wc'] = self.word_count(text)

            # Stop if a limit is defined!
            if max_page_count is not None and page is max_page_count:
                break

    def tika_parser(self, file_path, max_page_count=None):
        current_time = millis()
        print("Start to process {} at {}...".format(file_path, current_time), end='')
        pages_txt = {}
        pages_txt['file_path'] = file_path

        # Read PDF file
        data = parser.from_file(file_path, xmlContent=True)

        # Extract pages
        self.tika_extract_pages(pages_txt, data, max_page_count)

        # Extract Metadata

        pages_txt.update(data['metadata'])

        print("then it is processed in {} milliseconds".format(millis() - current_time))
        return pages_txt
