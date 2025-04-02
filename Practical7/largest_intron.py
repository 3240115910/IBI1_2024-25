import re
        
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
sequence = re.findall(r'GT.+AG',seq)
largest_intron_length = [len(intron)for intron in sequence]
print (f'The largest intron is {sequence}.')
print (f'The length of largest intron is {largest_intron_length}.')