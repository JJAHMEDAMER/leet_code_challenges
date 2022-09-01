class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1.__add__(num2)
    
def main():
    solu = Solution()
    print(solu.sum(12, 5))
    print(solu.sum(-10, 4))

if __name__ == "__main__":
    main()