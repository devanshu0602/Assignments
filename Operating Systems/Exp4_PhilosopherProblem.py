# importing the required libraries
import threading
import time
import random


# Philosopher thread function
def philosopher(index):
	while True:
		print(f"Philosopher {index} is THINKING. | ")
		t = random.randint(1, 5)
		time.sleep(t)
		mutex.acquire()
		leftChopstickIndex = index
		rightChopstickIndex = (index + 1) % numOfChopsticks
		chopsticks[leftChopstickIndex].acquire()
		chopsticks[rightChopstickIndex].acquire()
		mutex.release()
		print(f"Philosopher {index} is EATING. | ")
		t = random.randint(1, 5)
		time.sleep(t)
		chopsticks[leftChopstickIndex].release()
		chopsticks[rightChopstickIndex].release()


# MAIN FUNCTION
# Header
print("Devanshu Gupta\n")
# Number of philosophers and chopsticks
numOfPhilosophers = int(input("Enter the number of philosophers: "))
numOfChopsticks = numOfPhilosophers
# Defining semaphores for chopsticks and the mutex
chopsticks = [threading.Semaphore(1) for i in range(numOfChopsticks)]
mutex = threading.Semaphore(1)
# Create a thread for each philosopher
philosopher_threads = []
for i in range(numOfPhilosophers):
	philosopher_threads.append(threading.Thread(target=philosopher, args=(i,)))
# Start the philosopher threads
for thread in philosopher_threads:
	thread.start()
# Wait for the philosopher threads to complete
for thread in philosopher_threads:
	thread.join()
