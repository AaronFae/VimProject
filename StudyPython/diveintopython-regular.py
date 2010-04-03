if __name__ == '__main__':
    import re
    s = '100 NORTH BROAD ROAD'
    print s.replace('ROAD', 'RD.')
    # $ here means at the end of a string while ^ means at the beginning of the string
    print re.sub('ROAD$', 'RD.', s)

    s = '100 BROAD'
    print re.sub('ROAD$', 'RD.', s)
    print re.sub('\\bROAD$', 'RD.', s) # '\\b' means '\b', which is a word boundary here.
    print re.sub(r'\bROAD$', 'RD.', s) # always use raw string in python for regular expression.

    s = '100 BROAD ROAD APT. 3'
    print re.sub(r'\bROAD$', 'RD.', s) # ROAD is not at the end of the string, so the expression will not work.
    print re.sub(r'\bROAD\b', 'RD.', s) # Use '\bkeyword\b' to match the word exactly.

    pattern = '^M?M?M?$' # means the the string must start with 'M' or '' and end with 'M' or '', and '' to 3M string is qualified. 'M?' here means match zero or single 'M'
    print re.search(pattern, 'M') 
    print re.search(pattern, 'MM') 
    print re.search(pattern, 'MMM') 
    print re.search(pattern, 'MMMM') # get None result here.
    print re.search(pattern, '') 


    # in parentheses, which defines a set of three mutually exclusive patterns, separated by vertical bars:
    # CM, CD, and D?C?C?C? (which is an optional D followed by zero to three optional C characters).
    pattern = '^M?M?M?(CM|CD|D?C?C?C?)$' 
    print re.search(pattern, 'MCM') 
    print re.search(pattern, 'MD')
    print re.search(pattern, 'MMMCCC')
    print re.search(pattern, 'MCMC') # get None result here.
    print re.search(pattern, '')

    pattern = '^M{0,3}$' # equals to '^M?M?M?$'
    print re.search(pattern, 'M') 
    print re.search(pattern, 'MM') 
    print re.search(pattern, 'MMM') 
    print re.search(pattern, 'MMMM') # get None result here.
    print re.search(pattern, '') 

    pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'
    # pattern = '^M{0, 4}(CM|CD|D?C{0, 3})(XC|XL|L?X{0, 3})$'
    re.search(pattern, 'MCMXL')
    re.search(pattern, 'MCML')
    re.search(pattern, 'MCMLX')
    re.search(pattern, 'MCMLXXX')
    re.search(pattern, 'MCMLXXXX') # get None result here.

    # Verbose regular expression is different from compact regular expression in two ways: Whitespace is ignored while Comments are ignored.
    # Verbose regular expression is used for ease of understanding the regular expression.
    pattern = """
    ^                # beginning of string
    M{0,4}           # thousands ? 0 to 4 M's
    (CM|CD|D?C{0,3}) # hundreds ? 900 (CM), 400 (CD), 0?300 (0 to 3 C's),
                     # or 500?800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3}) # tens ? 90 (XC), 40 (XL), 0?30 (0 to 3 X's),
                     # or 50?80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3}) # ones ? 9 (IX), 4 (IV), 0?3 (0 to 3 I's),
                     # or 5?8 (V, followed by 0 to 3 I's)
    $                # end of string
    """
    re.search(pattern, 'M', re.VERBOSE) # re.VERBOSE indicate that, it is verbose mode now.
    re.search(pattern, 'MCMLXXXIX', re.VERBOSE)

    # 'prog = re.compile(pattern) result = prog.search(str)' is equivalent to 'result = re.search(pattern, str)'
    # What's \d{3}? Well, the {3} means "match exactly three numeric digits"; \d means "any numeric digit" (0 through 9).
    # Putting it in parentheses means "match exactly three numeric digits, and then remember them as a group that I can ask for later".
    phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
    # use the groups() method on the object that the search function returns. It will return a tuple of however many groups were defined in the regular expression.
    print phonePattern.search('800-555-1212').groups()
    # \d+ means one or more digits here.
    phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
    print phonePattern.search('800-555-1212-1234').groups()
    # \D matches any character except a numeric digit, and + means "1 or more".So \D+ matches one or more characters that are not digits.
    phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
    print phonePattern.search('800 555 1212 1234').groups()
    # Remember that + means "1 or more"? Well, * means "zero or more". So now you should be able to parse phone numbers even when there is no separator character at all.
    phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
    print phonePattern.search('80055512121234').groups()
    phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
    print phonePattern.search('(800)5551212 ext. 1234').groups()
    print phonePattern.search('work 1-(800) 555.1212 #1234') # get None result here.
    phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') # to avoid the None result above, get rid of '^\D*'
    print phonePattern.search('work 1-(800) 555.1212 #1234').groups()

    # You should now be familiar with the following techniques:
    # ^ matches the beginning of a string.
    # $ matches the end of a string.
    # \b matches a word boundary.
    # \d matches any numeric digit.
    # \D matches any non?numeric character.
    # x? matches an optional x character (in other words, it matches an x zero or one times).
    # x* matches x zero or more times.
    # x+ matches x one or more times.
    # x{n,m} matches an x character at least n times, but not more than m times.
    # (a|b|c) matches either a or b or c.
    # (x) in general is a remembered group. You can get the value of what matched by using the groups()
    # method of the object returned by re.search.
    
    
    
    
    
    
    
    




