def minAddToMakeValid(s: str) -> int:
    stack = []
    add = 0

    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping.values():   # opening
            stack.append(ch)
        else:  # closing
            if stack and stack[-1] == mapping[ch]:
                stack.pop()
            else:
                add += 1   # missing opening bracket

    # remaining openings need closing brackets
    return add + len(stack)
    
print(minAddToMakeValid("[({}])"))