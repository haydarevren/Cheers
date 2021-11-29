# Cheers - NLP beer recommendation engine
![cheers_animation2](https://user-images.githubusercontent.com/79766032/143927360-fc083dc2-1fe9-4b5d-93fc-00cffe526c9e.gif)

## An interactive web app that allows users to type the flavors/characteristics they find appealing and shows five recommended beers and the user's taste profile.

This capstone deliverable consists of this github repo, and a Flask app deployed with heroku: https://cheers-capstone.herokuapp.com/ (app is down right now)

## Project description
  You are not alone if you have ever found yourself staring at a wall of beers at your local supermarket, scouring the Internet on your phone, looking up obscure beer names for reviews. You have come to the right place if you are always looking for something new to try, but also don't want to be disappointed that you are making a good choice. Although Cheers allows you to find a beer that suits your taste with the touch of a few buttons, the underlying methods can also improve business decisions. For example, a liquor shop wants to know similar beers to its top-selling ones? Cheers can help solve your problem.

Using the text entry that describes flavors/characteristic you are looking for in the moment, cheers provides:

  - 3 recommended beers and their Word Cloud built out of TF-IDF and their descriptions,
  - recommended beer styles shown in a polar bar chart,
  - interactive network vizuliazation, a the web-network of different beer and their relationships to each other. 

## Data Ingestion

  Beeradvocate.com and Ratebeer.com: For each beer, its reviews, description, and	style are scraped using BeautifulSoup. (~3M reviews and descriptions)

  - I performed data cleaning and preprocessing to have a reliable and balanced dataset.
  - The final dataset consists of ~1.2M reviews.
  - Main tools: Pandas, Beatifulsoup, Requests, Seaborn, NLP features (nltk, spacy).

## Model

  Natural language processing, transfer learning, deep learning, and classification uncovers relationships between these descriptive sentences and beers. This part involves two main sections.

  1) Transforming unstructured text data to high dimensional vectors: With sentence embedding the context of the whole sentence is captured in a vector. 

  2) Deep learning for classification

  - I tried a variety of models for classification task (with and without tranfer learning). You can see the performance of them below.

  | Embedding | Model | Train Accuracy(Top-1) | Test Accuracy(Top-1) | Train Accuracy(Top-5) | Test Accuracy(Top-5) |
  | --- | --- | --- | --- | --- | --- |
  | TfidfVectorizer | Logistic | 17.1% | 16.9% | 34.9% | 34.5% |
  | USE | Logistic | 31.4% | 29.4% | 54.5% | 54.4% |
  | USE | MultinomialNB | 3.9% | 3.8% | 11.5% | 11.4% |
  | USE | LinearSVC | 29.2% | 25.9% | 51.3% | 50.1% |
  | USE | XGBoost | 42.5% | 30.4% | 72.1% | 55.9% |
  | USE | DNN | 36.5% | 34.4% | 59.9% | 59.2% |

  - The best results were obtained with a model using tranfer learning with deep learning.
  - I trained a separate deep learning model to predict user's beer taste in terms of beer style.
  - The third model is to uncover the semantic similarity between beer reviews. I used cosine similarities and filtered the closest 2 beers
  - Main tools: TensorFlow's Universal Sentence Embedding, TensorFlow, Scikit-Learn, NLP feature-extraction tools.

  See the https://github.com/haydarevren/Cheers/blob/main/notebooks/EDA%20and%20Model%20Training.ipynb notebook for details.  

## Visualization of the results 

  - Using wordcloud and matplotlib, I showed the recommended beers in the shape of wordcloud and user's beer taste in a polar chart.
  - Using pyvis, I created an interactive network to show the relationsship between different beers.
  - The explanatory data analysis is in 'EDA and Model Training' notebook.

This project was developped during my fellowship at The Data Incubator.
