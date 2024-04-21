import nltk
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz
import knowledge as k

# Knowledge base


def preprocess_query(query):
    #print("Preprocessing query...")
    tokens = word_tokenize(query)
    return [word.lower() for word in tokens]
kb=k.knowledge_base
def get_potential_concepts(preprocessed_query, kb):
    #print("Getting potential concepts...")
    potential_concepts = []
    for concept in k.knowledge_base.keys():
        if any(word in concept for word in preprocessed_query):
            potential_concepts.append(concept)
    return potential_concepts

def get_explanation(query):
    #print("Inside get_explanation function")
    # Preprocess the user query
    preprocessed_query = preprocess_query(query)
   # print("Preprocessed query:", preprocessed_query)

    # Print keys of the knowledge base for debugging
    #print("Knowledge base keys:", knowledge_base.keys())

    # Identify potential concepts in the knowledge base that match the query
    potential_concepts = get_potential_concepts(preprocessed_query, k.knowledge_base)
    #print("Potential concepts:", potential_concepts)

    # If no potential concepts found, return a message
    if not potential_concepts:
        print("Concept not found in the knowledge base.")
        return

    # If a perfect match is found, return the explanation directly
    if len(potential_concepts) == 1:
        concept = potential_concepts[0]
        #print("Perfect match found")
        return k.knowledge_base[concept]  # Return the entire concept dictionary

    # If no perfect match, identify the concept with the most matching words (basic approach)
    elif potential_concepts:
        best_match_concept = max(potential_concepts, key=lambda concept: len(set(preprocessed_query) & set(concept.split())))
        #print("Best match found")
        return k.knowledge_base[best_match_concept]  # Return the entire concept dictionary

def main():
    print("Script started")
    while True:
        user_query = input("Enter a question about programming (or 'quit' to exit): ")
        if user_query.lower() == ('quit' or 'bye' or 'exit'):
            break
        
        concept_info = get_explanation(user_query)
        if concept_info:
            explanation = concept_info["answer"]
            difficulty_level = concept_info["difficulty_level"]
            additional_resources = concept_info.get("additional_resources", None)
            
            print(f"\nExplanation for {user_query}:")
            print(explanation)
            if additional_resources:
                print(f"\nAdditional Resources: {additional_resources}")

if __name__ == "__main__":
    main()