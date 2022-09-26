 <p align="center">
    <img src="https://github.com/agusle/sentiment-analysis-on-movie-reviews/blob/main/img/project-logo.png" width = 400 height = 400>
</p>

<p align="center">
    <a href="https://github.com/agusle/sentiment-analysis-on-movie-reviews/commits/main">
    <img src="https://img.shields.io/github/last-commit/agusle/sentiment-analysis-on-movie-reviews?logo=Github"
         alt="GitHub last commit">
    <a href="https://github.com/agusle/sentiment-analysis-on-movie-reviews/issues">
    <img src="https://img.shields.io/github/issues-raw/agusle/sentiment-analysis-on-movie-reviews?logo=Github"
         alt="GitHub issues">
    <a href="https://github.com/agusle/sentiment-analysis-on-movie-reviews/pulls">
    <img src="https://img.shields.io/github/issues-pr-raw/agusle/sentiment-analysis-on-movie-reviews?logo=Github"
         alt="GitHub pull requests">
</p>

<p align="center">
  <a href="#-about">About</a> • 
  <a href="#%EF%B8%8F-install-and-run">Install and Run</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-contribute">Contribute</a> •
</p>

------------------

## 📖 About
- **Problem**: Movie reviews help users decide if the movie is worth their time. A summary of all the reviews for a movie can help users make this decision without wasting time reading all the reviews. Movie rating websites are often used by critics to post reviews and rate movies, which helps viewers decide if the movie is worth watching. Sentiment analysis of a movie can determine the attitude of critics based on their reviews and rate them as positive or negative. 

- **Industries**: film industry, streaming services, movie-rating websites,etc.

- **Solution**:  Natural Language Processing (NLP) is a subfield of machine learning that allows computers to understand, analyze, manipulate and generate human language. Understanding whether a review is positive or negative can be automated as the machine learns, through this subfield mentioned above, by training and testing different data sources.  
Classification is a data mining methodology that assigns classes to a collection of data to help make more accurate predictions and analysis.  
In this case, the solution consists of applying **binary sentiment classification approach in natural language processing** to determine the sentiment of a text from the [Stanford AI Lab's movie review dataset](https://ai.stanford.edu/~amaas/data/sentiment/).  
Basically a basic sentiment analysis problem, as in this case, consists of a classification problem, where the possible output labels are: `positive` and `negative`. Which indicates, if the review of a movie speaks positively or negatively. In our case it is a binary problem, but one could have many more "feelings" tagged and thus allow a more granular analysis.  
These are the objectives of the project:

    - Read data that is not in a traditional format.
    - Put together a set of preprocessing functions that we can use later on any NLP or related problems.
    - Vectorize the data in order to apply a machine learning model to it: using BoW or TF-IDF.
    - BoW and TF-IDF are classic ways to vectorize text, but currently we have some more complex ways with better performance, for this we are going to train our own word embedding and use it as a vectorization source for our data.
    - Train a sentiment analysis model that allows us to detect positive and negative opinions in movie reviews.


You can see the whole project in the following **notebook**:
 - [Sentiment_Analysis_NLP](https://github.com/agusle/sentiment-analysis-on-movie-reviews/blob/main/Sentiment_Analysis_NLP.ipynb)

------------------

## ⚡️ Install and Run 

Listed below you'll find an example or application usage to run the services using compose:

You can use `Docker` to easily install all the needed packages and libraries.

- **CPU:**

```bash
$ docker build -t sentiment_analysis -f Dockerfile .
```

- **Run Docker**

```bash
$ docker run --rm -it \
    -p 8888:8888 \
    -v $(pwd):/home/app/src \
    --workdir /home/app/src \
    sentiment_analysis \
    bash
```

- **Tests**

Some basic tests were added to [Sentiment_Analysis_NLP.ipynb](https://github.com/agusle/sentiment-analysis-on-movie-reviews/blob/main/Sentiment_Analysis_NLP.ipynb) that you must be able to run without errors. If you encounter some issues in the path, make sure to be following these requirements in your code:

- Every time you need to run a tokenizer on your sentences, use `nltk.tokenize.toktok.ToktokTokenizer`.
- When removing stopwords, always use `nltk.corpus.stopwords.words('english')`.
- For Stemming, use `nltk.porter.PorterStemmer`.
- For Lematizer, use `Spacy` pre-trained model `en_core_web_sm`.

You can use others methods if you want to do extra experimentation but do it outside the code used to run the tests. Otherwise, they may fail for some specific cases.

------------------

## 👀 Usage

It doesn't matter if you are inside or outside a Docker container, in order to execute the project you need to launch a Jupyter notebook server running:

```bash
$ jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root
```
------------------

## 👍 Contribute
**Please follow these steps to get your work merged in.**

1. Add a [GitHub Star](https://github.com/agusle/sentiment-analysis-on-movie-reviews) to the project.
2. Clone repo and create a new branch: `$ git checkout https://github.com/agusle/sentiment-analysis-on-movie-reviews -b name_for_new_branch.`
3. Add a feature, fix a bug, or refactor some code :)
4. Write/update tests for the changes you made, if necessary.
5. Update `README.md`, if necessary.
4. Submit Pull Request with comprehensive description of changes

