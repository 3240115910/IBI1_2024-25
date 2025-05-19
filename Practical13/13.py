# Change working directory
import os
os.chdir(r'C:\Users\张嘉芮1\Desktop\IBI1\IBI1_2024-25\Practical13')
# Defined a function called read_fasta for reading files.
# Read all lines of the file and extract the sequence in FASTA format (excluding description lines starting with '>').
# Return the extracted sequence string.
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence
# Defined a function called read_closum62 for reading BLOSUM62 files.
# Open the file and read all lines, with the first line containing the code for amino acids.
# Traverse each row and column of the matrix, and store the amino acid pairs and their corresponding scores in the dictionary.
# Return a dictionary containing the BLOSUM62 matrix.
def read_blosum62(file_path):
    blosum62 = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
    amino_acids = lines[0].strip().split()
    for i in range(1, len(lines)):
        row = lines[i].strip().split()
        for j in range(1, len(row)):
            blosum62[(amino_acids[i-1], amino_acids[j-1])] = int(row[j])
    return blosum62
# Defined a function called calculate_stcore to calculate the alignment score and percentage similarity between two sequences.
# Traverse each position of two sequences, calculate scores, and count the number of identical amino acids.
# Return the calculated score and percentage similarity.
def calculate_score(seq1, seq2, blosum62):
    score = 0
    identical_count = 0
    for i in range(len(seq1)):
        pair = (seq1[i], seq2[i])
        score += blosum62.get(pair, 0)
        if seq1[i] == seq2[i]:
            identical_count += 1
    return score, identical_count / len(seq1) * 100
# Defined a main function called 'main' for performing sequence alignment and print the results.
def main():
    seq1 = read_fasta('P04179_Human.fasta')
    seq2 = read_fasta('P09671_Mouse.fasta')
    random_seq = read_fasta('Random.fasta')
    blosum62 = read_blosum62('BLOSUM62.txt')
    
    print("Human vs Mouse:")
    score, identity = calculate_score(seq1, seq2, blosum62)
    print(f"Score: {score}, Identity: {identity:.2f}%")
    
    print("Human vs Random:")
    score, identity = calculate_score(seq1, random_seq, blosum62)
    print(f"Score: {score}, Identity: {identity:.2f}%")
    
    print("Mouse vs Random:")
    score, identity = calculate_score(seq2, random_seq, blosum62)
    print(f"Score: {score}, Identity: {identity:.2f}%")

if __name__ == "__main__":
    main()