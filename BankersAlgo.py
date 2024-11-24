def is_safe(processes, avail, max_need, alloc):
    n = len(processes)  # Number of processes
    m = len(avail)      # Number of resources

    # Calculate the Need matrix
    need = [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

    # Initialize work and finish vectors
    work = avail[:]
    finish = [False] * n
    safe_sequence = []

    print("\nNeed Matrix:")
    for row in need:
        print(row)

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                # Check if the process can be executed
                if all(need[i][j] <= work[j] for j in range(m)):
                    # Simulate resource allocation
                    work = [work[j] + alloc[i][j] for j in range(m)]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    found = True
                    break

        if not found:
            print("\nSystem is not in a safe state.")
            return False, []

    print("\nSystem is in a safe state.")
    return True, safe_sequence


# Input Section
processes = list(map(int, input("Enter process IDs (space-separated): ").split()))
avail = list(map(int, input("Enter available resources (space-separated): ").split()))

print("\nEnter the allocation matrix (one row at a time):")
alloc = [list(map(int, input().split())) for _ in processes]

print("\nEnter the maximum need matrix (one row at a time):")
max_need = [list(map(int, input().split())) for _ in processes]

# Call the function
is_safe_state, safe_sequence = is_safe(processes, avail, max_need, alloc)

if is_safe_state:
    print("\nSafe Sequence:", " -> ".join(map(str, safe_sequence)))
