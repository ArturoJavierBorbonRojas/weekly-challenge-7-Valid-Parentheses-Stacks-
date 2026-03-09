# weekly-challenge-7-Valid-Parentheses-Stacks-
For Week 7, I am diving into formal **Data Structures**. I tackled the classic "Valid Parentheses" problem, which is a foundational exercise to understand how a **Stack** works.
# 📚 Week 7: Data Structures - Stacks (Valid Parentheses)

## 📖 Description
For Week 7, I am diving into formal **Data Structures**. I tackled the classic "Valid Parentheses" problem, which is a foundational exercise to understand how a **Stack** works.

A Stack operates on the **LIFO (Last In, First Out)** principle—think of it like a stack of plates in a cafeteria; the last plate you put on top is the first one you take off.

This algorithm is exactly how your code editor (IDE) or compiler knows if you forgot to close a bracket or a parenthesis in your code!

## ⚙️ How it works
1. **The Stack:** I use a standard Python list `[]` to simulate the stack using `.append()` for pushing and `.pop()` for popping.
2. **The Mapping:** A Hash Map (dictionary) is used to link closing brackets `)`, `}`, `]` to their opening counterparts `(`, `{`, `[`.
3. **The Logic:** - Iterate through the string.
   - If we see an *opening* bracket, we push it to the stack.
   - If we see a *closing* bracket, we pop the top element from the stack. If they don't match (or if the stack is empty), the string is invalid.
   - At the end, if the stack is completely empty, the string is balanced!

## 🚀 Complexity Analysis
* **Time Complexity:** $O(n)$ - We traverse the string of length $n$ exactly once. Dictionary lookups and stack push/pop operations take $O(1)$ time.
* **Space Complexity:** $O(n)$ - In the worst-case scenario (e.g., all opening brackets like `"((((("`), we will push all $n$ characters onto the stack.

## 💻 Code Snippet
```python
def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
                
    return len(stack) == 0
