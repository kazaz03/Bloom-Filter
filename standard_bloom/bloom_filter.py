import hashlib
import math 

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes  
        #bit niz
        self.bit_array = [0] * size

    def _get_hashes(self, element):
        #SHA-256, MD5 i double hashing tehnika
        indices = []
        
        #enkodiranje elemnta u bajtove
        hash1_bytes = hashlib.sha256(element.encode('utf-8')).digest()
        hash2_bytes = hashlib.md5(element.encode('utf-8')).digest()
        #konverzija bajtova u brojeve
        hash1_int = int.from_bytes(hash1_bytes, 'big')
        hash2_int = int.from_bytes(hash2_bytes, 'big')
        
        #generisanje k indeksa
        for i in range(self.num_hashes):
            combined_hash = hash1_int + i * hash2_int
            index = combined_hash % self.size
            indices.append(index)
        
        return indices

    def add(self, element):
        indices_to_set = self._get_hashes(element)

        for index in indices_to_set:
            self.bit_array[index] = 1
        return indices_to_set

    def check(self, element):
        indices_to_check = self._get_hashes(element)
        
        for index in indices_to_check:
            if self.bit_array[index] == 0:
                return False, indices_to_check
        
        #vjerovatno jeste tu ako su svi na 1
        return True, indices_to_check 

    @staticmethod
    def calculate_optimal_params(num_elements, false_positive_prob):
        """
        :param num_elements - ocekivani broj el
        :param false_positive_prob: zeljena vjerovatnoca lazno pozitivnih
        """
        #optimalna velicina niza s bitima
        m = - (num_elements * math.log(false_positive_prob)) / (math.log(2) ** 2)
        #optimalan broj funkcija
        k = (m / num_elements) * math.log(2)
        return int(m), int(k)