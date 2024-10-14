import pandas as pd

# Function to calculate values for Round Robin scheduling
def round_robin_scheduling(n, processes, quantum):
    # Initialize variables
    ct = [0] * n  # Completion Time
    tat = [0] * n  # Turnaround Time
    wt = [0] * n  # Waiting Time
    rt = [0] * n  # Response Time
    awt = 0  # Average Waiting Time
    ata = 0  # Average Turnaround Time
    current_time = 0
    completed_processes = 0
    remaining_bt = [process[2] for process in processes]  # Remaining Burst Time
    queue = []  # Queue for Round Robin
    
    while completed_processes < n:
        for i in range(n):
            # Check if the process has arrived and is not already completed
            if processes[i][1] <= current_time and remaining_bt[i] > 0:
                queue.append(i)
        
        if queue:
            # Get the next process from the queue
            index = queue.pop(0)
            
            # If the remaining burst time is greater than quantum, it will run for quantum time
            if remaining_bt[index] > quantum:
                current_time += quantum
                remaining_bt[index] -= quantum
            else:
                current_time += remaining_bt[index]
                ct[index] = current_time  # Set completion time
                remaining_bt[index] = 0  # Process is completed
                completed_processes += 1
            
            # Update Turnaround Time (TAT) and Waiting Time (WT)
            tat[index] = ct[index] - processes[index][1]  # TAT = Completion Time - Arrival Time
            wt[index] = tat[index] - processes[index][2]  # WT = Turnaround Time - Burst Time
            awt += wt[index]
            ata += tat[index]
            
            # If the process has remaining time, it goes back to the queue
            if remaining_bt[index] > 0:
                queue.append(index)
        else:
            # No process is ready, increment current time
            current_time += 1

    # Calculate average turnaround time (ATA) and average waiting time (AWT)
    ata /= n
    awt /= n
    
    # Calculate throughput and context switches
    throughput = completed_processes / current_time
    context_switches = sum(1 for i in range(1, len(remaining_bt)) if remaining_bt[i] < processes[i][2])

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
    print(f"Throughput: {throughput:.2f} processes/unit time")
    print(f"Context Switches: {context_switches}")
    
    # Create Gantt Chart
    gantt_chart(processes, ct)

# Function to generate Gantt Chart (textual)
def gantt_chart(processes, ct):
    gantt_chart_str = ""
    timeline_str = "0"  # Start timeline at 0
    
    for i in range(len(processes)):
        gantt_chart_str += f"| P{processes[i][0]} "  # Process name
        if i > 0:
            timeline_str += f" {ct[i]}"  # Completion time
    
    gantt_chart_str += "|"
    
    print("\nGantt Chart:")
    print(gantt_chart_str)  # Display the Gantt chart with process names
    print(timeline_str)  # Display the corresponding timeline

# Input: Number of processes and Time Quantum
n = int(input("Enter the number of processes: "))
quantum = int(input("Enter the time quantum: "))

# Input: Process details (PID, Arrival Time, Burst Time)
processes = []
for i in range(n):
    pid = input(f"Enter Process ID for process {i + 1}: ")
    at = int(input(f"Enter Arrival Time for process {i + 1}: "))
    bt = int(input(f"Enter Burst Time for process {i + 1}: "))
    processes.append([pid, at, bt])

# Call the Round Robin scheduling function
round_robin_scheduling(n, processes, quantum)
