class IndexedAllocation:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk = [None] * total_blocks
        self.files = {}

    def allocate_file(self, file_name, blocks):
        index_block = None
        allocated_blocks = []

        for i in range(self.total_blocks):
            if self.disk[i] is None:
                if index_block is None:
                    index_block = i
                self.disk[i] = file_name
                allocated_blocks.append(i)

        if len(allocated_blocks) > 1:
            self.files[file_name] = {"index_block": index_block, "blocks": allocated_blocks}
            print(f"File {file_name} allocated with index block {index_block} and data blocks {allocated_blocks}")
            return True
        else:
            print("Not enough space.")
            return False

    def deallocate_file(self, file_name):
        if file_name in self.files:
            file_info = self.files[file_name]
            index_block = file_info["index_block"]
            allocated_blocks = file_info["blocks"]
            for block in allocated_blocks:
                self.disk[block] = None
            self.disk[index_block] = None
            del self.files[file_name]
            print(f"File {file_name} deallocated.")
            return True
        else:
            print(f"File {file_name} not found.")
            return False

    def display(self):
        print("Disk Blocks:", self.disk)
        print("Files:", self.files)


# Test Indexed Allocation
indexed_alloc = IndexedAllocation(10)
indexed_alloc.allocate_file("file1", [1, 2, 3])
indexed_alloc.display()
indexed_alloc.deallocate_file("file1")
indexed_alloc.display()
