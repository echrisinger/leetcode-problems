
def soln(a, b, target):
    a = a.sort(key=lambda t: t[1])
    b = b.sort(key=lambda t: -t[1])
    
    curr_a = 0 # increment to increase total
    curr_b = 0 # increment to decrease total
    
    max_score = -float('inf')
    max_elements = []
    while curr_a < len(a) and curr_b < len(b):
        total = a[curr_a][1] + b[curr_b][1]
        if max_score < total and total <= target:
            max_score = total
            max_elements = [[a[curr_a][0], b[curr_b][0]]]
        elif max_score == total:
            max_elements.append([a[curr_a][0], b[curr_b][0]])
        
        if total < target:
            curr_a += 1
        else:
            curr_b += 1

    
    return max_elements
