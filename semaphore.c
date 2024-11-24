#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

// Semaphore declaration
sem_t semaphore;

// Function executed by threads
void* thread_function(void* arg) {
    int thread_id = *(int*)arg;

    printf("Thread %d is waiting for the semaphore...\n", thread_id);

    // Wait (P operation)
    sem_wait(&semaphore);
    printf("Thread %d has entered the critical section.\n", thread_id);

    // Simulate critical section
    sleep(2);

    printf("Thread %d is leaving the critical section.\n", thread_id);

    // Signal (V operation)
    sem_post(&semaphore);
    
    return NULL;
}

int main() {
    pthread_t threads[3];
    int thread_ids[3] = {1, 2, 3};

    // Initialize the semaphore with value 1
    sem_init(&semaphore, 0, 1);

    // Create threads
    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, thread_function, &thread_ids[i]);
    }

    // Wait for all threads to complete
    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }

    // Destroy the semaphore
    sem_destroy(&semaphore);

    printf("All threads have completed execution.\n");

    return 0;
}
