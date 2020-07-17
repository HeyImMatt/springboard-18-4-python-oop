from random import choice

class WordFinder:
  """Reads words from a file and provides a method to generate a random word"""

  def __init__(self, path='words.txt'):
    """Initializes by opening the default words list or a user-provided path, 
    reads the words list, and tells user how many words are in the list"""

    self.path = path

    with open(self.path) as f:
        self.words = f.readlines()

    self.list_length()

  def list_length(self):
    self.count = len(self.words)
    
    print(f'{self.count} words read')

  def random(self):
    """Generates a random word from the list"""
    rand_word = choice(self.words)
    return rand_word[:-1]


