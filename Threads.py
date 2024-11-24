import threading
import time

# Task for the first thread: Counting numbers
def count_numbers():
    for i in range(1, 6):  # Count from 1 to 5
        print(f"Count: {i}")
        time.sleep(1)  # Simulate a time-consuming task (1 second delay)

# Task for the second thread: Printing letters
def print_letters():
    for letter in "ABCDE":  # Iterate through letters A to E
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulate a time-consuming task (1 second delay)

# Creating two threads for the tasks
thread1 = threading.Thread(target=count_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting both threads
thread1.start()
thread2.start()

# Waiting for both threads to complete
thread1.join()
thread2.join()

# Final message after both threads complete
print("Both tasks completed.")
