"""

This code implements a document summarization algorithm using the TF-IDF (Term Frequency-Inverse Document Frequency) approach. Let's break down the code step by step:

1. The code begins by importing necessary libraries and modules, 
such as NLTK (Natural Language Toolkit), NumPy, Pandas, scikit-learn, and Matplotlib. It also imports specific functions and classes from these libraries.

2. The find_similarities function is defined. 
It takes two parameters: sentences and stopwords. This function performs the following steps:

    => It creates a TfidfVectorizer object from scikit-learn, specifying the stop_words parameter as the stopwords argument.
    => It uses the fit_transform method of the vectorizer to transform the input sentences into TF-IDF vectors (trsfm).
    => It creates a Pandas DataFrame (text_df) from the transformed vectors, with the columns as the feature names and the index as the original sentences.
    => It calculates the number of sentences (num_sentences) in the input text and determines the number of sentences to be used in the summary (num_summary_sentences). The number of summary sentences is calculated as the square root of the number of sentences, rounded up.
    => It calculates the cosine similarity between all pairs of sentences using the transformed vectors.
    => It creates a list (avgs) to hold the average cosine similarity for each sentence.
    => It iterates over the cosine similarity values and calculates the mean for each sentence, storing it in the avgs list.
    => It finds the indices of the sentences with the highest average cosine similarities (top_idx) based on the num_summary_sentences.
    => Finally, it returns the top_idx list.
3. The build_summary function is defined. It takes two parameters: sentences and stopwords. This function performs the following steps:

    =>It calls the find_similarities function with the input sentences and stopwords to obtain the indices of the sentences to be used in the summary (sents_for_sum).
    =>It sorts the indices in ascending order.
    =>It prints the number of selected sentences (len(sort)).
    =>It assigns the input sentences to the sent_list variable.
    =>It prints the total number of sentences in the input sent_list.
    =>It extracts the selected sentences from the sent_list using the indices from sort. It removes any newline characters and appends a period at the end of each sentence. The extracted sentences are stored in the sents list.
    =>It joins the sentences in the sents list into a single string, separated by spaces, and assigns it to the summary variable.
    =>Finally, it returns the summary string.


4. The __main__ block is the entry point of the script. It performs the following steps:

    =>It assigns an empty string to the book_url variable. This variable represents the URL or path to the PDF document to be summarized.
    =>It creates an instance of the pdfPrser class from the pdfParser module, passing the book_url as the argument. The pdfPrser class is assumed to handle the parsing of the PDF document and provide a list of sentences (pparser.sentences) as the output.
    =>It calls the build_summary function with pparser.sentences as the input and assigns the result to the article_summary variable.
    =>It prints the article_summary.
"""
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
import pdfParser as pp
from sklearn import feature_extraction
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances_argmin_min
import nltk
nltk.download('punkt')
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def find_similarities(sentences, stopwords):
    #tokenize sentences
    #sentences = sent_tokenize(text, language = 'en')
    #sentences = text.sentences
    #set stop words
    #stops = list(set(stopwords.words('english'))) + list(punctuation)
    
    #vectorize sentences and remove stop words
    vectorizer = TfidfVectorizer(stop_words = stopwords)
    #transform using TFIDF vectorizer
    trsfm=vectorizer.fit_transform(sentences)
    
    #creat df for input article
    text_df = pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names_out(),index=sentences)
    
    #declare how many sentences to use in summary
    num_sentences = text_df.shape[0]
    num_summary_sentences = int(np.ceil(num_sentences**.5))
        
    #find cosine similarity for all sentence pairs
    similarities = cosine_similarity(trsfm, trsfm)
    
    #create list to hold avg cosine similarities for each sentence
    avgs = []
    for i in similarities:
        avgs.append(i.mean())
     
    #find index values of the sentences to be used for summary
    top_idx = np.argsort(avgs)[-num_summary_sentences:]
    
    return top_idx


def build_summary(sentences, stopwords):
    #find sentences to extract for summary
    sents_for_sum = find_similarities(sentences, stopwords)
    #sort the sentences
    sort = sorted(sents_for_sum)
    #display which sentences have been selected
    print('Number of selected sentences',len(sort))
    
    sent_list = sentences#sent_tokenize(text)
    #print number of sentences in full article
    print('Total number of sentences', len(sent_list))
    
    
    #extract the selected sentences from the original text
    sents = []
    for i in sort:
        sents.append(sent_list[i].replace('\n', '') + '።') 
    
    #join sentences together for final output
    summary = ' '.join(sents) 
    return summary

if __name__ == "__main__":
        book_url = ''
        pparser = pp.pdfPrser(book_url)
        article_summary = build_summary(pparser.sentences)
        print(article_summary)
