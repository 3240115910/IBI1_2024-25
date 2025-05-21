import re
# input the sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
# find the largest intron
sequence = re.findall(r'GT.+AG',seq)
# find the lengthe of the largest intron
largest_intron_length = [len(intron)for intron in sequence]
#print the results.
print (f'The largest intron is {sequence}.')
print (f'The length of largest intron is {largest_intron_length}.')