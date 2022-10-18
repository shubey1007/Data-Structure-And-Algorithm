#code

class Solution(object):
   def lengthOfLongestSubstring(self, s):
      i =0
      j = 0
      d={}
      ans = 0
      while j < len(s):
         if s[j] not in d or i>d[s[j]]:
            ans = max(ans,(j-i+1))
            d[s[j]] = j
         else:
            i = d[s[j]]+1
            ans = max(ans,(j-i+1))
            j-=1
         #print(ans)
         j+=1
      return ans
ob1 = Solution()
print(ob1.lengthOfLongestSubstring("ABCABCBB"))


# Algorithm

# set i := 0, j := 0, set one map to store information
# ans := 0
# while j < length of string s
# if s[j] is not present in map, or i > map[s[j]], then
# ans := max(ans, j – i + 1)
# map[s[j]] := j
# otherwise
# i := map[s[j]] + 1
# ans := max(ans, j – i + 1)
# decrease j by 1
# increase j by 1
# return ans
