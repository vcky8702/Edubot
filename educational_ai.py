from nlp_utils import preprocess_query  # Import the preprocess_query function
from nlp_utils import get_potential_concepts
from nlp_utils import *
def get_explanation(query):
  """
  Retrieves the explanation (answer) and other information for a concept.
  Uses NLP to identify the concept from the user query.
  """
  # Preprocess the user query
  preprocessed_query = preprocess_query(query)
  print(preprocessed_query)
  # Identify potential concepts in the knowledge base that match the query
  # We'll use a simple matching approach for now (can be improved later)
  #potential_concepts = [concept for concept in knowledge_base if any(word in concept.split() for word in preprocessed_query)]
  #potential_concepts = [concept for concept in knowledge_base if any(word[0] in concept for word in preprocessed_query)]
  
  potential_concepts = get_potential_concepts(preprocessed_query, knowledge_base)
  
  # If a perfect match is found, return the explanation directly
 # print(potential_concepts)
  if len(potential_concepts) == 1 and potential_concepts[0].lower() == query.lower():
    return knowledge_base[potential_concepts[0]]
  
  # If no perfect match, identify the concept with the most matching words (basic approach)
  elif potential_concepts:
    best_match_concept = max(potential_concepts, key=lambda concept: len(set(preprocessed_query) & set(concept.split())))
    return knowledge_base[best_match_concept]
  
  # No matching concept found
  else:
    return {"explanation": "Concept not found in the knowledge base."}

# Replace this with your actual knowledge base data structure (dictionary)
knowledge_base = {
  # Sample entries in your knowledge base


  "functions": {
    "question": "What are functions in Python?",
    "answer": "Functions are reusable blocks of code that perform specific tasks. They can take arguments (inputs) and return values (outputs). Functions help in organizing code and making it more modular.",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.w3schools.com/python/python_functions.asp"
  },

  "lists": {
    "question": "What are lists in Python?",
    "answer": "Lists are ordered collections of items. They can store different data types (like integers, strings, or even other lists) and are mutable (elements can be changed after creation).",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.tutorialspoint.com/python/python_lists.htm"
  },

  "dictionaries": {
    "question": "What are dictionaries in Python?",
    "answer": "Dictionaries are unordered collections of key-value pairs. Keys are unique and used to access the corresponding values. Dictionaries are useful for storing and organizing data based on keys.",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.programiz.com/python/dictionary/"
  },

  "conditional statements": {
    "question": "What are conditional statements in Python?",
    "answer": "Conditional statements allow you to control the flow of your program based on certain conditions. They use keywords like 'if', 'elif', and 'else' to execute different code blocks depending on whether a condition is True or False.",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.w3schools.com/python/python_conditional_statements.asp"
  },

  "strings": {
    "question": "What are strings in Python?",
    "answer": "Strings are sequences of characters. They are used to represent text data. Strings are immutable (their content cannot be changed after creation).",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.tutorialspoint.com/python/python_strings.htm"
  },

  "operators": {
    "question": "What are operators in Python?",
    "answer": "Operators are special symbols that perform operations on values. Python has various operators like arithmetic operators (+, -, *, /), comparison operators (==, !=, <, >), and logical operators (and, or, not).",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.guru99.com/python-operators.htm"
  },

  "modules": {
    "question": "What are modules in Python?",
    "answer": "Modules are reusable Python code files. They contain functions, classes, and variables that can be imported and used in other Python scripts. Modules help in code organization and reusability.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://www.datacamp.com/tutorial/modules-in-python"
  },

  "classes": {
    "question": "What are classes in Python?",
    "answer": "Classes are blueprints for creating objects. They define properties (attributes) and functionalities (methods) that objects of that class will inherit. Classes are fundamental for object-oriented programming in Python.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://www.tutorialspoint.com/python/python_classes.htm"
  },

"input/output": {
    "question": "How to get user input and print output in Python?",
    "answer": "Python provides functions to get user input (using the 'input' function) and display output (using the 'print' function). These functions are essential for interacting with users in your programs.",
    "difficulty_level": "beginner",
    "additional_resources": "Link",
},

"tuples": {
    "question": "What are tuples in Python?",
    "answer": "Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation. They are ordered collections of items and can store different data types.",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.tutorialspoint.com/python/python_tuples.htm"
  },

  "sets": {
    "question": "What are sets in Python?",
    "answer": "Sets are unordered collections of unique elements. They are useful for tasks like membership testing and eliminating duplicate entries from other collections.",
    "difficulty_level": "beginner",
    "additional_resources": "https://realpython.com/python-sets/"
  },

  "file handling": {
    "question": "What is file handling in Python?",
    "answer": "File handling in Python allows you to work with files on the filesystem. You can open, read, write, and close files using built-in functions and methods.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files"
  },

  "exception handling": {
    "question": "What is exception handling in Python?",
    "answer": "Exception handling is a mechanism to deal with runtime errors in Python. It allows you to catch and handle exceptions gracefully, preventing your program from crashing.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/python-exceptions/"
  },

  "generators": {
    "question": "What are generators in Python?",
    "answer": "Generators are functions that allow you to generate a sequence of values lazily. They produce values one at a time and are memory efficient compared to lists.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/introduction-to-python-generators/"
  },
  
}
  # ... add more entries for other concepts ...
def main():
  while True:
    user_query = input("Enter a question about programming (or 'quit' to exit): ")
    if user_query.lower() == 'quit':
      break
    
    concept_info = get_explanation(user_query)
    explanation = concept_info["answer"]
    difficulty_level = concept_info["difficulty_level"]
    additional_resources = concept_info.get("additional_resources", None)
    
    print(f"\nExplanation for {user_query}:")
    print(explanation)
    if additional_resources:
      print(f"\nAdditional Resources: {additional_resources}")

if __name__ == "__main__":
  main()
