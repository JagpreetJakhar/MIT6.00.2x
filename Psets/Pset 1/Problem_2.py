def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trips=[]
    parts=sorted(get_partitions(cows),key=len)
    solutions=[]
    for i in parts: #enter sorted partitions
        ships=[]
        for j in i : #iterate over each partition
            weights=[]
            for k in j: #get weight of each cow in each partition
                weights.append(cows[k])
            ships.append(sum(weights))
        if all(d <= limit for d in ships):
            solutions.append(i)
        #This may contain repeats of same solutions
    cleaned_solutions=[]
    for w in solutions:
        if w not in cleaned_solutions:
            cleaned_solutions.append(w)
    #now search for min length list
    best_sol=min(map(len,cleaned_solutions))
    for m in cleaned_solutions:
        if len(m) == best_sol :
            return m
