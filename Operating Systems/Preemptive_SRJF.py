# Find the waiting time
def findWaitingTime(processes, n, waiting_time):
	remaining_time = [0] * n
	for i in range(n):
		remaining_time[i] = processes[i][1]
	complete = 0
	t = 0
	minimum = 999999
	s = 0
	check = False
	while (complete != n):
		for j in range(n):
			if ((processes[j][2] <= t) and (remaining_time[j] < minimum) and remaining_time[j] > 0):
				minimum = remaining_time[j]
				s = j
				check = True
		if (check == False):
			t += 1
			continue
		remaining_time[s] -= 1
		minimum = remaining_time[s]
		if (minimum == 0):
			minimum = 999999
		if (remaining_time[s] == 0):
			complete += 1
			check = False
			# Find finish time of current
			fint = t + 1
			# Calculate waiting time
			waiting_time[s] = (fint - process_id[s][1] - process_id[s][2])
			if (waiting_time[s] < 0):
				waiting_time[s] = 0
		t += 1


# Function to calculate turn around time
def findTurnAroundTime(processes, n, waiting_time, turn_around_time):
	for i in range(n):
		turn_around_time[i] = processes[i][1] + waiting_time[i]
		

# Function to calculate average
def findAverage(processes, n):
	waiting_time = [0] * n
	turn_around_time = [0] * n
	findWaitingTime(processes, n, waiting_time)
	findTurnAroundTime(processes, n, waiting_time, turn_around_time)
	# Display processes along with all details
	print("Processes \tBT	 WT	 TAT")
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + waiting_time[i]
		total_tat = total_tat + turn_around_time[i]
		print(" ", processes[i][0], "\t\t", processes[i][1], "\t", waiting_time[i], "\t", turn_around_time[i])
	print("\nAverage waiting time = %.3f " % (total_wt / n))
	print("Average turn around time = ", total_tat / n)


# Driver code
if __name__ == "__main__":
	print("\nDevanshu Gupta\n")
	process_id = [[1, 6, 1], [2, 8, 1], [3, 7, 2], [4, 3, 3]]
	n = 4
	findAverage(process_id, n)
	print("\nDevanshu Gupta\n")
