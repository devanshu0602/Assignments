# Import the required libraries
import threading


# Initialize a mutex to 1
mutex = threading.Semaphore(1)
# Number of full slots as 0
full = 0
# Number of empty slots as size of buffer
empty = 10
x = 0


# Function to produce an item and add it to the buffer
def producer():
    global mutex, full, empty, x
    # Decrease mutex value by 1
    mutex.acquire()
    # Increase the number of full slots by 1
    full += 1
    # Decrease the number of empty slots by 1
    empty -= 1
    # Item produced
    x += 1
    print("Producer produces item", x, "\n")
    # Increase mutex value by 1
    mutex.release()


# Function to consume an item and remove it from buffer
def consumer():
    global mutex, full, empty, x
    # Decrease mutex value by 1
    mutex.acquire()
    # Decrease the number of full slots by 1
    full -= 1
    # Increase the number of empty slots by 1
    empty += 1
    print("Consumer consumes item", x, "\n")
    x -= 1
    # Increase mutex value by 1
    mutex.release()


# Driver Code
if __name__ == '__main__':
    print("Devanshu Gupta [21BCE0597]\n")
    print("1. Press 1 for Producer")
    print("2. Press 2 for Consumer")
    print("3. Press 3 for Exit")
    while True:
        n = int(input("Enter your choice: "))
        # Switch Cases
        if n == 1:
            # If mutex is 1 and empty is non-zero, then it is possible to produce
            if (mutex._value == 1 and empty != 0):
                producer()
            # Otherwise, print buffer is full
            else:
                print("Buffer is full!")
        elif n == 2:
            # If mutex is 1 and full is non-zero, then it is possible to consume
            if (mutex._value == 1 and full != 0):
                consumer()
            # Otherwise, print Buffer is empty
            else:
                print("Buffer is empty!")
        elif n == 3:
            break