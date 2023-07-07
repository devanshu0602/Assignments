def First_Fit(block_size_ff, num_of_blocks, process_size, num_of_processes):
	allocated_block = [-1] * num_of_processes
	# Memory allocation
	for process in range(0, num_of_processes):
		for block in range(0, num_of_blocks):
			if block_size_ff[block] >= process_size[process]:
				allocated_block[process] = block
				block_size_ff[block] = block_size_ff[block] - process_size[process]
				break
	# Table of allocated memory
	print("Memory Table:")
	print("P_id.  \tProcess Size \tAllocated Block")
	for process in range(0, num_of_processes):
		print(" ", process, "\t", process_size[process], "\t\t", end="")
		if allocated_block[process] == -1:
			print("Not Allocated")
		else:
			print("   ", allocated_block[process])


def Best_Fit(block_size_bf, num_of_blocks, process_size, num_of_processes):
	allocated_block = [-1] * num_of_processes
	# Memory allocation
	for process in range(num_of_processes):
		min_value_index = -1
		for block in range(num_of_blocks):
			if block_size_bf[block] >= process_size[process]:
				if min_value_index == -1:
					min_value_index = block
				elif block_size_bf[min_value_index] > block_size_bf[block]:
					min_value_index = block
		if min_value_index != -1:
			allocated_block[process] = min_value_index
			block_size_bf[min_value_index] -= process_size[process]
	# Table of allocated memory
	print("Memory Table:")
	print("P_id.  \tProcess Size \tAllocated Block")
	for process in range(0, num_of_processes):
		print(" ", process, "\t", process_size[process], "\t\t", end="")
		if allocated_block[process] == -1:
			print("Not Allocated")
		else:
			print("   ", allocated_block[process])


def Worst_Fit(block_size_wf, num_of_blocks, process_size, num_of_processes):
	allocated_block = [-1] * num_of_processes
	# Memory allocation
	for process in range(0, num_of_processes):
		for block in range(0, num_of_blocks):
			if process_size[process] <= block_size_wf[block]:
				allocated_block[process] = block_size_wf.index(max(block_size_wf))
				block_size_wf[allocated_block[process]] = block_size_wf[allocated_block[process]] - process_size[process]
				break
	# Table of allocated memory
	print("Memory Table:")
	print("P_id.  \tProcess Size \tAllocated Block")
	for process in range(0, num_of_processes):
		print(" ", process, "\t", process_size[process], "\t\t", end="")
		if allocated_block[process] == -1:
			print("Not Allocated")
		else:
			print("   ", allocated_block[process])


# Main Function
if __name__ == '__main__':
	# Header
	print("\nDevanshu Gupta [21BCE0597]\n")
	# Details of blocks
	num_of_blocks = int(input("Enter the number of blocks: "))
	block_size = []
	for i in range(0, num_of_blocks):
		block_size.append(int(input(f"Enter the size of Block {i}: ")))
	print()
	# Details of processes
	num_of_processes = int(input("Enter the number of processes: "))
	process_size = []
	for i in range(0, num_of_processes):
		process_size.append(int(input(f"Enter the size of Process {i}: ")))
	print()
	# Given
	print("Given Block Sizes:")
	print("|", end="")
	for i in range(0, num_of_blocks):
		print(f" P{i} = {block_size[i]} |", end="")
	print()
	# Call the memory allocation functions
	block_size_ff = block_size.copy()
	block_size_bf = block_size.copy()
	block_size_wf = block_size.copy()
	print("\n--------------- Using FIRST FIT ---------------")
	First_Fit(block_size_ff, num_of_blocks, process_size, num_of_processes)
	print("\n--------------- Using BEST FIT ---------------")
	Best_Fit(block_size_bf, num_of_blocks, process_size, num_of_processes)
	print("\n--------------- Using WORST FIT ---------------")
	Worst_Fit(block_size_wf, num_of_blocks, process_size, num_of_processes)
    # Footer
	print("\nDevanshu Gupta [21BCE0597]\n")