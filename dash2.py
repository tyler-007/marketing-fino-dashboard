import matplotlib.pyplot as plt
import pandas as pd

def generate_dashboard(df):
    sentiment_fig_path = "sentiment_fig.png"
    facebook_fig_path = "facebook_fig.png"
    instagram_fig_path = "instagram_fig.png"
    twitter_fig_path = "twitter_fig.png"
    youtube_fig_path = "youtube_fig.png"
    linkedin_fig_path = "linkedin_fig.png"
    
    plot_piechart(df, 'Sentiment', sentiment_fig_path)
    plot_piechart(df[df['Source']=='Facebook.com'], 'Sentiment', facebook_fig_path)
    plot_piechart(df[df['Source']=='Instagram'], 'Sentiment', instagram_fig_path)
    plot_piechart(df[df['Source']=='Twitter.com'], 'Sentiment', twitter_fig_path)
    plot_piechart(df[df['Source']=='youtube.com'], 'Sentiment', youtube_fig_path)
    plot_piechart(df[df['Source']=='linkedin'], 'Sentiment', linkedin_fig_path)

    return sentiment_fig_path, facebook_fig_path, instagram_fig_path, twitter_fig_path, youtube_fig_path, linkedin_fig_path

def plot_piechart(data, column, file_path, background_color=None):
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
                                       textprops=dict(color="#4169E1"))  
    
    ax.axis('equal')  
    ax.set_facecolor(background_color)
    fig.patch.set_facecolor('black')
    
    for text, label in zip(autotexts, labels):
        text.set_text(f'{text.get_text()} - {label}')
    
    plt.legend(patches, labels, loc="best")
    
    # Save the figure as an image
    plt.savefig(file_path)
    plt.close(fig)  # Close the figure to release memory
    
    return file_path
