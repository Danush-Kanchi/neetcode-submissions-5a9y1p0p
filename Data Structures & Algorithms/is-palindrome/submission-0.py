class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            # If ch is alphanumeric:
            #     Convert to lowercase
            #     Append to cleaned
            if ch.isalnum():
                cleaned+= ch.lower()
        return cleaned==cleaned[::-1]


        # Compare cleaned with its reverse