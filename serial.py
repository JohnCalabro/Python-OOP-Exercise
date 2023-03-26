"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        self.start = self.next = start  #start will be next each time so it counts up?
    def counter(self):
        
        self.next += 1
        return self.next - 1
    def __repr__(self):
        return f"start = {self.start} next = {self.next}"
    def reset(self):
        self.next = self.start # next val is now the start val which resets it





    



