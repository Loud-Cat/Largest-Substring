def longest_substring(s):
    s = [int(i) for i in s]
    state = 'even' if int(s[0]) % 2 == 0 else 'odd'
    looking = 'even' if state == 'odd' else 'odd'

    patterns = [ [ s[0] ] ]
    current = 0
    
    first = True
    for i in s:
        looking = 'even' if state == 'odd' else 'odd'
        
        if not first:
            if looking == 'even':
                if i % 2 == 0:
                    patterns[current].append(i)
                else:
                    patterns.append([i])
                    current += 1

            elif i % 2 != 0:
                patterns[current].append(i)
            else:
                patterns.append([i])
                current += 1
        first = False
        state = 'even' if i % 2 == 0 else 'odd'
    patterns = [i for i in patterns if len(i) >= 2]
    
    large = 0
    for i in patterns:
        if len(i) > large:
            largest = i
            large = len(i)
    largest = "".join([str(i) for i in largest])
    print(largest)

longest_substring(input("string: "))
