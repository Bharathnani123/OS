def round_robin(processes, burst_times, time_quantum):
    n = len(processes)
    remaining_burst_times = burst_times[:]
    waiting_times = [0] * n
    turnaround_times = [0] * n
    time = 0

    while any(remaining_burst_times):
        for i in range(n):
            if remaining_burst_times[i] > 0:
                executed_time = min(remaining_burst_times[i], time_quantum)
                time += executed_time
                remaining_burst_times[i] -= executed_time
                if remaining_burst_times[i] == 0:
                    waiting_times[i] = time - burst_times[i]

    turnaround_times = [waiting_times[i] + burst_times[i] for i in range(n)]

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i]}\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
    print(f"\nAverage Waiting Time: {sum(waiting_times) / n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_times) / n:.2f}")


# Input Section
process_ids = list(map(int, input("Enter Process IDs: ").split()))
burst_times = list(map(int, input("Enter Burst Times: ").split()))
time_quantum = int(input("Enter Time Quantum: "))

# Call the function
round_robin(process_ids, burst_times, time_quantum)

