#!/usr/bin/python3
'''
task_03_countediterator module with CountedIterator class
'''


class CountedIterator:
    '''
    CountedIterator class
    '''
    def __init__(self, iterable):
        self.iterator_obj = iter(iterable)
        self.counter = 0
    
    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iterator_obj)
        except IndexError:
            raise StopIteration()
        self.counter += 1
        return item
        
