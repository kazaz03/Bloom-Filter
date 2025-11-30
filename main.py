from tests.test_standard_filter import test_standard_bloom_filter
from tests.test_counting_filter import test_counting_bloom_filter

if __name__ == "__main__":
    test_standard_bloom_filter()
    test_counting_bloom_filter()