import pandas as pd
import numpy as np
import openai
import matplotlib.pyplot as plt

def get_completion(prompt, model="gpt-3.5-turbo",temperature=0): 
    messages = [
        {"role": "system", "content": "You are a kind business insight employee with speciality in online media sentiment analysis, you work in India's Largest Payments Bank - Fino Pay App"},
        {"role": "assistant", "content": prompt}
    ]    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
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

    openai.api_key=api_key
    dict_obt=labelling(data)

    for sentiment in dict_obt.keys():
        prompt =  f""" 
As a business insights expert at Fino Pay App, you have been tasked with analyzing the {sentiment} feedback received from various social media platforms where Fino Pay App is active. The dataset contains comments categorized as {sentiment}.\

Your objective is to thoroughly analyze the {sentiment} feedback by reading, memorizing, and interpreting all comments in this category. After analysis, you are required to present the top 5 insights derived from the sentiment. These insights should reflect the prevailing sentiment of the people and provide a deeper understanding of their feelings.\

Furthermore, for each insight, you must provide a percentage stat indicating the proportion of comments expressing the same sentiment out of the total comments analyzed. For example, "35% of the total positive comments expressed satisfaction with the user interface (UI)."\
Bank on the go with the new FinoPay Mobile banking Application.
This is a revamped version of existing BPay application. This app has been designed keeping in mind the customer favourite touch points and for enhancing customers digital banking experience.
FinoPay is your one stop solution for all your banking needs with features like UPI, Fund Transfer, Merchant payments, Recharge, Utility payments and much more.
You can link your account for UPI on FinoPay and can avail UPI services for fast and secure payments
Just create your UPI VPA on FinoPay and link it to your Fino or Non-Fino Savings accounts to start sending & receiving money instantly through UPI. There are zero charges for transferring money using UPI.
FinoPay is a unique app with combination of mobile wallet and Mobile banking .You can access all your Fino bank accounts on FinoPay.
FinoPay has been aligned as per our motto of “Fino hai to fikar not” to provide customer a “fikar not” banking experience.
It’s an app with simple user experience and user adaptability. This app has been built keeping in mind the customer daily needs and usage behaviour.
Key Features:
- View and transact from all your Fino accounts i.e. Wallet, Saving & Current account.
- Buy insurance for self and family through FinoPay through our partner’s tie-ups.
- Link any of your bank account with Fino BHIM UPI and send & receive money instantly
- Have a flexibility of sending money from any of your account or wallet
- Send Money instantly using IMPS to other Bank accounts by entering account number and IFSC.
- Send Money to Fino customer using Mobile number to any of her/his Fino Account/Wallet(Full KYC)
- Transact superfast using Favourite feature. By tagging a transaction as favourite, you can quickly access and complete your transactions like mobile recharge or fund transfer
- Full KYC wallet customers can Send Money to mobile wallets of their friends and family with minimum clicks
- Get personalized offers designed for you through our notifications and banners which will keep you updated on the latest product offering for your daily needs
- Load money in your wallet using your Debit / Credit Cards, Net Banking & UPI. You can also save your cards for reloading quickly in future powered by our PG partner
- No need to worry about cash, pay at any merchant store by just scanning the QR code with FinoPay
- Use FinoPay for hassle free payment of all your Bill Payments through the integrated BBPS platform.
Recharge your mobile numbers pertaining to any telecom operator. Also get recharge options for DTH, Cable TV etc. on FinoPay.
- Pay your insurance premium with FinoPay for all the major insurance companies
- We will keep adding new products and offering for providing our customer an entire digital product suite.
Register yourself and experience the fastest and secure application to access all your accounts!
FinoPay is supported on all android versions i.e. 4.0 and up.
Be a part of the Cashless revolution and download FinoPay now!
For any queries or suggestions please feel free to write to us at customercare@finobank.com

The top 5 insights will be compiled as bullet points and presented to the Directors of the company for review and action.\

Please ensure that your analysis is concise and focuses on the most significant findings. Limit your output to only 5 bullet points, each accompanied by its respective percentage stat.\

"""
        response = get_completion(prompt)
        list_response.append(response)
    return list_response

    
    






    
