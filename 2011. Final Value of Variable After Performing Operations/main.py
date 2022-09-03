from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for operation in operations:
            if "+" in operation:
                ans += 1
            else:
                ans -= 1
        return ans
    
def main():
    solu = Solution()
    print(solu.finalValueAfterOperations(["--X","X++","X++"]))
    print(solu.finalValueAfterOperations(["++X","++X","X++"]))
    print(solu.finalValueAfterOperations(["X++","++X","--X","X--"]))


if __name__ == "__main__":
    main()