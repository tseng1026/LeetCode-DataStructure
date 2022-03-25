# https://leetcode.com/problems/lfu-cache/

class Bucket:
    def __init__(self, frequent: int = 0):
        self.frequent = frequent
        self.key_list = list()
        self.prev = None
        self.next = None


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = defaultdict(int)
        self.capacity = capacity
        self.length = 0

        self.key_bucket_map = defaultdict(Bucket)
        self.head = Bucket()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_buckets(key)
            return self.cache[key]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.cache and \
                self.capacity == self.length:
            least_frequent_key = self.head.next.key_list[0]
            self.remove_key(least_frequent_key, self.head.next)
            self.key_bucket_map.pop(least_frequent_key)
            self.cache.pop(least_frequent_key)

        self.update_buckets(key)
        self.cache[key] = value

    def update_buckets(self, key: int) -> None:
        bucket = None
        if key in self.cache:
            curr = self.key_bucket_map[key]
            bucket = self.insert_key(key, curr, curr.frequent + 1)
            self.remove_key(key, curr)

        else:
            bucket = self.insert_key(key, self.head, 1)
        self.key_bucket_map[key] = bucket

    def insert_key(self, key: str, candidate: Bucket, frequent: int) -> Bucket:
        if candidate.next and candidate.next.frequent == frequent:
            candidate = candidate.next

        if candidate.frequent != frequent:
            self.insert_bucket(candidate, frequent)
            candidate = candidate.next

        candidate.key_list.append(key)
        self.length += 1
        return candidate

    def insert_bucket(self, target: Bucket, frequent: int) -> None:
        next_bucket = target.next

        temp_bucket = Bucket(frequent)
        target.next = temp_bucket
        temp_bucket.prev = target

        temp_bucket.next = next_bucket
        if next_bucket:
            next_bucket.prev = temp_bucket

    def remove_key(self, key: str, candidate: Bucket) -> None:
        candidate.key_list.remove(key)
        self.length -= 1

        if len(candidate.key_list) == 0:
            self.remove_bucket(candidate)

    def remove_bucket(self, target: Bucket):
        prev_bucket = target.prev
        next_bucket = target.next

        prev_bucket.next = next_bucket
        if next_bucket:
            next_bucket.prev = prev_bucket
