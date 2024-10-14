import pandas as pd

# Function to calculate the values for SJF (Shortest Job First)
def sjf_scheduling(n, processes):
    # Initialize variables
    ct = [0] * n  # Completion Time
    tat = [0] * n  # Turnaround Time
    wt = [0] * n  # Waiting Time
    rt = [0] * n  # Response Time
    awt = 0  # Average Waiting Time
    ata = 0  # Average Turnaround Time
    
    # Sort processes by Arrival Time
    processes.sort(key=lambda x: x[1])
    
    # Create a list to hold processes that are ready to execute
    ready_queue = []
    current_time = 0
    completed_processes = 0
    
    while completed_processes < n:
        # Add processes to the ready queue that have arrived by current time
        for process in processes:
            if process[1] <= current_time and process not in ready_queue:
                ready_queue.append(process)
        
        if ready_queue:
            # Sort the ready queue by Burst Time (Shortest Job First)
            ready_queue.sort(key=lambda x: x[2])
            
            # Get the process with the shortest burst time
            current_process = ready_queue.pop(0)
            
            # Calculate the completion time for the current process
            ct[processes.index(current_process)] = current_time + current_process[2]
            current_time += current_process[2]
            completed_processes += 1
        else:
            # If no processes are ready, increment the current time
            current_time += 1
    
    # Calculate TAT, WT, RT
    for i in range(n):
        tat[i] = ct[i] - processes[i][1]  # Turnaround Time = Completion Time - Arrival Time
        wt[i] = tat[i] - processes[i][2]  # Waiting Time = Turnaround Time - Burst Time
        rt[i] = wt[i]  # Response Time = Waiting Time
        ata += tat[i]
        awt += wt[i]
    
    # Calculate average turnaround time and average waiting time
    ata /= n
    awt /= n

    # Display the results in a DataFrame
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

# Input: Number of processes
n = int(input("Enter the number of processes: "))
processes = []

# Input: Process details (PID, Arrival Time, Burst Time)
for i in range(n):
    pid = input(f"Enter Process ID for process {i + 1}: ")
    at = int(input(f"Enter Arrival Time for process {i + 1}: "))
    bt = int(input(f"Enter Burst Time for process {i + 1}: "))
    processes.append([pid, at, bt])

# Call the SJF scheduling function
sjf_scheduling(n, processes)
