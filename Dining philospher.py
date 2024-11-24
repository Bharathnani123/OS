import threading
import time

# Number of philosophers and forks
NUM_PHILOSOPHERS = 5

# Semaphore to represent each fork
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

# Philosophers' tasks
def philosopher(philosopher_id):
    while True:
        print(f"Philosopher {philosopher_id} is thinking.")
        time.sleep(1)

        # Pick up forks
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % NUM_PHILOSOPHERS

        print(f"Philosopher {philosopher_id} is hungry.")
        forks[left_fork].acquire()
        forks[right_fork].acquire()

        # Eating
        print(f"Philosopher {philosopher_id} is eating.")
        time.sleep(1)

        # Put down forks
        forks[right_fork].release()
        forks[left_fork].release()
        print(f"Philosopher {philosopher_id} finished eating.")

# Create threads for each philosopher
threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]

# Start all threads
for t in threads:
    t.start()

# Join threads (in a real application, we might want to stop them gracefully)
for t in threads:
    t.join()
