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
FNV_PRIME = 1099511628211
FNV_BASIS = 14695981039346656037


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        assert type(capacity) is int
        assert capacity >= MIN_CAPACITY
        self.__size = 0
        self.__capacity = capacity
        self.__table = [None] * capacity

    @property
    def capacity(self):
        return self.__capacity

    @property
    def size(self):
        return self.__size

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.__table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.__size / self.__capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash = FNV_BASIS
        for b in key.encode():
            hash *= FNV_PRIME
            hash ^= b
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for b in key.encode():
            hash += (hash << 5) + b
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity



    def __getitem__(self, key):
        """
        """
        index = self.hash_index(key)
        entry = self.__table[index]

        while entry is not None:
            if entry.key == key:
                return entry.value
            entry = entry.next

        raise ValueError(f"{key}")
        

    def __setitem__(self, key, value):
        """
        """
        index = self.hash_index(key)
        entry = self.__table[index]

        if entry is None:
            self.__table[index] = HashTableEntry(key, value)
            self.__size += 1
            return

        while entry.key != key and entry.next is not None:
            entry = entry.next

        if entry.key == key:
            entry.value = value
        else:
            entry.next = HashTableEntry(key, value)
            self.__size += 1


    def __delitem__(self, key):
        """
        """
        index = self.hash_index(key)
        entry = self.__table[index]

        if entry is None:
            raise ValueError(f"{key}")

        if entry.key == key:
            self.__table[index] = self.__table[index].next
            self.__size -= 1
            return

        prev, entry = entry, entry.next
        while entry is not None and entry.key != key:
            prev, entry = entry, entry.next

        if entry is None:
            raise ValueError(f"{key}")

        prev.next = entry.next
        self.__size -= 1


    def keys(self):
        """
        Returns a list of the keys in the hashtable.
        """
        res = []
        for entry in self.__table:
            while entry is not None:
                res.append(entry.key)
                entry = entry.next
        return res


    def values(self):
        """
        Returns a list of the values in the hashtable.
        """
        res = []
        for entry in self.__table:
            while entry is not None:
                res.append(entry.value)
                entry = entry.next
        return res


    def items(self):
        """
        Returns a list of tuples of the keys and values in the hashtable.
        """
        res = []
        for entry in self.__table:
            while entry is not None:
                res.append((entry.key, entry.value))
                entry = entry.next
        return res



    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        i = self.hash_index(key)
        if self.__table[i] is None:
            self.__table[i] = HashTableEntry(key, value)
            self.__size += 1
        else:
            curr = self.__table[i]
            # iterate through the linked list until we either find the existing
            # item with the given key or reach the end of the list
            while curr.key != key and curr.next is not None:
                curr = curr.next
            # key exists, overwrite
            if curr.key == key:
                curr.value = value
            # append the value to the linked list
            else:
                curr.next = HashTableEntry(key, value)
                self.__size += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        curr = self.__table[i]

        if curr.key == key:
            self.__table[i] = self.__table[i].next
            return 

        # iterate through the linked list until we either find the existing
        # item with the given key or reach the end of the list
        while curr is not None and curr.key != key:
            prev, curr = curr, curr.next

        if curr is None:
            print("Key not found")
            return

        self.__size -= 1
        prev.next = curr.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        curr = self.__table[i]
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.__table
        self.__table = [None] * new_capacity
        for bucket in old_table:
            curr = bucket
            while curr is not None:
                self.put(curr.key, curr.value)
                curr = curr.next



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
