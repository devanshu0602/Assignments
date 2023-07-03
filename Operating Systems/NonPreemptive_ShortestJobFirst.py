# Print the final table
def print_values(arrival_time, burst_time, completion_time, turn_around_time, waiting_time):
    n = len(arrival_time)
    for i in range(0, n):
        print("Process[" + str(i + 1) + "]: "
              + str(arrival_time[i]) + " | "
              + str(burst_time[i]) + " | "
              + str(completion_time[i]) + " | "
              + str(turn_around_time[i]) + " | "
              + str(waiting_time[i]))


# Find the average time
def find_average(values):
    sum_of_values = 0
    for i in values:
        sum_of_values += i
    avg = sum_of_values/len(values)
    return avg


# Sort w.r.t. the burst time
def sort_wrt_BT(start, n, arrival_time, burst_time):
    n = len(burst_time)
    for i in range(start, n-1):
        for j in range(start, n-i-1):
            if burst_time[j] > burst_time[j+1]:
                # swap the values
                burst_time[j], burst_time[j+1] = burst_time[j+1], burst_time[j]
                arrival_time[j], arrival_time[j+1] = arrival_time[j+1], arrival_time[j]


# Sort w.r.t. the arrival time
def sort_wrt_AT(n, arrival_time, burst_time):
    n = len(arrival_time)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arrival_time[j] > arrival_time[j+1]:
                # swap the values
                arrival_time[j], arrival_time[j+1] = arrival_time[j+1], arrival_time[j]
                burst_time[j], burst_time[j+1] = burst_time[j+1], burst_time[j]


# Creation of the table of details
def shortestJobFirst(n, arrival_time, burst_time):
    # Calculating Completion time
    completion_time = [0]
    completion_time[0] = burst_time[0] + arrival_time[0]
    for i in range(1, n):
        sort_wrt_BT(i, n, arrival_time, burst_time)
        if arrival_time[i] < completion_time[i-1]:
            completion_time.append(completion_time[i-1] + burst_time[i])
        else:
            completion_time.append(arrival_time[i] + burst_time[i])
    # Calculating Turn Around Time
    turn_around_time = []
    for i in range(0, n):
        turn_around_time.append(completion_time[i] - arrival_time[i])
    # Calculating Waiting Time
    waiting_time = []
    for i in range(0, n):
        waiting_time.append(turn_around_time[i] - burst_time[i])
    # Print the table
    print("\nAfter Calculations:")
    print("Process[i]: AT | BT | CT | TAT | WT")
    print_values(arrival_time, burst_time, completion_time,
                 turn_around_time, waiting_time)
    # Find the average TAT and WT
    avg_TAT = find_average(turn_around_time)
    print("\nThe average Turn Around Time = " + str(avg_TAT))
    avg_WT = find_average(waiting_time)
    print("The average Waiting Time = " + str(avg_WT))


# ------- Main Function --------
print("\nDevanshu Gupta\n")
# Number of processes
n = int(input("Enter the number of Processes: "))
# Arrival & Burst time
arrival_time = []
burst_time = []
print("Enter the Arrival Time of each process:")
for i in range(0, n):
    arrival_time.append(int(input()))
print("Enter the Burst Time of each process:")
for i in range(0, n):
    burst_time.append(int(input()))
# Print given inputs
print("\nGiven:")
print("Process[i]: AT | BT | CT | TAT | WT")
for i in range(0, n):
    print("Process[" + str(i + 1) + "]: "
          + str(arrival_time[i]) + " | "
          + str(burst_time[i]))
# Sorting the table for execution of the Shortest Job First.
sort_wrt_AT(n, arrival_time, burst_time)
# Create the table and calculate the values
shortestJobFirst(n, arrival_time, burst_time)
print("\nDevanshu Gupta\n")
