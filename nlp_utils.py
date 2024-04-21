import nltk
from nltk import PorterStemmer
from nltk import pos_tag
from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer

import string

def preprocess_query(query):
    """
    Preprocesses a user query by converting to lowercase, removing punctuation marks,
    performing stemming, and performing part-of-speech tagging.

    Args:
        query: The user's query as a string.

    Returns:
        A list of tuples containing (stemmed_word, part-of-speech) tags.
    """

    # Convert the query to lowercase
    lowercase_query = query.lower()

    # Remove punctuation marks
    query_without_punctuation = lowercase_query.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the query
    tokens = nltk.word_tokenize(query_without_punctuation)

    # Perform stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in tokens]

    # Perform part-of-speech tagging
    preprocessed_query = pos_tag(stemmed_words)

    return preprocessed_query


def get_potential_concepts(preprocessed_query, knowledge_base):
    """
    Identifies potential concepts from the knowledge base that might be relevant
    to the user query, using fuzzy matching in addition to exact word matching.

    Args:
        preprocessed_query: The preprocessed user query (list of word-tag tuples).
        knowledge_base: The dictionary containing knowledge base entries.

    Returns:
        A list of concept names (strings) from the knowledge base that are potentially
        related to the user query.
    """
    potential_concepts = []
    for key, value in knowledge_base.items():
        if isinstance(value, dict):
            # Recursively search through nested dictionaries
            potential_concepts.extend(get_potential_concepts(preprocessed_query, value))
        else:
            # Check for exact word match
            if any(word[0] == key for word in preprocessed_query):
                potential_concepts.append(key)

            # Check for fuzzy match
            elif any(fuzz.ratio(word[0], key) > 80 for word in preprocessed_query):
                potential_concepts.append(key)

    return potential_concepts