import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud


def generate_word_cloud(df):
    Content_fig_path= "Content_fig_wc.png"
    facebook_fig_path = "facebook_fig_wc.png"
    instagram_fig_path = "instagram_fig_wc.png"
    twitter_fig_path = "twitter_fig_wc.png"
    youtube_fig_path = "youtube_fig_wc.png"
    linkedin_fig_path = "linkedin_fig_wc.png"
    
    wrod(df['Content'], Content_fig_path)
    wrod(df[df['Source']=='Facebook.com']['Content'], facebook_fig_path)
    wrod(df[df['Source']=='Instagram']['Content'], instagram_fig_path)
    wrod(df[df['Source']=='Twitter.com']['Content'], twitter_fig_path)
    wrod(df[df['Source']=='youtube.com']['Content'], youtube_fig_path)
    wrod(df[df['Source']=='linkedin']['Content'], linkedin_fig_path)

    return Content_fig_path, facebook_fig_path, instagram_fig_path, twitter_fig_path, youtube_fig_path, linkedin_fig_path


def wrod(Content_series, file_path):
    Content_series = Content_series.astype(str)

    text = ' '.join(Content_series.tolist())

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Plot the word cloud
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    # Save the word cloud as an image
    plt.savefig(file_path)
    plt.close()

    return file_path