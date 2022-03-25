# https://leetcode.com/problems/all-oone-data-structure/

from typing import Set


class Bucket:
    def __init__(self, count: int = 0):
        self.count = count
        self.key_set = set()
        self.next = None
        self.prev = None


class AllOne:
    def __init__(self):
        self.key_bucket_map = defaultdict(Bucket)
        self.head = self.tail = Bucket()

    def inc(self, key: str) -> None:
        bucket = None
        if key not in self.key_bucket_map:
            bucket = self.insert_key(key, self.head, 1)

        else:
            curr = self.key_bucket_map[key]
            bucket = self.insert_key(key, curr, curr.count + 1)
            self.remove_key(key, curr)
        self.key_bucket_map[key] = bucket

    def dec(self, key: str) -> None:
        curr = self.key_bucket_map[key]
        self.remove_key(key, curr)

        if curr.count - 1 != 0:
            bucket = self.insert_key(key, curr.prev, curr.count - 1)
            self.key_bucket_map[key] = bucket

        else:
            self.key_bucket_map.pop(key)

    def insert_key(self, key: str, candidate: Bucket,
                   count: int) -> Bucket:
        if candidate.next and candidate.next.count == count:
            candidate = candidate.next

        if candidate.count != count:
            self.insert_bucket(candidate, count)
            candidate = candidate.next

        candidate.key_set.add(key)
        return candidate

    def insert_bucket(self, target: Bucket, count: int) -> None:
        next_bucket = target.next

        temp_bucket = Bucket(count)
        target.next = temp_bucket
        temp_bucket.prev = target

        temp_bucket.next = next_bucket
        if next_bucket:
            next_bucket.prev = temp_bucket
        else:
            self.tail = temp_bucket

    def remove_key(self, key: str, candidate: Bucket) -> None:
        candidate.key_set.discard(key)

        if len(candidate.key_set) == 0:
            self.remove_bucket(candidate)

    def remove_bucket(self, target: Bucket) -> None:
        prev_bucket = target.prev
        next_bucket = target.next

        prev_bucket.next = next_bucket
        if next_bucket:
            next_bucket.prev = prev_bucket
        else:
            self.tail = prev_bucket

    def getMaxKey(self) -> str:
        if self.head.next:
            return next(iter(self.tail.key_set))
        else:
            return ""

    def getMinKey(self) -> str:
        if self.head.next:
            return next(iter(self.head.next.key_set))
        else:
            return ""
