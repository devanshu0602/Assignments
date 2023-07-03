import threading
import time


# Shared variables
turn = 0
flag = [False, False]


# Process 0
def process_0():
    global turn, flag
    while True:
        # Set flag[0] to indicate process 0 wants to enter the critical section
        flag[0] = True
        turn = 1
        # Wait until it's process 0's turn and process 1 is not in its critical section
        while flag[1] and turn == 1:
            time.sleep(1)
        # Critical section
        print("Process 0 is in the critical section")
        # Reset flag[0] to indicate process 0 is done with the critical section
        flag[0] = False
        # Remainder section


# Process 1
def process_1():
    global turn, flag
    while True:
        # Set flag[1] to indicate process 1 wants to enter the critical section
        flag[1] = True
        turn = 0
        # Wait until it's process 1's turn and process 0 is not in its critical section
        while flag[0] and turn == 0:
            time.sleep(1)
        # Critical section
        print("Process 1 is in the critical section")
        # Reset flag[1] to indicate process 1 is done with the critical section
        flag[1] = False
        # Remainder section


# Create and start the threads
if __name__ == '__main__':
    print("Devanshu Gupta\n")
    thread_0 = threading.Thread(target=process_0)
    thread_1 = threading.Thread(target=process_1)
    thread_0.start()
    thread_1.start()
