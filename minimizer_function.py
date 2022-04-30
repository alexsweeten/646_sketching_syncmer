from audioop import reverse

#This is spaghetti code. Please dont judge :)
def reverse_comp(seq):
    new_seq = ""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    for letter in reversed(seq):
        if letter in complement:
            new_seq = new_seq + str(complement[letter])
    return new_seq
        

def compute_min(seq,k,w,canonical):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    if canonical:
        rev=seq[::-1]

        rev=rev.replace("A","X")
        rev=rev.replace("T","A")
        rev=rev.replace("X","T")
        rev=rev.replace("C","X")
        rev=rev.replace("G","C")
        rev=rev.replace("X","G")

    Kmer=k
    M=w
    L=len(seq)

    min_list = []
    #Oh god im so sorry, this is atrociously inefficient
    min_direction = "?"

    for i in range(0, L-Kmer+1):
            sub_f=seq[i:i+Kmer]
            if canonical:
                sub_r=rev[L-Kmer-i:L-i]

            min="ZZZZZZZZZZZZZ"
            for j in range(0, Kmer-M+1):
                    sub2=sub_f[j:j+M]
                    if sub2 < min:
                            min=sub2
                            min_direction = "forward"
                    if canonical:
                        sub2=sub_r[j:j+M]
                        if sub2 < min:
                                min=sub2
                                min_direction = "reverse"
            if min_direction == "forward":
                min_list.append(min)
            else:
                min_list.append(reverse_comp(min))
    
    return min_list


print(compute_min("CCAGTGGCTACGG",k=7,w=5,canonical=True))
