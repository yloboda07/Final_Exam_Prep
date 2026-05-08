# def Racaman(n):
#     if n == 0:
#         return 0
#     else: 
#         if Racaman(n-1) - n > 0:
#             return Racaman(n-1) - n
#         else:
#             return Racaman(n-1) + n

def Racaman(n):
    if n == 0:
        return 0
    seq = [0]
    for n in range(1,n+1):
        potential = seq[n-1]-n
        if potential > 0 and potential not in seq:
            seq.append(potential)
        else:
            seq.append(seq[n-1]+n)
    return seq[-1]


print(Racaman(6))