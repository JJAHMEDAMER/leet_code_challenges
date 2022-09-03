class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in address:
            if i == ".":
                ans += ("[.]")
            else:
                ans += (i)
        return ans
    
def main():
    solu = Solution()
    print(solu.defangIPaddr("1.1.1.1"))
    print(solu.defangIPaddr("255.100.50.0"))

if __name__ == "__main__":
    main()