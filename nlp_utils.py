import nltk
from nltk import PorterStemmer
from nltk import pos_tag
from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_query(query):
    """
    Preprocesses a user query by converting to lowercase, performing stemming,
    and performing part-of-speech tagging.

    Args:
        query: The user's query as a string.

    Returns:
        A list of tuples containing (stemmed_word, part-of-speech) tags.
    """

    # Download resources required for POS tagging (one-time)
    #nltk.download('punkt')

    # Convert the query to lowercase
    lowercase_query = query.lower()

    # Perform stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in lowercase_query.split()]

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
  for concept in knowledge_base:
    # Check for exact word match first
    if any(word[0] in concept for word in preprocessed_query):
      potential_concepts.append(concept)
      continue  # Don't do fuzzy matching if exact match found

    # Fuzzy matching (already implemented, no changes needed)
    # ...

  return potential_concepts

