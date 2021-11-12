# Cheers - NLP beer recommendation engine

## An interactive web app that allows users to type the flavors/characteristics they find appealing and shows five recommended beers and the user's taste profile.

You are not alone if you have ever found yourself staring at a wall of beers at your local supermarket, scouring the Internet on your phone, looking up obscure beer names for reviews. You have come to the right place if you are always looking for something new to try, but also don't want to be disappointed that you are making a good choice. Although Cheers allows you to find a beer that suits your taste with the touch of a few buttons, the underlying methods can also improve business decisions. For example, a liquor shop wants to know similar beers to its top-selling ones? Cheers can help solve your problem.


The deliverable of this project will be a web app. Using a dataset of reviews and descriptions from popular beer websites, the engine provides a list of beers using the maximum number of keywords specified by the user.  In just a single result page, each beer is listed along with its description, average rating, and a link that showing the list of places you can find it near your location.

Data:

  1. Beeradvocate.com: For each beer, its reviews, ratings, state,	country, and	style are scraped from beeradvocate.com.
  2. Ratebeer.com, Untappd.com, Beerconnoisseur.com, Influenster.com: Will be added after finizlizing the model.

Model:

| Embedding | Model | Train Accuracy(Top-1) | Test Accuracy(Top-1) | Train Accuracy(Top-5) | Test Accuracy(Top-5) |
| --- | --- | --- | --- | --- | --- |
| TfidfVectorizer | Logistic | 17.1% | 16.9% | 34.9% | 34.5% |
| USE | Logistic | 31.4% | 29.4% | 54.5% | 54.4% |
| USE | MultinomialNB | 3.9% | 3.8% | 11.5% | 11.4% |
| USE | LinearSVC | 29.2% | 25.9% | 51.3% | 50.1% |
| USE | XGBoost | 42.5% | 30.4% | 72.1% | 55.9% |
| USE | DNN | 36.5% | 34.4% | 59.9% | 59.2% |

This project was developped during my fellowship at The Data Incubator.
