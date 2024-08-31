#https://leetcode.com/problems/valid-palindrome/
def isPalindrome(self, s: str) -> bool:
      #s=s.lower()
      
      s_new=''
      for ch in s:
          if ch.isalnum()==True:
              s_new+=ch.lower()
      print(s_new)
      i=0
      j=len(s_new)-1

      while i<j:
          # print(i,j)
          # print(s_new[i],s_new[j])
          if s_new[i]!=s_new[j]:
              return False
          i+=1
          j-=1
      return True
