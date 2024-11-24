def optimal_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Find the page to replace
                future_use = []
                for f in frames:
                    if f in pages[i + 1:]:
                        future_use.append(pages[i + 1:].index(f))
                    else:
                        future_use.append(float('inf'))  # If not used in future

                # Replace the page with the furthest future use
                victim_index = future_use.index(max(future_use))
                frames[victim_index] = page

            page_faults += 1

        print(f"Page: {page} -> Frames: {frames}")

    print(f"\nTotal Page Faults (Optimal): {page_faults}")


# Input Section
pages = list(map(int, input("Enter the page reference string: ").split()))
frame_size = int(input("Enter the frame size: "))

# Call the function
optimal_page_replacement(pages, frame_size)
