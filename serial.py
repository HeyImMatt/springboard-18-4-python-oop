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
    def __init__(self, start):
        """Create SerialGenerator with a starting number"""

        self.start = start
        self.counter = 0

    def generate(self):
        """Generate a serial number that increments 1 each time"""
        
        if self.counter == 0:
            self.counter += 1
            return self.start
        else:
            self.counter += 1
            self.start += 1
            return self.start
        
    
