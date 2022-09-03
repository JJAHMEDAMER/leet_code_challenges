class Solution:
    def rotateString1(self, s: str, goal: str) -> bool:
        for i in range(0,len(s)):
            if s == goal:
                return True
            else:
                s = s[1:] + s[0]
        return False
    def rotateString2(self, s: str, goal: str) -> bool:
        return goal in s+s and len(s) == len(goal)
    
def main():
    solu = Solution()
    print(solu.rotateString1("abcde", "cdeab"))
    print(solu.rotateString1("abcde", "abced"))
    
    print(solu.rotateString2("abcde", "cdeab"))
    print(solu.rotateString2("abcde", "abced"))
    

if __name__ == "__main__":
    main()