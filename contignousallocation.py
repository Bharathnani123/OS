class ContiguousAllocation:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk = [None] * total_blocks

    def allocate_file(self, start_block, length):
        if start_block + length <= self.total_blocks:
            for i in range(start_block, start_block + length):
                if self.disk[i] is not None:
                    print(f"Block {i} is already allocated!")
                    return False
            for i in range(start_block, start_block + length):
                self.disk[i] = "Allocated"
            print(f"File allocated from block {start_block} to {start_block + length - 1}")
            return True
        else:
            print("Not enough contiguous space.")
            return False

    def deallocate_file(self, start_block, length):
        for i in range(start_block, start_block + length):
            if self.disk[i] is None:
                print(f"Block {i} is not allocated.")
                return False
        for i in range(start_block, start_block + length):
            self.disk[i] = None
        print(f"File deallocated from block {start_block} to {start_block + length - 1}")
        return True

    def display(self):
        print("Disk Blocks:", self.disk)


# Test Contiguous Allocation
disk_size = 10
contiguous_alloc = ContiguousAllocation(disk_size)
contiguous_alloc.allocate_file(2, 3)
contiguous_alloc.display()
contiguous_alloc.deallocate_file(2, 3)
contiguous_alloc.display()
