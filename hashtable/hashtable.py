class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class LinkedList:
    def __init__(self):
        self.head = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.canister = [LinkedList()] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.canister)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / len(self.canister)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hashed = 5381
        for x in key:
            hashed = (hashed * 33) + ord(x)
        return hashed

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # self.canister[index] = value // Only use for MVP Day 1

        # MVP Day 2 Code
        if self.canister[index].head is None:
            self.canister[index].head = HashTableEntry(key, value)
            self.size += 1
            return

        else:
            current = self.canister[index].head

            while current.next:
                if current.key == key:
                    current.value = value
                current = current.next

            current.next = HashTableEntry(key, value)
            self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # self.canister.pop(index) // MVP Day 1 Code
        current = self.canister[index].head

        if current.key == key:
            self.canister[index].head = self.canister[index].head.next
            self.size -= 1
            return
        while current.next:
            previous = current
            current = current.next
            if current.key == key:
                previous.next = current.next
                self.size -= 1
                return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # return self.canister[index] // MVP Day 1 Code

        current = self.canister[index].head

        if current is None:
            return None
        if current.key == key:
            return current.value

        while current.next:
            current = current.next
            if current.key == key:
                return current.value
            return None

    def resize(self, newcapacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = newcapacity
        new_ll = [LinkedList()] * newcapacity

        for x in self.canister:
            current = x.head

            while current is not None:
                index = self.hash_index(current.key)

                if new_ll[index].head is None:
                    new_ll[index].head = HashTableEntry(current.key, current.value)
                else:
                    n = HashTableEntry(current.key, current.value)
                    n.next = new_ll[index].head

                    new_ll[index].head = n
                current = current.next
                self.canister = new_ll


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
