lines = open('data').readlines()
print len(lines)
prefix = lines[0].strip()
iv = [ line.strip().decode('hex')[:16] for line in lines[1:]]


