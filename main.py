import math
import random
import time 
def calculate_distance_ordery():
    distance=0;
    for i in range (no_of_city):
        distance=distance+int(input_array[order[i]][order[i+1]])
    return distance




if __name__ == "__main__":
    start_time=time.time()

    global temperatue
    temperatue=700

    global no_of_loop
    no_of_loop=100000

    global alpha
    alpha=0.95

    global no_of_city
    no_of_city=17

    global input_array

    #open .txt file
    input_file=open("gr17_d.txt","r")
    line=input_file.readline()
    line=line.strip().split()
    input_array = [[0 for x in range (no_of_city)] for y in range (no_of_city)]

    # initial order of the city
    order=[i for i in range (no_of_city)]
    order.append(0)
    row =0

    #read file and stored into an array
    while line :
        input_array[row]=line
        line=input_file.readline();
        line=line.strip().split()
        row =row+1

    distance=0;
    #Current found minimum distance
    minimum_distance=100000
    #assuming currently best solution be intial solution
    current_best_solution=order
    for x in range (no_of_loop):
        distance=calculate_distance_ordery()
        if distance<minimum_distance:
            #found a better solution
            minimum_distance=distance;
            current_best_solution=order;

        else:
            distance_difference = distance-minimum_distance;
            hop_probability = math.exp(-distance_difference/temperatue)
            if random.random() < hop_probability:
                minimum_distance = distance
                current_best_solution = order

        #Setting for next iteration
        swapping_location_a = random.randint(0,16)
        swapping_location_b = random.randint(0,16)
        while swapping_location_a == swapping_location_b:
            swapping_location_b=random.randint(0,16)
        temp_location=order[swapping_location_a]
        order[swapping_location_a]=order[swapping_location_b]
        order[swapping_location_b]=temp_location

        if x>0:
            #preventing changing the temperature in the first iteration
            temperatue=temperatue*alpha

    print(current_best_solution)
    print(minimum_distance)
    print("--- %s seconds ---" % (time.time() - start_time))






