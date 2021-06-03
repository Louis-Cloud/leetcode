class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s1_len = len(s1)
        s1_index = 0
        not_s1 = ""
        for s3_index, c in enumerate(s3):
            print("c:" + c)
            if s1_index == s1_len:
                print("a")
                print("s3_index:" + str(s3_index))
                print("c[s3_index:]" + s3[s3_index:])
                not_s1 += s3[s3_index:]
                break
            elif c == s1[s1_index]:
                print("b")
                print("s1_index:" + str(s1_index))
                s1_index += 1
            else:
                print("d")
                not_s1 += c
                
            print("not_s1:" + not_s1)
        print("not_s1:",not_s1)
        return not_s1 == s2