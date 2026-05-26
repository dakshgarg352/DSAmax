class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i not in '+-*/':
                st.append(int(i))
                continue
            if i == '*':
                st.append(st.pop()*st.pop())
            elif i == '+':
                st.append(st.pop()+st.pop())
            elif i == '-':
                st.append(-1*(st.pop()-st.pop()))
            elif i == '/':
                if st[-2] != 0:
                    st.append(int(1/st.pop()*st.pop()))
                else:
                    st.pop()
                    st.pop()
                    st.append(0)
        
        return st[0]