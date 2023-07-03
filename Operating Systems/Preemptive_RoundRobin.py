# Find the waiting time
def findWaitingTime(processes, n, burst_time, waiting_time, time_quantum):
	remaining_BT = [0] * n
	for i in range(n):
		remaining_BT[i] = burst_time[i]
	time = 0
	while (1):
		done = True
		for i in range(n):
			if (remaining_BT[i] > 0):
				done = False
				if (remaining_BT[i] > time_quantum):
					time += time_quantum
					remaining_BT[i] -= time_quantum
				else:
					time = time + remaining_BT[i]
					waiting_time[i] = time - burst_time[i]
					remaining_BT[i] = 0
		if (done == True):
			break


# Find the Turn Around Time
def findTurnAroundTime(processes, n, burst_time, waiting_time, turn_around_time):
	for i in range(n):
		turn_around_time[i] = burst_time[i] + waiting_time[i]


# Calculate average
def averageTime(processes, n, burst_time, time_quantum):
	waiting_time = [0] * n
	turn_around_time = [0] * n
	# Find waiting time
	findWaitingTime(processes, n, burst_time, waiting_time, time_quantum)
	# Find turn around time
	findTurnAroundTime(processes, n, burst_time, waiting_time, turn_around_time)
	# Print all details
	print("Processes \t BT	  WT    TAT")
	total_WT = 0
	total_TAT = 0
	for i in range(n):
		total_WT = total_WT + waiting_time[i]
		total_TAT = total_TAT + turn_around_time[i]
		print(" ", i + 1, "\t\t", 
	          burst_time[i], "\t ",
	          waiting_time[i], "\t", 
	          turn_around_time[i])
	print("\nAverage waiting time = %.3f " % (total_WT / n))
	print("Average turn around time = %.3f " % (total_TAT / n))


# Driver code
if __name__ == "__main__":
	print("\nDevanshu Gupta\n")
	# Process id's
	process_id = [1, 2, 3, 4, 5]
	n = 5
	# Burst time of all processes
	burst_time = [3, 5, 2, 5, 5]
	# Time quantum
	time_quantum = 2
	averageTime(process_id, n, burst_time, time_quantum)
	print("\nDevanshu Gupta\n")
