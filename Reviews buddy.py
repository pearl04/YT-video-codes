#!/usr/bin/env python
# coding: utf-8

# # Bot 
# This bot reads customer reviews and provides an assuring reply to them 
# 

# In[1]:


#openai library is used to interact with OpenAI's API
import openai
#os module is used to access environment variables
#environment variables are those stored in computer (outside application) : for privacy of secret keys
import os

#dotenv library is used to get load and find dotenv functions
#find dotenv , looks for a .env file in your project directory. once found , load dotenv , loads it into the application

from dotenv import load_dotenv, find_dotenv
#here "_" specifically means we dont care about value returned , we just want to load the secret key so API works
_=load_dotenv(find_dotenv())

#gets the api key from environment and use to connect to openAI API
openai.api_key=os.getenv('OPENAI_API_KEY')



# In[2]:


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# In[5]:


def collect_reviews(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)


# In[6]:


#This is the review I would be using!
lamp_review = """
Keith : Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast.  The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together.  I had a missing part, so I contacted their \
support and they very quickly got me the missing piece! \
Lumina seems to me to be a great company that cares \
about their customers and products!!
"""


# In[7]:


#Iteration 1
import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context= [
    {
      "role": "system",
      "content": """
You are ReviewBot, an automated service designed to read and respond to customer reviews for a business. \
Your first task is to analyze the sentiment of the review (positive, negative, or neutral). \
You then identify key details from the review, such as specific comments about service, product quality, or experience. \
Based on the sentiment and the details provided, you craft a personalized response. \
Your response should address any concerns raised, highlight positives mentioned, and, if applicable, explain how feedback will be used to improve. \
For negative reviews, ensure the message is empathetic and offers a solution or compensation if appropriate. \
For positive reviews, express gratitude and encourage future visits or purchases. \
Always use a friendly and professional tone, aiming to make the customer feel heard and valued. \
Your responses should help build a positive relationship with the customer, encouraging trust and loyalty.\
"""
    }
  ]  # accumulate messages


# In[8]:


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_reviews, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard


# In[9]:


#Iteration 2
import panel as pn  # GUI
pn.extension()

panels = []  # collect display 

context = [
    {
      "role": "system",
      "content": """
You are ReviewBot, an automated AI service designed to read and respond to customer reviews for a business. \
Your first task is to analyze the sentiment of the review (positive, negative, or neutral). \
You then identify key details from the review, such as specific comments about service, product quality, or experience. \
Based on the sentiment and the details provided, you craft a personalized response that addresses any concerns raised, highlights positives mentioned, and, if applicable, explains how feedback will be used to improve. \
For negative reviews, your message should be empathetic and offer a solution or compensation if appropriate. \
For positive reviews, you express gratitude and encourage future visits or purchases. \
Always use a friendly and professional tone, aiming to make the customer feel heard and valued. \
Your responses should help build a positive relationship with the customer, encouraging trust and loyalty. \
When concluding your message, always specify that you are an AI agent (mentioning your name, ReviewBot).\
This personalized approach ensures the customer knows their feedback is being taken seriously by the business, even in an automated manner.\
"""
    }
]  # accumulate messages


# In[10]:


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_reviews, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard


# In[11]:


messages =  context.copy()
messages.append(
{'role':'system', 'content':'create a json summary of the sentiment and key details from each review with product/service as key.\
 The fields should be 1) review type  2) sentiment type(positive, negative or neutral) 3) list of sentiments, like happy , angry , disappointed , satisfied etc   4) list of key details in the review'},    
)
 
response = get_completion_from_messages(messages, temperature=0)
print(response)

