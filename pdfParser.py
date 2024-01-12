# -*- coding: utf-8 -*-
"""

This code defines a class named pdfPrser that is responsible for parsing and extracting information from PDF documents. Let's go through the code step by step:

1. The code starts by importing necessary modules (tika.parser, string, re, os.path).

2. The pdfPrser class is defined.

3. The get_stop_words method is defined. It reads a file called stopwords.txt located in the same directory as the script and returns a list of stop words. Stop words are common words that are often filtered out in natural language processing tasks.

4. The class defines several class-level variables:

   => am_sent_endings: A regular expression pattern representing sentence endings in Amharic language. It includes question marks, exclamation marks, period (።), and double space (፡፡).
   => am_punctuation: A string containing various punctuation marks in Amharic.
   => am_numbers: A string containing Amharic numerals.
   => am_random: A string containing random characters specific to Amharic language.
   => stop_words: A list of stop words obtained by calling the get_stop_words method.
5. The __init__ method is the class constructor. It takes a pdf_path parameter representing the path to the PDF file. It initializes instance variables pdf_path, raw_text, clean_text, sentences, and words. It then calls the parse method to extract the necessary information from the PDF file.

6. The parse method takes a path parameter representing the path to the PDF file. It uses the parser.from_file function from the tika.parser module to extract the raw text content of the PDF file. It then cleans the raw text by removing duplicate spaces and returns. The clean text is stored in the clean_text instance variable. The method also calls the extract_sentences and extract_words methods to extract sentences and words from the clean text, respectively. The resulting sentences and words are stored in the sentences and words instance variables.

7. The extract_sentences method takes an optional text parameter and generates a list of sentences by splitting the text using the am_sent_endings regular expression pattern. If no text parameter is provided, it uses the raw_text instance variable as the input. The method returns the list of sentences.

8. The extract_words method takes a text parameter and generates a list of words by splitting the text using white space as the delimiter. The method returns the list of words.

9. The clean method takes a text parameter and performs text cleaning by removing punctuation marks, numbers, random characters, and other unwanted symbols from the text. It uses the string.punctuation constant and the class-level variables (am_numbers, am_random, am_punctuation) to define the characters to be cleaned. The method returns the cleaned text as a list of words.

10. The clean_minimized method is similar to the clean method, but it handles the cleaning process in a more minimized way. It removes punctuation marks, numbers, random characters, and sentence endings specified by the am_sent_endings pattern. It returns the cleaned text as a string.

11. The remove_duplicate_sentence method takes a list of sentences and removes any duplicates from it. It iterates over the sentences, checks if each sentence is already in a list called cleaned, and if not, adds it to cleaned. If a sentence is already in cleaned, it checks if it's already in another list called duplicates. If not, it adds it to duplicates. The method returns the cleaned list, which contains the sentences without duplicates.

12. The __main__ block is the entry point of the script. It creates an instance of the pdfPrser class (pd_parser) without specifying a PDF file path. It then prints the words attribute of the pd_parser instance, which contains the list of words extracted from the PDF document
"""

from tika import parser
import string
import re

import os.path

class pdfPrser:

    def get_stop_words():
        return  open(os.path.dirname(__file__) + '/data/stopwords.txt', encoding='utf-8').read().split()


    # init method or constructor 
    am_sent_endings = r'\?|\!|\።|\፡፡'#".|?|!|።"
    am_punctuation = '፠፡።፣፤፥፦፧፨“”‘’…‹‹››·•'
    am_numbers = '፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻፼'
    am_random = '�©\uf0c4\uf0d8\uf0a7\uf066\uf0d8' 
    stop_words = get_stop_words()

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.raw_text = None
        self.clean_text = None
        self.sentences = None
        self.words = None

        self.parse(pdf_path)


    #reading old pdf files with non-unicode fonts has been imposible 
    def parse(self, path):
        self.raw_text = parser.from_file(path)['content']
        #remove duplicated spaces and return
        #return " ".join(raw['content'].split())
        self.clean_text = self.clean_minimized(self.raw_text)
        self.sentences = self.extract_sentences(self.clean_text)
        #remove duplicates
        self.sentences = self.remove_duplicate_sentence(self.sentences)
        self.words = self.extract_words(self.clean_text)


    def extract_sentences(self, text=None):
        '''generates a list of sentences'''
        if text == None: text=self.raw_text
        sentences = re.split(self.am_sent_endings,text)
        return sentences
    
    def extract_words(self, text):
        '''generates a list of words'''    
        return text.split()

    def clean(self, text):
        # split into words by white space
        words = text.split()   
        to_clean = string.punctuation + self.am_numbers + self.am_random + string.ascii_letters + string.digits + self.am_punctuation    
        table = str.maketrans('', '', to_clean)
        stripped = [w.translate(table) for w in words]
        #remove empty strings from list
        clean_txt = list(filter(None, stripped))
        return clean_txt

    def clean_minimized(self, text):
        # split into words by white space
        words = text.split()   
        to_clean = string.punctuation + self.am_numbers + self.am_random + string.ascii_letters + string.digits + self.am_punctuation
        to_clean = re.sub(self.am_sent_endings,'',to_clean)
        table = str.maketrans('', '', to_clean)
        stripped = [w.translate(table) for w in words]
        #remove empty strings from list
        clean_txt = list(filter(None, stripped))
        return ' '.join(clean_txt)
    
    def remove_duplicate_sentence(self,sentences):
        duplicates = []
        cleaned = []
        for s in sentences:
            if s in cleaned:
                if s in duplicates:
                    continue
                else:
                    duplicates.append(s)
            else:
                cleaned.append(s)
        return cleaned

#Test
if __name__ == '__main__':
    pd_parser = pdfPrser('')
    print(pd_parser.words)
