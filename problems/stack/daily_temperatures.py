class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [temperatures[-1]]
        n = len(temperatures)
        out = [0]
        for i in range(1,n):
            temp = temperatures[n-i-1]
            x = 1
            for i in range(len(st)):
                i = st[len(st) - i - 1]
                if i > temp:
                    out.append(x)
                    break
                else:
                    x+=1
            else:
                out.append(0)
                st = []
            st.append(temp)
        
        out.reverse()
        return out