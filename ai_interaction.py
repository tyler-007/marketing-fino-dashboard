import pandas as pd
import numpy as np
import openai
import matplotlib.pyplot as plt
openai.api_key='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'

import subprocess
import sys

def create_virtual_environment():
    subprocess.run([sys.executable, '-m', 'venv', 'openai_env'])

def install_latest_openai():
    subprocess.run(['source', 'openai_env/bin/activate'])

    subprocess.run(['pip', 'install', '--upgrade', 'openai'])

def main():
    create_virtual_environment()

    install_latest_openai()

    subprocess.run(['source', 'openai_env/bin/activate'])

    import openai
    print("OpenAI version:", openai.__version__)

if __name__ == "__main__":
    main()




def get_completion(prompt, model="gpt-3.5-turbo",temperature=0): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [
        {"role": "system", "content": "You are a kind business insight employee with speciality in online media sentiment analysis, you work in India's Largest Payments Bank - Fino Payments Bank"},
        {"role": "assistant", "content": prompt}
    ]    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

list_response=[]

def labelling(data):
    sentiment_content_dict = {}
    for index, row in data.iterrows():
        sentiment = row['Sentiment']
        content = row['Content']  
        if sentiment in sentiment_content_dict:
            sentiment_content_dict[sentiment].append(content)
        else:
            sentiment_content_dict[sentiment] = [content]
    return sentiment_content_dict


def generate_suggestions(api_key,data):

    data = data.sample(n=300, random_state=42)
    openai.api_key=api_key
    dict_obt=labelling(data)

    for sentiment in dict_obt.keys():
        prompt =  f""" 
As a business insights expert at Fino Payments Bank.\
You have been given a dataset which has negative, positive, constructive and neutral feedbacks in comments section of different social media platfrom in which Fino Payments Bank is active.\
You are given a task to analyse the {sentiment} \
You must read, remember and analyse all the comments in this section\
After reading them you must present the top 5 findings related to the sentiment\
It should reflect the sentiment of the people, what they feel\
Also, from the analysis you must give a percentage stat of how many comments from the total think the same\
These top 5 most popular talks will be noted by the Directors of the company and will be addressed\
Make sure you return only and only 5 points, thats it and that too in bullet points
"""
        response = get_completion(prompt)
        list_response.append(response)
    return list_response

    
    






    
