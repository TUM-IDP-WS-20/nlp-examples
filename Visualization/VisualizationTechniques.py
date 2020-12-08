########################################################################################
########################################################################################
##
## VISUALIZATION TECHNIQUES  
##
########################################################################################
########################################################################################
class VisualizationTechniques:
    def __init__(self, background_color = 'white', stopwords = "", max_words = 500, max_font_size = 40, random_state = 42):
        self.background_color = background_color
        self.stopwords = stopwords
        self.max_words = max_words
        self.max_font_size = max_font_size
        self.random_state = random_state
########################################################################################
## REMOVE STOP WORDS
## input: data_frame --> lemmatized content
## output: diagram --> draw a word cloud diagram
########################################################################################
    
    def word_cloud(self, data_frame):
        from wordcloud import WordCloud
        import matplotlib.pyplot as plt
        
        word_cloud = WordCloud(
                                  background_color= self.background_color,
                                  stopwords=self.stopwords,
                                  max_words = self.max_words,
                                  max_font_size = self.max_font_size,
                                  random_state = self.random_state
                                 ).generate(str(data_frame))
        
        fig = plt.figure(1)
        plt.imshow(word_cloud)
        plt.axis('off')
        plt.show();   
    