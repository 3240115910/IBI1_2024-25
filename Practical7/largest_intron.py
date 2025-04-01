import re
def intron (seq):
    GT_site = [m.start() for m in re.finditer('GT', seq)]
    AG_site = [m.start() for m in re.finditer('AG', seq)]
    largest = 0
    largest_intron = ""
    for GT in GT_site:
        for AG in AG_site:
             if AG > GT:
                l= AG-GT-2
                if l >largest:
                    largest = l 
                    largest_intron = seq[GT + 2:AG]  
    return largest , largest_intron          
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron_length, largest_intron = intron(seq)
print (f'The largest intron is {largest_intron}.')
print (f'The length of largest intron is {largest_intron_length}.')