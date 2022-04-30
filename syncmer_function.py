def compute_syncmer(seq,k,w,canonical,t):
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
    tmp_list = []
    syncmer_list = []
    if canonical:
        direction = []

    for i in range(0, L-Kmer+1):
            tmp_list.append(0)
            sub_f=seq[i:i+Kmer]
            if canonical:
                direction.append("?")
                sub_r=rev[L-Kmer-i:L-i]

            min="ZZZZZZZZZZZZZ"
            for j in range(0, Kmer-M+1):
                    sub2=sub_f[j:j+M]
                    if sub2 < min:
                            min=sub2
                            if canonical:
                                direction[i] = "forward"
                            tmp_list[i] = j
                    if canonical:
                        sub2=sub_r[j:j+M]
                        if sub2 < min:
                                min=sub2
                                direction[i] = "reverse"
                                tmp_list[i] = j
            min_list.append(min)
            syncmer_list.append(seq[i:i+Kmer])
    
    
    
    if canonical:
        #print(direction)
        for i in range(len(direction)):
                if direction[i] == "reverse":
                        #print(Kmer, tmp_list[i])
                        newbie = Kmer - tmp_list[i] - w
                        tmp_list[i] = newbie

    #print(min_list,tmp_list,syncmer_list)
    assert len(min_list) == len(tmp_list) == len(syncmer_list)

    final_syncmer_list = []
    for i in range(len(tmp_list)):
        if tmp_list[i] == t-1:
            final_syncmer_list.append(syncmer_list[i])
            #print(syncmer_list[i])
    return final_syncmer_list

print(compute_syncmer("CCAGTGGCTACGG",k=5,w=2,canonical=True,t=3))