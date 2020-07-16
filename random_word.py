class WordFinder:
  """Reads words from a file and provides a method to generate a random word"""

  def __init__(self, path='words.txt'):
    """Initializes by opening the default words list or a user-provided path, 
    reads the words list, and tells user how many words are in the list"""
    
    self.path = path
    self.words = open(self.path, 'r').readlines( )

    count = len(self.words)
    
    print(f'{count} words read')