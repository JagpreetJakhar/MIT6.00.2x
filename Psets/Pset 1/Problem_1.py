def greedy_cow_transport(cows,limit=10):
    trips = []
    cowsCopy = cows.copy()
    sortedCows=sorted(cowsCopy.items(), key=lambda x:x[1], reverse = True)#sorted and reversed to have weights in descending order
    print(sortedCows)
    while sum(cowsCopy.values())>0:
        ship =[]
        total =0
        for i,w in sortedCows:
            if cowsCopy[i] != 0 and w + total <= limit :
                ship.append(i)
                total +=w
                cowsCopy[i]=0
        trips.append(ship)
    return trips
"""Test Cases :
  greedy_cow_transport({'Louis': 45, 'Miss Bella': 15, 'Muscles': 65, 'Patches': 60,\
  'Lotus': 10, 'Polaris': 20, 'MooMoo': 85, 'Clover': 5, 'Horns': 50, 'Milkshake': 75}, 100)
  
  greedy_cow_transport({'Willow': 35, 'Dottie': 85, 'Patches': 12, 'Daisy': 50, 'Lilly': 24, \
  'Buttercup': 72, 'Betsy': 65, 'Coco': 10, 'Abby': 38, 'Rose': 50}, 100)
  
  greedy_cow_transport({'Willow': 59, 'Buttercup': 11, 'Luna': 41, \
  'Betsy': 39, 'Starlight': 54, 'Coco': 59, 'Abby': 28, 'Rose': 42}, 120)
  
  
  """
greedy_cow_transport({'Willow': 35, 'Dottie': 85, 'Patches': 12, 'Daisy': 50, 'Lilly': 24, \
'Buttercup': 72, 'Betsy': 65, 'Coco': 10, 'Abby': 38, 'Rose': 50}, 100)

