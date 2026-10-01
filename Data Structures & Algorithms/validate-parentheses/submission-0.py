class Solution:
    def isValid(self, s: str) -> bool:
        store = []  
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                store.append(i)
                
            elif i == ')' or i == '}' or i == ']':
                if not store:
                    return False
                
                popped = store.pop()
                
                if i == ')' and popped != '(':
                    return False
                if i == '}' and popped != '{':
                    return False
                if i == ']' and popped != '[':
                    return False
                    
        return len(store) == 0