import re
import nltk
import spacy
import unicodedata
from bs4 import BeautifulSoup
from contractions import CONTRACTION_MAP
from nltk.tokenize.toktok import ToktokTokenizer

tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words("english")
nlp = spacy.load("en_core_web_sm")
stemmer = nltk.stem.porter.PorterStemmer()
nltk.download("stopwords")


def remove_html_tags(text):
    """
    Remove html tags from a string.
    e.g. "<br /><br />But with plague..." to "But with plague..."

    Parameters
    ----------
    text : str
        Sentence or text to modify words.

    Returns
    -------
        Same string with sentence or text with original words replaced.

    """
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()
    return text


def stem_text(text):
    """
    Reduce inflection in words to their root forms.

    Parameters
    ----------
    text : str
        Sentence or text to modify words.

    Returns
    -------
        Same string with sentence or text with original words replaced.

    """
    words = tokenizer.tokenize(text)
    text = [stemmer.stem(word) for word in words]
    text = " ".join(text)
    return text


def lemmatize_text(text):
    """
    Group together the different inflected forms of a word
    so they can be analyzed as a single item. Similar to stemming
    but it brings context to the words.

    Parameters
    ----------
    text : str
        Sentence or text to modify words.

    Returns
    -------
        Same string with sentence or text with original words replaced.

    """
    doc = nlp(text)
    text = " ".join([token.lemma_ for token in doc])
    return text


def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):
    """
    Expand contractions words in string with multiple separators using regex.
    e.g.  "I can't, because it doesn't work." to "I cannot, because it does not work."

    Parameters
    ----------
    text : str
        Word, sentence or text to modify words.

    Returns
    -------
        Same string with word, sentence or text with original words replaced.

    """
    for word in re.split("[, \-!?:]+", text):
        if contraction_mapping.get(word) != None:
            text = text.replace(word, contraction_mapping.get(word))
    return text


def remove_accented_chars(text):
    """
    Remove all the accents (diacritics) of input word, text or sentence.
    e.g. "Héllo, thís is..." to "Hello, this is..."

    Parameters
    ----------
    text : str
        Word, sentence or text to modify words.

    Returns
    -------
        Same string with word, sentence or text with original words replaced.

    """
    text = "".join(
        (
            c
            for c in unicodedata.normalize("NFD", text)
            if unicodedata.category(c) != "Mn"
        )
    )
    return text


def remove_special_chars(text, remove_digits=False):
    """
    Remove all special characters of input word, text or sentence.
    e.g. "hello? there A-Z-R_T(,**)" to "hello there AZRT"

    Parameters
    ----------
    text : str
        Word, sentence or text to modify words.

    Returns
    -------
        Same string with word, sentence or text with original words replaced.
    """
    text = "".join(c for c in str(text) if c.isalnum() or c == " ")
    if remove_digits:
        text = "".join(c for c in text if not c.isdigit())
    return text


def remove_stopwords(text, is_lower_case=False, stopwords=stopword_list):
    """
    Remove stopwords of input word, text or sentence.
    e.g. "He is a very good person" to "good person"

    Parameters
    ----------
    text : str
        Word, sentence or text to modify words.

    Returns
    -------
        Same string with word, sentence or text with original words replaced.
    """
    words = tokenizer.tokenize(text)
    tokens_without_sw = [
        word for word in words if not word.lower() in stopwords
    ]
    text = " ".join(tokens_without_sw)
    return text


def remove_extra_new_lines(text):
    """
    Remove extra new lines ("\n") of input word, text or sentence.
    e.g. "lot\nof\n\n\nlines"

    Parameters
    ----------
    text : str
        Word, sentence or text to modify words.

    Returns
    -------
        Same string with word, sentence or text with original words replaced.
    """
    text = text.replace("\n", " ")
    return text


def remove_extra_whitespace(text):
    """
    Remove extra whitespace of input word, text or sentence.
    e.g. "Hello           my      dear          friend"

    Parameters
    ----------
    text : str
        Word, sentence or text to modify words.

    Returns
    -------
        Same string with word, sentence or text with original words replaced.
    """
    text = " ".join(text.split())
    return text


def normalize_corpus(
    corpus,
    html_stripping=True,
    contraction_expansion=True,
    accented_char_removal=True,
    text_lower_case=True,
    text_stemming=False,
    text_lemmatization=False,
    special_char_removal=True,
    remove_digits=True,
    stopword_removal=True,
    stopwords=stopword_list,
):

    normalized_corpus = []

    # Normalize each doc in the corpus
    for doc in corpus:
        # Remove HTML
        if html_stripping:
            doc = remove_html_tags(doc)

        # Remove extra newlines
        doc = remove_extra_new_lines(doc)

        # Remove accented chars
        if accented_char_removal:
            doc = remove_accented_chars(doc)

        # Expand contractions
        if contraction_expansion:
            doc = expand_contractions(doc)

        # Lemmatize text
        if text_lemmatization:
            doc = lemmatize_text(doc)

        # Stemming text
        if text_stemming and not text_lemmatization:
            doc = stem_text(doc)

        # Remove special chars and\or digits
        if special_char_removal:
            doc = remove_special_chars(doc, remove_digits=remove_digits)

        # Remove extra whitespace
        doc = remove_extra_whitespace(doc)

        # Lowercase the text
        if text_lower_case:
            doc = doc.lower()

        # Remove stopwords
        if stopword_removal:
            doc = remove_stopwords(
                doc, is_lower_case=text_lower_case, stopwords=stopwords
            )

        # Remove extra whitespace
        doc = remove_extra_whitespace(doc)
        doc = doc.strip()

        normalized_corpus.append(doc)

    return normalized_corpus
