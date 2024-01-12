"""
This code performs text summarization on a PDF document. Let's analyze it step by step:

1. The code starts by importing necessary modules: fasttext, os, pathlib, numpy, pdfParser, extraction_summary, and cosine_similarity.

2. It defines a variable output_path that represents the output directory path where the generated text files will be saved.

3. The detect_language function is defined. It takes a text parameter and uses the fasttext library to predict the language of the text. It loads a pre-trained language identification model (lid.176.ftz) and uses it to predict the language of the text. It returns the predicted language code.

4. The save_text_file function is defined. It takes a file_name and text as parameters and saves the provided text to a text file with the given file_name in the output_path directory.

5. The __main__ block is the entry point of the script. It opens a log file (log.log) in append mode to log any important information or errors.

6. The variable book_url is set to the URL of a PDF document to be summarized. This URL points to a document named "on-hibret1.pdf" hosted on a website.

7. An instance of the pdfPrser class (pparser) is created using the book_url. This class is defined in the pdfParser module and is responsible for parsing and extracting information from PDF documents.

8. The detect_language function is called with the pparser.clean_text as the input. It predicts the language of the text extracted from the PDF document.

9. If the predicted language (lang) is 'am' (Amharic), the summarization process begins.


10. The extraction summary is generated using the _get_summary function from the extraction_summary module. The pparser instance and a hyperparameter value of 1.5 are passed as arguments. The extraction summary represents a summary of the document based on important sentences extracted from the document.

11. The extracted summary is stored in the ext_summary variable.



12. The cosine summary is generated using the build_summary function from the cosine_similarity module. The pparser.sentences (which contains the sentences extracted from the document) and pparser.stop_words (a list of stop words) are passed as arguments. The cosine summary represents a summary of the document based on the similarity of sentences.

13. The cosine summary is stored in the cos_summary variable.

14. The save_text_file function is called to save the cos_summary to a text file named "cosine_summary.txt" in the output_path directory.

15. At this point, the code ends for the Amharic language case. If the language is not 'am', a log message is written to the log file indicating that the language is not supported for the provided URL.


"""

import fasttext
import os
from pathlib import Path

from numpy import cos
import pdfParser as pp
import extraction_summary
import cosine_similarity


output_path = os.path.dirname(Path(__file__)) + '/out/'

def detect_language(text):
    model = fasttext.load_model(os.path.dirname(Path(__file__)) + '/fastText/lid.176.ftz')
    return model.predict(text, k=1)[0][0][-2:]

def save_text_file(file_name, text):
    with open(output_path + file_name, "w+",encoding="utf-8") as text_file:
        text_file.write(text)


if __name__ == "__main__":    

#read pdf
#detect language, if 'am' Continue

#make extraction summary, save text
#make cosine summary, save text
#make abstract summary, save text
#update db and continue
    logf = open("out/log.log", "a+")
    
    book_url = 'https://amnewsupdate.files.wordpress.com/2015/06/on-hibret1.pdf'
    pparser = pp.pdfPrser(book_url)
    lang = detect_language(pparser.clean_text)
    if  lang == 'am':
        print('Summarizing...')
        
       
        #extraction
        print('Extraction summary...')
        hyper_param = 1.5
        ext_summary = extraction_summary._get_summary(pparser,hyper_param)
        # save_text_file('extraction_summary.txt',ext_summary)        
        #cosine summary
        print('Cosine summary...')
        cos_summary = cosine_similarity.build_summary(pparser.sentences,pparser.stop_words)
        save_text_file('cosine_summary.txt',cos_summary)
        #abstract summary
        #TODO
    else:
        logf.write('language not supported: {0}: {1}\n '.format(book_url, lang))

    print('The End')