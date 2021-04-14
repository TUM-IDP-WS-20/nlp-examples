########################################################################################
########################################################################################
##
## VISUALIZATION TECHNIQUES  
##
########################################################################################
########################################################################################
class VisualizationTechniques:
    def __init__(self, background_color='white', stopwords="", max_words=500, max_font_size=40, random_state=42):
        self.background_color = background_color
        self.stopwords = stopwords
        self.max_words = max_words
        self.max_font_size = max_font_size
        self.random_state = random_state

    ########################################################################################
    ## REMOVE STOP WORDS
    ## input: data_frame --> lemmatized content, background_color, stopwords, max_words, max_font_size, random_state
    ## output: diagram --> draw a word cloud diagram
    ########################################################################################

    def word_cloud(self, data_frame):
        from wordcloud import WordCloud
        import matplotlib.pyplot as plt

        word_cloud = WordCloud(
            background_color=self.background_color,
            stopwords=self.stopwords,
            max_words=self.max_words,
            max_font_size=self.max_font_size,
            random_state=self.random_state
        ).generate(str(data_frame))

        fig = plt.figure(1)
        plt.imshow(word_cloud)
        plt.axis('off')
        plt.show();

    def get_top_n_gram_diagram(self, corpus, num_of_words_in_each_topic, n=1):
        import pandas as pd
        import plotly.graph_objects as go
        from sklearn.feature_extraction.text import CountVectorizer

        vec = CountVectorizer(ngram_range=(n, n), stop_words='english').fit(corpus)
        bag_of_words = vec.transform(corpus)
        sum_words = bag_of_words.sum(axis=0)
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
        common_words = words_freq[:n]
        df = pd.DataFrame(common_words, columns=['ngram', 'count'])

        fig = go.Figure([go.Bar(x=df['ngram'], y=df['count'])])
        fig.update_layout(title=go.layout.Title(
            text="Top {} ngrams in the paper after removing stop words".format(num_of_words_in_each_topic)))
        fig.show()

    def plot_histogram(self, data, title='', x_label='', y_label=''):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 6))
        plt.hist(data, bins=100)
        plt.title(title)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
