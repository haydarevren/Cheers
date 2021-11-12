# Cheers - NLP beer recommendation engine

The number of different beers produced in the United States has increased from 10,000 to nearly 100,000 in the last decade. Several issues arise as a result of this. One, a beer's style, such as IPA, is meaningless because there are over 50k of them, each with its own distinct flavor profile. Second, how can one choose between a wall of beer in a liquor store or a tap list with hundreds of beers on tap?

Cheers is a beer recommendation engine to addresses both of these concerns by allowing users to search for beers based on how we actually choose beers: by describing the flavors we desire or beers in similar taste.

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


