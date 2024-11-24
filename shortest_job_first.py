def sjf(processes, burst_times):
    n = len(processes)
    processes_sorted = sorted(zip(processes, burst_times), key=lambda x: x[1])  # Sort by burst time
    waiting_times, turnaround_times = [0] * n, [0] * n
    total_time = 0

    for i, (pid, bt) in enumerate(processes_sorted):
        waiting_times[i] = total_time
        total_time += bt
        turnaround_times[i] = total_time

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i, (pid, bt) in enumerate(processes_sorted):
        print(f"P{pid}\t{bt}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
    print(f"\nAverage Waiting Time: {sum(waiting_times) / n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_times) / n:.2f}")


# Input Section
process_ids = list(map(int, input("Enter Process IDs: ").split()))
burst_times = list(map(int, input("Enter Burst Times: ").split()))

# Call the function
sjf(process_ids, burst_times)

