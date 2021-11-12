# Cheers - NLP beer recommendation engine

## An interactive web app that allows users to type the flavors/characteristics they find appealing and shows five recommended beers and the user's taste profile.

You are not alone if you have ever found yourself staring at a wall of beers at your local supermarket, scouring the Internet on your phone, looking up obscure beer names for reviews. You have come to the right place if you are always looking for something new to try, but also don't want to be disappointed that you are making a good choice. Although Cheers allows you to find a beer that suits your taste with the touch of a few buttons, the underlying methods can also improve business decisions. For example, a liquor shop wants to know similar beers to its top-selling ones? Cheers can help solve your problem.

Using the text entry that describes flavors/characteristic you are looking for in the moment, cheers provides:

  - 5 recommended beers,
  - word cloud of each recommended beer,
  - polar bar chart of the user's taste profile in terms of beer styles.

Data:

  Beeradvocate.com and Ratebeer.com: For each beer, its reviews, description, and	style are scraped using BeautifulSoup. (2m+ reviews and descriptions)
 
Model:

Natural language processing, deep learning, and classification uncovers relationships between these descriptive sentences and beers. This part involves two main sections.

1) Transforming unstructured text data to high dimensional vectors: With sentence embedding the context of the whole sentence is captured in a vector. 

2) Deep learning fro classification



| Embedding | Model | Train Accuracy(Top-1) | Test Accuracy(Top-1) | Train Accuracy(Top-5) | Test Accuracy(Top-5) |
| --- | --- | --- | --- | --- | --- |
| TfidfVectorizer | Logistic | 17.1% | 16.9% | 34.9% | 34.5% |
| USE | Logistic | 31.4% | 29.4% | 54.5% | 54.4% |
| USE | MultinomialNB | 3.9% | 3.8% | 11.5% | 11.4% |
| USE | LinearSVC | 29.2% | 25.9% | 51.3% | 50.1% |
| USE | XGBoost | 42.5% | 30.4% | 72.1% | 55.9% |
| USE | DNN | 36.5% | 34.4% | 59.9% | 59.2% |

This project was developped during my fellowship at The Data Incubator.
