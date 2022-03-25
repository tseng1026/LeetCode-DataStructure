# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        monotonic = []
        for asteroid in asteroids:
            is_explode = False

            while monotonic and not is_explode and \
                    monotonic[-1] > 0 > asteroid:
                if abs(monotonic[-1]) >= abs(asteroid):
                    is_explode = True

                if abs(monotonic[-1]) <= abs(asteroid):
                    monotonic.pop()

            if not is_explode:
                monotonic.append(asteroid)

        return monotonic
