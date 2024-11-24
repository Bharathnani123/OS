def lru_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0

    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)  # Remove the least recently used
                frames.append(page)
            page_faults += 1
        else:
            # Move the used page to the most recently used position
            frames.remove(page)
            frames.append(page)

        print(f"Page: {page} -> Frames: {frames}")

    print(f"\nTotal Page Faults (LRU): {page_faults}")


# Input Section
pages = list(map(int, input("Enter the page reference string: ").split()))
frame_size = int(input("Enter the frame size: "))

# Call the function
lru_page_replacement(pages, frame_size)
