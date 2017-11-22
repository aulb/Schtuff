# Iterative fibonacci

def fibonacci(n):
    # Special case for negative elements and 1
    if n < 1: return []
    if n == 1: return [0]
    
    # Prefill result with the first and second fibonacci element
    result = [0, 1]
    
    while len(result) < n:
        result.append(result[-1] + result[-2]) 
    
    return result
