# https://leetcode.com/problems/flatten-nested-list-iterator/

class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        self.flatten_list = self.flatten(nested_list)
        self.index = 0

    def flatten(self, nested_list: [NestedInteger]):
        temp_list = []
        for nested_integer in nested_list:
            if nested_integer.isInteger():
                temp_list += [nested_integer.getInteger()]
            else:
                temp_list += self.flatten(nested_integer.getList())

        return temp_list

    def next(self) -> int:
        val = self.flatten_list[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.flatten_list)
