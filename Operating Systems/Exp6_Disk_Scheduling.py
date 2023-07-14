# ----------------- FCFS -----------------
# Function to perform FFCS
def FFCS(starting_position, request_queue):
    found = 0
    current_position = starting_position
    iterator = 0
    total_track_movements = 0
    while found < len(request_queue):
        print(f"---- To find {request_queue[iterator]} ----")
        print(f"Track movements = {total_track_movements} + ", end="")
        total_track_movements = total_track_movements + (abs(request_queue[iterator] - current_position))
        print(f"abs({request_queue[iterator]} - {current_position}) = {total_track_movements}")
        current_position = request_queue[iterator]
        found = found + 1
        iterator = iterator + 1
    return total_track_movements
# ----------------------------------------


# ----------------- SSTF -----------------
# Function to perform SSTF
def SSTF(starting_position, request_queue):
    INF = 9999999
    found = 0
    current_position = starting_position
    total_track_movements = 0
    difference = []
    visited = [0] * len(request_queue)
    while found < len(request_queue):
        # find the distance between current position and all other positions
        for i in range(0, len(request_queue)):
            difference.append(abs(current_position - request_queue[i]))
        # check if that positioin is already visited
        for j in range(0, len(request_queue)):
            if visited[j] == 1:
                difference[j] = INF
        # closest position is set as next destination
        index_of_closest = difference.index(min(difference))
        print(f"---- Closest value is {request_queue[index_of_closest]} ----")
        print(f"Track movements = {total_track_movements} + ", end="")
        total_track_movements = total_track_movements + abs(request_queue[index_of_closest] - current_position)
        print(f"abs({request_queue[index_of_closest]} - {current_position}) = {total_track_movements}")
        current_position = request_queue[index_of_closest]
        found = found + 1
        visited[index_of_closest] = 1
        difference.clear()
    return total_track_movements
# ----------------------------------------


# Main function
if __name__ == '__main__':
    # Header
    print("\nDevanshu Gupta [21BCE0597]\n")
    # Number of tracks
    num_of_tracks = int(input("Enter the number of tracks: "))
    # Values to look for (request queue)
    request_queue = []
    print("\nEnter the values in request queue (type 'end' to stop):")
    while True:
        val = input()
        if val == 'end':
            break
        else:
            request_queue.append(int(val))
    # Starting position of the R/W head
    starting_position = int(input("\nEnter the starting position of the R/W head: "))
    # Time taken to move from one track to another
    track_change_time = int(input("\nEnter the time taken to move from one track to another (ns): "))
    # Choice to perform FCFS or SSTF
    print("\nAlgorithm to be used:")
    choice = int(input("1. FFCS - First Come First Serve\n2. SSTF - Shortest Seek Time First\n\nEnter choice: "))
    print()
    # Perform operations
    if choice == 1:
        total_track_movements = FFCS(starting_position, request_queue)
    elif choice == 2:
        total_track_movements = SSTF(starting_position, request_queue)
    else:
        print("!! Invalid choice. !!")
    # Total seek time
    total_seek_time = total_track_movements * track_change_time
    # Print the result
    print(f"\n=> The total number of track movements = {total_track_movements}")
    print(f"\n=> The total seek time = {total_seek_time} ns")
    # Footer
    print("\nDevanshu Gupta [21BCE0597]\n")