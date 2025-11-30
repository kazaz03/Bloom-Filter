import hashlib

class CountingBloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.counter_array = [0] * size

    def _get_hashes(self, element):
        indices = []
        hash1_bytes = hashlib.sha256(element.encode('utf-8')).digest()
        hash2_bytes = hashlib.md5(element.encode('utf-8')).digest()
        hash1_int = int.from_bytes(hash1_bytes, 'big')
        hash2_int = int.from_bytes(hash2_bytes, 'big')
        
        for i in range(self.num_hashes):
            combined_hash = hash1_int + i * hash2_int
            index = combined_hash % self.size
            indices.append(index)
        
        return indices

    def add(self, element):
        indices_to_increment = self._get_hashes(element)
        for index in indices_to_increment:
            self.counter_array[index] += 1
        
        return indices_to_increment

    def delete(self, element):
        indices_to_decrement = self._get_hashes(element)
        
        for index in indices_to_decrement:
            if self.counter_array[index] > 0:
                self.counter_array[index] -= 1
        
        return indices_to_decrement

    def check(self, element):
        indices_to_check = self._get_hashes(element)
        for index in indices_to_check:
            if self.counter_array[index] == 0:
                return False, indices_to_check
        return True, indices_to_check