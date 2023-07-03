def find_highest_priority(processes, arrival_times, burst_times, priorities, current_time):
    highest_priority = float('inf')
    highest_priority_index = -1
    for i in range(len(processes)):
        if arrival_times[i] <= current_time and priorities[i] < highest_priority and burst_times[i] > 0:
            highest_priority = priorities[i]
            highest_priority_index = i
    return highest_priority_index


def Priority(processes, arrival_times, burst_times, priorities):
    n = len(processes)
    remaining_burst_times = burst_times.copy()
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n
    current_time = 0
    completed_processes = 0
    while completed_processes < n:
        highest_priority_index = find_highest_priority(
            processes, arrival_times, remaining_burst_times, priorities, current_time)
        if highest_priority_index == -1:
            current_time += 1
            continue
        remaining_burst_times[highest_priority_index] -= 1
        if remaining_burst_times[highest_priority_index] == 0:
            completion_times[highest_priority_index] = current_time + 1
            turnaround_times[highest_priority_index] = completion_times[highest_priority_index] - \
                arrival_times[highest_priority_index]
            waiting_times[highest_priority_index] = turnaround_times[highest_priority_index] - \
                burst_times[highest_priority_index]
            completed_processes += 1
        current_time += 1
    print("Process\t  AT\tBT\tP\tCT\tWT\tTAT")
    for i in range(n):
        print(f"{processes[i]}\t  {arrival_times[i]}\t{burst_times[i]}\t{priorities[i]}\t{completion_times[i]}\t{waiting_times[i]}\t{turnaround_times[i]}")
    # Find Average Waiting Time
    print("\nAverage Waiting Time = " + str(sum(waiting_times)/n))
    # Find Average Turn Around Time
    print("Average Turn Around Time = " + str(sum(turnaround_times)/n))


# Main Function
print("\nDevanshu Gupta [21BCE0597]\n")
processes = ['P1', 'P2', 'P3', 'P4', 'P5']
arrival_times = [0, 1, 2, 3, 4]
burst_times = [3, 5, 2, 5, 5]
priorities = [3, 2, 1, 4, 5]
Priority(processes, arrival_times, burst_times, priorities)
print("\nDevanshu Gupta [21BCE0597]\n")