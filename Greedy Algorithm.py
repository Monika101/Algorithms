###########################
# 6.00.2x Problem Set 1: Space Cows 

#from ps1_partition import get_partitions
#import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows():
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
#
#    cow_dict = dict()
#
#    f = open('C:/Users/Monika/Documents/MIT600/MIT 600.2x/ps1_cow_data.txt')
#    
#    for line in f:
#        line_data = line.split(',')
#        cow_dict[line_data[0]] = int(line_data[1])
#    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

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
  
    keys = list(cows.keys())
    keys = sorted(keys, key = cows.__getitem__, reverse = True)

    l = []

    k = [cows[keys[0]]]

    while keys:
    
        sub_out = [keys.pop(0)]
        pop_list = []
    
        for index, item in enumerate(keys):
        
            if cows[item] + sum(k) <= limit:
        
                sub_out.append(item)
                k.append(cows[item])
                pop_list.append(index)
           
        l.append(sub_out)
        try: 
            k = [cows[keys[0]]]
        except IndexError:
            pass

        for index in reversed(pop_list):
            keys.pop(index)
                 
    return l
    

# Problem 2dict
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
#    # TODO: Your code here
#    answer = []
#    shortest_comb = len(cows) + 1
#    for combination in get_partitions(cows):
#        correct = True #all trips respect weight limit   
#        for trip in combination:
#            weight = 0
#            for cow_name in trip:
#                weight += cows[cow_name]
#            if weight > limit:
#                correct = False
#                break
#        if correct == True and len(combination) < shortest_comb:
#            answer = combination
#            shortest_comb = len(combination)
#    return answer
#    
#        

        
# Problem 3
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
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#limit=100
#print(cows)
#
#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))


