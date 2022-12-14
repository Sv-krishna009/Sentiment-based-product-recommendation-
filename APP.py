#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
from email import header
from operator import index
from flask import Flask, request, render_template, jsonify
import pickle


# In[ ]:


app = Flask(__name__)


# In[ ]:


sentiment_model = pickle.load(open("ML_Deployment Model.pkl", 'rb'))


# In[ ]:


@app.route('/')
def home():
    return render_template('index.html')


# In[ ]:


if __name__ == '__main__':
    app.debug=True
    app.run(debug=True, use_reloader=False)
    
    


# In[ ]:


@app.route("/predict", methods=['POST'])
def predict():
    # get user from the html form
    user = request.form['userName']
    # convert text to lowercase
    user = user.lower()
    items = sentiment_model.getSentimentRecommendations(user)

    if(not(items is None)):
        print(f"retrieving items....{len(items)}")
        print(items)
        # data=[items.to_html(classes="table-striped table-hover", header="true",index=False)
        return render_template("index.html", column_names=items.columns.values, row_data=list(items.values.tolist()), zip=zip)
    else:
        return render_template("index.html", message="User Name doesn't exists, No product recommendations at this point of time!")


# In[ ]:



@app.route('/predictSentiment', methods=['POST'])
def predict_sentiment():
    # get the review text from the html form
    review_text = request.form["reviewText"]
    print(review_text)
    pred_sentiment = sentiment_model.classify_sentiment(review_text)
    print(pred_sentiment)
    return render_template("index.html", sentiment=pred_sentiment)


# In[ ]:


if __name__ == '__main__':
    app.run()
    
    


# In[ ]:




