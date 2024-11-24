class LinkedAllocation:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk = [None] * total_blocks
        self.files = {}

    def allocate_file(self, file_name, blocks):
        allocated_blocks = []
        for i in range(self.total_blocks):
            if self.disk[i] is None:
                self.disk[i] = file_name
                allocated_blocks.append(i)
                if len(allocated_blocks) == len(blocks):
                    break

        if len(allocated_blocks) == len(blocks):
            self.files[file_name] = allocated_blocks
            print(f"File {file_name} allocated with blocks: {allocated_blocks}")
            return True
        else:
            print("Not enough space.")
            return False

    def deallocate_file(self, file_name):
        if file_name in self.files:
            allocated_blocks = self.files[file_name]
            for block in allocated_blocks:
                self.disk[block] = None
            del self.files[file_name]
            print(f"File {file_name} deallocated from blocks: {allocated_blocks}")
            return True
        else:
            print(f"File {file_name} not found.")
            return False

    def display(self):
        print("Disk Blocks:", self.disk)
        print("Files:", self.files)


# Test Linked Allocation
linked_alloc = LinkedAllocation(10)
linked_alloc.allocate_file("file1", [1, 2, 3])
linked_alloc.display()
linked_alloc.deallocate_file("file1")
linked_alloc.display()
