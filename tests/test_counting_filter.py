from counting_bloom.counting_filter import CountingBloomFilter

def test_counting_bloom_filter():
    cbf = CountingBloomFilter(size=62, num_hashes=4)
    print(f"\nCounting Bloom filter veličine {cbf.size} sa {cbf.num_hashes} heš funkcija.")

    words_to_add = ["javascript", "rust", "go"]
    print(f"\nDodajemo riječi: {words_to_add}")
    for word in words_to_add:
        indices = cbf.add(word)
        print(f"  -> Riječ '{word}' inkrementira indekse: {sorted(indices)}")
    
    print(f"Stanje brojača (samo > 0): { {i: cbf.counter_array[i] for i in range(cbf.size) if cbf.counter_array[i] > 0} }")

    print("\nProvjeravam da li riječi postoje (prije brisanja):")
    result_rust_before, _ = cbf.check("rust")
    print(f"  -> Da li 'rust' postoji? Rezultat: {result_rust_before}")
    result_go_before, _ = cbf.check("go")
    print(f"  -> Da li 'go' postoji? Rezultat: {result_go_before}")

    word_to_delete = "rust"
    print(f"\nBrišemo riječ: '{word_to_delete}'")
    indices = cbf.delete(word_to_delete)
    print(f"  -> Riječ '{word_to_delete}' dekrementira indekse: {sorted(indices)}")
    
    print(f"Stanje brojača nakon brisanja (samo > 0): { {i: cbf.counter_array[i] for i in range(cbf.size) if cbf.counter_array[i] > 0} }")
    
    print("\nProvjeravamo da li riječi postoje (nakon brisanja):")
    result_rust_after, _ = cbf.check("rust")
    print(f"  -> Da li 'rust' i dalje postoji? Rezultat: {result_rust_after}")
    result_go_after, _ = cbf.check("javascript")
    print(f"  -> Da li 'javascript' i dalje postoji? Rezultat: {result_go_after}")