import matplotlib.pyplot as plt
import pandas as pd

def generate_dashboard(df):
    sentiment_fig = plot_piechart(df, 'Sentiment')
    facebook_fig = plot_piechart(df[df['Source']=='Facebook.com'], 'Sentiment')
    instagram_fig = plot_piechart(df[df['Source']=='Instagram'], 'Sentiment')
    twitter_fig = plot_piechart(df[df['Source']=='Twitter.com'], 'Sentiment')
    youtube_fig = plot_piechart(df[df['Source']=='youtube.com'], 'Sentiment')
    linkedin_fig = plot_piechart(df[df['Source']=='linkedin'], 'Sentiment')

#Twitter.com', 'youtube.com', 'linkedin', 'Facebook.com','Instagram
    return sentiment_fig, facebook_fig, instagram_fig, twitter_fig, youtube_fig, linkedin_fig

def plot_piechart(data, column, background_color=None):
    sentiment_counts = data[column].value_counts()
    
    if background_color is None:
        background_color = '#ffffff'  # White
    
    colors = {'Positive': 'purple', 'Negative': 'red', 'Neutral': 'white'}
    
    labels = sentiment_counts.index.tolist()
    counts = sentiment_counts.values.tolist()
    explode = (0, 0.2, 0.0)  # Explode the negative slices slightly
    
    fig, ax = plt.subplots(figsize=(8, 6))
    patches, texts, autotexts = ax.pie(counts, labels=None, autopct='%1.1f%%', startangle=140, 
                                       colors=[colors[label] for label in labels], explode=explode,             
                                       textprops=dict(color="#39FF14"))  
    
    ax.axis('equal')  
    ax.set_facecolor(background_color)
    fig.patch.set_facecolor('white')
    
    for text, label in zip(autotexts, labels):
        text.set_text(f'{text.get_text()} - {label}')
    
    plt.legend(patches, labels, loc="best")
    return fig
