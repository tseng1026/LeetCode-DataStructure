# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(
            self,
            target: int,
            position: List[int],
            speed: List[int]) -> int:
        cars = []
        for pos, spd in zip(position, speed):
            time = (target - pos) / spd
            cars.append((pos, time))
        cars = sorted(cars, key=lambda x: x[0], reverse=True)

        monotonic = []
        for _, time in cars:
            if not monotonic or monotonic[-1] < time:
                monotonic.append(time)
        return len(monotonic)
