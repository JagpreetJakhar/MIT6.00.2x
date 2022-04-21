def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start=time.time()
    print(greedy_cow_transport(cows, 10))
    end=time.time()
    print('Greedy Time: ', end-start)

    start2=time.time()
    print(brute_force_cow_transport(cows, 10))
    end2=time.time()
    print('Brute Time',end2-start2)
