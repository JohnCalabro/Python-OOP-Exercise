"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    # will write my understanding next to this solution, instructions confused me,
    # but the code makes sense, I see what it is doing:
    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)   # opens words.txt when instantiated,
        # ^ wf = WordFinder("simple.txt")


        self.words = self.parse(dict_file) # gives us access to vast list of words

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        
        return [w.strip() for w in dict_file] # make words into list to be cycled 
        #through by choice when we call the random class method
        

    def random(self):
        """Return random word."""

        return random.choice(self.words) # using choice method from random module,
        # returns a random word


class SpecialWordFinder(WordFinder): # class from above passed in
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
        # ^ return only if the line is occupied or does NOT begin with #
