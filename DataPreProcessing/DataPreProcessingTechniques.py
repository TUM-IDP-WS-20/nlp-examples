########################################################################################
########################################################################################
##
## DATA PRE PROCESSING TECHNIQUES
##
########################################################################################
########################################################################################
class DataPreProcessingTechniques:

    def __init__(self, stop_list = ""):
        self.stop_list = ""

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
        