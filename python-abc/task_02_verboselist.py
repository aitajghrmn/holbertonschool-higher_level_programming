#!/usr/bin/python3
'''
task_02_verboselist module with VerboseList class
'''

# append, extend, remove, and pop.
class VerboseList(list):
    '''
    class VerboseList
    '''
    def append(self, item):
        '''
        overrided append method
        '''
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        '''
        overrided extend method
        '''
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        '''
        overrided remove method
        '''
        try:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        except ValueError:
            print("Item is not in the list")
        
    def pop(self, index=-1):
        '''
        overrided remove method
        '''
        try:
            print(f"Popped [{self[index]}] from the list")
            item = super().pop(index)
            return item
        except IndexError:
            print("No item at this index in list")
        
