from standard_bloom.bloom_filter import BloomFilter

def test_standard_bloom_filter():
    ocekivani_broj_elemenata = 10
    zeljena_stopa_greske = 0.05
    
    m_optimal, k_optimal = BloomFilter.calculate_optimal_params(ocekivani_broj_elemenata, zeljena_stopa_greske)
    
    print(f"Za {ocekivani_broj_elemenata} elemenata i {zeljena_stopa_greske*100}% greške, optimalni parametri su:")
    print(f"  -> Veličina niza (m): {m_optimal}")
    print(f"  -> Broj heš funkcija (k): {k_optimal}\n")
    
    bloom = BloomFilter(size=m_optimal, num_hashes=k_optimal)
    
    words_to_add = ["sarajevo", "mostar", "tuzla", "python"]
    print(f"Dodajemo riječi:")
    
    all_set_indices = set()
    
    for word in words_to_add:
        indices = bloom.add(word)
        print(f"  -> Riječ '{word}' postavlja indekse: {sorted(indices)}")
        current_indices_set = set(indices)
        preklapanje = all_set_indices.intersection(current_indices_set)
        if preklapanje:
            print(f"  -> Uočeno preklapanje na indeksima: {sorted(list(preklapanje))}")
        all_set_indices.update(current_indices_set)

    print(f"\nUkupno zauzeti indeksi u bit-nizu: {sorted(list(all_set_indices))}")

    words_to_check = ["sarajevo", "zenica", "python", "java"]
    print(f"\nProvjeravamo riječi:")
    
    for word in words_to_check:
        result, indices = bloom.check(word)
        print(f"  -> Da li '{word}' postoji? Rezultat: {result}. Provjereni indeksi: {sorted(indices)}")

    print("\n--- Testiranje završeno ---")

if __name__ == "__main__":
    test_standard_bloom_filter()