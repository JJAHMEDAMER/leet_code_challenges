class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)
    
def main():
    solu = Solution()
    print(solu.minPartitions("55"))
    print(solu.minPartitions("32"))
    print(solu.minPartitions("82734"))
    print(solu.minPartitions("27346209830709182346"))

if __name__ == "__main__":
    main()