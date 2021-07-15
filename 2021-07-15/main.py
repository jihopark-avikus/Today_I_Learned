from collections import deque

def create_LRUcache(max_len):
    cache = deque(maxlen=max_len)
    return cache

def main():
    test_array = [1, 1, 2, 3, 4, 5, 5, 10]
    max_len = 5
    cache = create_LRUcache(max_len)

    for i in test_array:
        cache.append(i)
        print(cache)


if __name__ == "__main__":
    main()