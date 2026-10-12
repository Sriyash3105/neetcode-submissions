class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = []
        for token in tokens:
            if token == "*":
                a = store.pop()
                b = store.pop()
                store.append(a*b)
            elif token == "-":
                a = store.pop()
                b = store.pop()
                store.append(b-a)
            elif token == "/":
                a = store.pop()
                b = store.pop()
                store.append(int(b/a))
            elif token == "+":
                a = store.pop()
                b = store.pop()
                store.append(a+b)
            else:
                store.append(int(token)) 
        return store[0]                       