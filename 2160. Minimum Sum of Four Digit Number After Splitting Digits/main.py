class Solution:
    def minimumSum(self, num: int) -> int:
        string = str(num)
        num1 = int(min(string) + max(string))
        string = string.replace(min(string),"",1)
        string = string.replace(max(string),"",1)
        num2 = int(min(string) + max(string))
        return  num1 + num2
    
def main():
    solu = Solution()
    print(solu.minimumSum(2932))
    print(solu.minimumSum(2932))

if __name__ == "__main__":
    main()