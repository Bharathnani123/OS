def fcfs(processes, burst_times):
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n

    # Calculate waiting and turnaround times
    for i in range(1, n):
        waiting_times[i] = waiting_times[i - 1] + burst_times[i - 1]
    turnaround_times = [waiting_times[i] + burst_times[i] for i in range(n)]

    # Display results
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i]}\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
    print(f"\nAverage Waiting Time: {sum(waiting_times) / n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_times) / n:.2f}")


# Input Section
process_ids = list(map(int, input("Enter Process IDs: ").split()))
burst_times = list(map(int, input("Enter Burst Times: ").split()))

# Call the function
fcfs(process_ids, burst_times)

