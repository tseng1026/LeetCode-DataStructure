# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)

        while hand:
            temp_hand = []
            count = 1
            card = hand.pop(0)

            while hand and count < groupSize:
                curr = hand.pop(0)
                if curr == card + count:
                    count += 1
                elif curr < card + count:
                    temp_hand.append(curr)
                else:
                    break

            if count != groupSize:
                return False

            hand = temp_hand + hand

        return len(hand) == 0
