'''Use a hash function to transform the key into an index which will fit in the underlying array.  Hashing functions'''

n = 301
s = 3

print(n%s)
print(n/s)


"""
Inserting a key/value pair: O(1) on avg.; O(n) in the worse case
Removing a key/value pair: O(1) on avg.; O(n) in the worse case
Looking up a key: O(1) on avg.; O(n) in the worse case

The worst-case linear time operations occur when a hash table experiences a lot of collisions, leading to long linked lists internally, which take O(n) time to traverse.

However, in practice and especially in coding interviews, we typically assume that the hash functions employed by hash tables are so optimized that the collisions are extremely rare and constant-time operations are all but guaranteed.
"""
