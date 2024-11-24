import threading
import time
from queue import Queue

# Buffer size
BUFFER_SIZE = 5

# Shared buffer
buffer = Queue(maxsize=BUFFER_SIZE)

# Producer task
def producer():
    for i in range(10):  # Produce 10 items
        item = f"Item {i}"
        buffer.put(item)  # Wait if buffer is full
        print(f"Producer produced: {item}")
        time.sleep(1)

# Consumer task
def consumer():
    for i in range(10):  # Consume 10 items
        item = buffer.get()  # Wait if buffer is empty
        print(f"Consumer consumed: {item}")
        time.sleep(2)  # Simulate slower consumption

# Create threads for producer and consumer
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()

print("Producer and Consumer tasks completed.")
