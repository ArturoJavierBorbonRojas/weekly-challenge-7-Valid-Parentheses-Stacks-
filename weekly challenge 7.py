# Weekly challenge 7: Valid Parentheses (Stacks)
# Author: Ing. Arturo Javier Borbon Rojas

def is_valid_parentheses(s):
    # This list will act as our Stack (Pila)
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    
    print(f"🔍 Analyzing string: '{s}'")
    print("-" * 30)
    
    for char in s:
        # If it's an opening bracket, PUSH it to the stack
        if char in mapping.values():
            stack.append(char)
            print(f"📥 Pushed '{char}'. Stack state: {stack}")
            
        # If it's a closing bracket, POP from the stack and check
        elif char in mapping.keys():
            # Check if stack is empty before popping
            if not stack:
                print(f"❌ Error: Found '{char}' but stack is empty!")
                return False
                
            top_element = stack.pop()
            
            # Check if the popped element matches the expected opening bracket
            if mapping[char] != top_element:
                print(f"❌ Error: Mismatched! Expected '{mapping[char]}' but found '{char}'.")
                return False
                
            print(f"📤 Popped '{top_element}' to match '{char}'. Stack state: {stack}")
            
    # If the stack is empty at the end, all brackets were matched!
    is_valid = len(stack) == 0
    
    print("-" * 30)
    if is_valid:
        print(f"✅ Success! The string is perfectly balanced.\n")
    else:
        print(f"❌ Error: Leftover unclosed brackets in stack: {stack}\n")
        
    return is_valid

# --- 2. Execute with Test Cases ---

print("\n--- TEST CASE 1: Balanced ---")
test_1 = "{[()]}"
is_valid_parentheses(test_1)

print("--- TEST CASE 2: Unbalanced ---")
test_2 = "{[(])}"
is_valid_parentheses(test_2)