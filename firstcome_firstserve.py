import pandas as pd

# Function to calculate the values for FCFS
def fcfs_scheduling(n, processes):
    # Initialize variables
    ct = [0] * n  # Completion Time
    tat = [0] * n  # Turnaround Time
    wt = [0] * n  # Waiting Time
    rt = [0] * n  # Response Time
    awt = 0  # Average Waiting Time
    ata = 0  # Average Turnaround Time

    # Sort processes by Arrival Time
    processes.sort(key=lambda x: x[1])

    # Calculate Completion Time
    ct[0] = processes[0][1] + processes[0][2]  # First process starts as soon as it arrives
    for i in range(1, n):
        if processes[i][1] > ct[i-1]:  # If the next process arrives after the previous has finished
            ct[i] = processes[i][1] + processes[i][2]
        else:
            ct[i] = ct[i-1] + processes[i][2]

    # Calculate TAT, WT, RT
    for i in range(n):
        tat[i] = ct[i] - processes[i][1]  # Turnaround Time = Completion Time - Arrival Time
        wt[i] = tat[i] - processes[i][2]  # Waiting Time = Turnaround Time - Burst Time
        rt[i] = wt[i]  # Response Time = Waiting Time
        ata += tat[i]
        awt += wt[i]

    ata /= n
    awt /= n

    # Display the results
    process_table = pd.DataFrame({
        'PID': [process[0] for process in processes],
        'AT': [process[1] for process in processes],
        'BT': [process[2] for process in processes],
        'CT': ct,
        'TAT': tat,
        'WT': wt,
        'RT': rt
    })
    print("\nProcess Information Table:")
    print(process_table)
    print(f"\nAverage Turnaround Time (ATA): {ata:.2f}")
    print(f"Average Waiting Time (AWT): {awt:.2f}")

    # Create Gantt Chart
    gantt_chart(processes, ct)


# Function to generate Gantt Chart (textual)
def gantt_chart(processes, ct):
    start_time = [0] * len(processes)
    start_time[0] = processes[0][1]  # First process starts at its arrival time
    for i in range(1, len(processes)):
        start_time[i] = max(ct[i-1], processes[i][1])  # Either start after the previous process or at its arrival time

    # Create textual Gantt Chart
    print("\nGantt Chart:")
    gantt_chart_str = ""
    timeline_str = "0"  # Start timeline at 0
    for i in range(len(processes)):
        gantt_chart_str += f"| P{processes[i][0]} "  # Process name
        timeline_str += f" {ct[i]}"  # Completion time
    gantt_chart_str += "|"
    print(gantt_chart_str)  # Display the Gantt chart with process names
    print(timeline_str)  # Display the corresponding timeline


# Input section
n = int(input("Enter the number of processes: "))
processes = []
for i in range(n):
    pid = input(f"Enter Process ID for process {i + 1}: ")
    at = int(input(f"Enter Arrival Time for process {i + 1}: "))
    bt = int(input(f"Enter Burst Time for process {i + 1}: "))
    processes.append([pid, at, bt])

# Call the FCFS scheduling function
fcfs_scheduling(n, processes)
