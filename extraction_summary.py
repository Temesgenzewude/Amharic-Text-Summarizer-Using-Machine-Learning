
"""
This code is another implementation of a document summarization algorithm. It uses a frequency-based approach to score sentences and generate a summary. Let's go through the code step by step:
1. The code starts by importing necessary modules (os, sys, re) and packages. It also imports a custom module pdfParser as pp.

2. It defines a function _create_dictionary_table that takes a list of words as input and returns a dictionary representing the word frequency table. The function iterates over the words, counts their occurrences, and stores them in the frequency_table dictionary.

3. The _calculate_sentence_scores function takes a list of sentences and the frequency_table as input and returns a dictionary representing the weight of each sentence. The function iterates over the sentences, splits them into words, and checks each word against the frequency_table. If a word is found in the table, its frequency is assigned as the weight for the sentence in the sentence_weight dictionary.

4. The _calculate_average_score function takes the sentence_weight dictionary as input and calculates the average score for the sentences. It sums up all the scores in the sentence_weight dictionary and divides the sum by the number of sentences to get the average score.

5. The _get_article_summary function takes the list of sentences, sentence_weight dictionary, and a threshold value as input. It generates the summary by iterating over the sentences, checking if each sentence is in the sentence_weight dictionary and if its weight is above the threshold. If a sentence meets the criteria, it is added to the article_summary string. The function also removes duplicate phrases using regular expressions.

6. The _get_summary function takes an instance of the pdfPrser class (pparser) and an optional threshold parameter as input. It extracts the sentences from pparser, creates the frequency_table using _create_dictionary_table, calculates the sentence scores using _calculate_sentence_scores, calculates the threshold using _calculate_average_score, and generates the summary using _get_article_summary.

7. The __main__ block is the entry point of the script. It performs the following steps:

    =>It assigns an empty string to the book_url variable, representing the URL or path to the PDF document.
    =>It creates an instance of the pdfPrser class (pparser) from the pdfParser module, passing the book_url as the argument.
    =>It calls the _get_summary function with pparser as the input and assigns the result to the article_summary variable.
    =>It prints the article_summary.

"""
import os, sys
import re
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import pdfParser as pp


def _create_dictionary_table(words) -> dict:
    # Creating dictionary for the word frequency table
    frequency_table = dict()
    #words = text_string.split() 

    for wd in words:
        #wd = stem.stem(wd)
        #if wd in stop_words:
        #    continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1

    return frequency_table

def _calculate_sentence_scores(sentences, frequency_table) -> dict:   

    #algorithm for scoring a sentence by its words
    sentence_weight = dict()

    for sentence in sentences:
        #sentence = ' '.join(sentence)
        #sentence_wordcount = (len(sentence.split()))
        sentence_wordcount_without_stop_words = 0
        words = sentence.split() 
        for word in words:
            if word in frequency_table:
                sentence_weight[sentence] = frequency_table[word]

        #sentence_weight[sentence] = sentence_weight[sentence]/len(words)


        
        # for word_weight in frequency_table:
        #     if word_weight in sentence      #.lower():
        #         sentence_wordcount_without_stop_words += 1
        #         if sentence[:7] in sentence_weight:
        #             sentence_weight[sentence[:7]] += frequency_table[word_weight]
        #         else:
        #             sentence_weight[sentence[:7]] = frequency_table[word_weight]

        # sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words       

    return sentence_weight

def _calculate_average_score(sentence_weight) -> int:
   
    #calculating the average score for the sentences
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]

    #getting sentence average value from source text
    average_score = (sum_values / len(sentence_weight))

    return average_score

def _get_article_summary(sentences, sentence_weight, threshold):
    sentence_counter = 0
    article_summary = ''

    for sentence in sentences:
        #sentence = ' '.join(sentence)
        if sentence in sentence_weight and sentence_weight[sentence] >= (threshold):
            article_summary += sentence + '።'
            sentence_counter += 1
    #remove duplicate phrase
    article_summary = re.sub(r'((\b\w+\b.{1,2}\w+\b)+).+\1', r'\1', article_summary, flags = re.I)

    return article_summary

def _get_summary(pparser, treshold_parameter=1.5):
    sentences = pparser.sentences

    #creating a dictionary for the word frequency table
    frequency_table = _create_dictionary_table(pparser.words)

    #tokenizing the sentences
        #we have sentences

    #algorithm for scoring a sentence by its words
    sentence_scores = _calculate_sentence_scores(sentences, frequency_table)    

    #getting the threshold
    threshold = _calculate_average_score(sentence_scores)

    #producing the summary
    return _get_article_summary(sentences, sentence_scores, treshold_parameter * threshold)


if __name__ == "__main__":
    book_url = ''
    pparser = pp.pdfPrser(book_url)
    article_summary = _get_summary(pparser)
    print(article_summary)