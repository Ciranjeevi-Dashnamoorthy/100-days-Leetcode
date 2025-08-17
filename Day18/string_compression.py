class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        write=0
        i=0
        print(type(n))

        while i < n:
            char=chars[i]
            count=0

            while i < n and chars[i]==char:
                i+=1
                count+=1

            chars[write]=char
            write+=1

            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write 