#start a function to find the cut sites
def sites(DNA_seq, enzyme_seq):
    # Check if both sequences contain only canonical nucleotides
    valid_nucleotides = set(["A","C","G","T"])
    if not set(DNA_seq).issubset(valid_nucleotides) or not set(enzyme_seq).issubset(valid_nucleotides):
        raise ValueError("Sequences must contain only canonical nucleotides (ACGT)") 
    # Find all positions where the enzyme sequence matches
    cut_positions = []
    for i in range(len(DNA_seq) - len(enzyme_seq) + 1):
        if DNA_seq[i:i+len(enzyme_seq)] == enzyme_seq:
            cut_positions.append(i + 1) 
    return cut_positions
# an example and print out the sites.
try:
    DNA_seq = "ACGTCCAGTCAG"
    enzyme_seq = "AG"
    cut_sites = sites(DNA_seq, enzyme_seq)
    print(f"Restriction enzyme cut sites: {cut_sites}")
except ValueError as e:
    print(e)
DNA_seq= input('Please type the DNA sequences:')
enzyme_seq =input ('Please type the enzyme cut sites:')
result = sites(DNA_seq, enzyme_seq)
print (result)