# Amharic text summarizer
<b>Team Members </b>
Aklile Yilma UGR/7107/12
Joshua Tesfaye UGR/0359/12
Temesgen Zewude UGR/3848/12
Abinet Anamo UGR/7110/12
Henok Mekuanint UGR/2272/12

#Algorithm 1: Extraction
1. Extract all the sentences from text.
2. Extract all the words from text.
3. Assign a score to each word.
4. Assign a score to each sentence.
5. Put the sentences with the highest score together in chronological order to produce the summary.

#Algorithm 2: Cosine Similarity
1. TF-IDF weights to each individual word in a sentence
2. Generate cosine-similarity of each TF-IDF sentence pair matrix
3. Average the weights of each vector
4. Vectors with highest average summarize the text
words with higher weights (more unique) have more importance



Installation 

>pip install -r requirements.txt

>python main.py


pdf at: https://amnewsupdate.files.wordpress.com/2010/09/asteway.pdf


Reference links: <br/>
- https://towardsdatascience.com/understand-text-summarization-and-create-your-own-summarizer-in-python-b26a9f09fc70
- https://github.com/icoxfog417/awesome-text-summarization#motivation
- https://blog.floydhub.com/gentle-introduction-to-text-summarization-in-machine-learning/
- https://www.machinelearningplus.com/nlp/cosine-similarity/

