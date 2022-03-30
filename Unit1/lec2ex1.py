"""Very Tricky Problem"""
def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    n = len(items)
    for i in range(3**n):
        bag1=[]#list so as to append
        bag2=[]
        for j in range(n):
            if(i//3**j)%3==0:
                bag1.append(items[j])
            elif(i//3**j)%3==1:
                bag2.append(items[j])
        yield (bag1,bag2)#give tuple back
        """Why use (i//3**j) instead of (i>>j)?
        READ:https://realpython.com/python-bitwise-operators/
        """
       
        

        
   
        
