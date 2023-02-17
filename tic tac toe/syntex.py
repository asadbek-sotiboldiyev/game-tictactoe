def syntax(a1,a2,a3):
    """O'yin natijasini tekshirib, natijani qaytarib yuboradigan funksiya"""
    if (len(set(a1))==1 and (a1[0]!=".")) or (len(set(a2))==1 and (a2[0]!=".")) or (len(set(a3))==1 and (a3[0]!=".")):
        # 1,2,3-qatorlar
        if len(set(a1))==1:
            return (a1[0])
        elif len(set(a2))==1:
            return (a2[0])
        elif len(set(a3))==1:
            return (a3[0])
    elif a1[0]==a2[0]==a3[0]!="." or a1[1]==a2[1]==a3[1]!="." or a1[2]==a2[2]==a3[2]!=".":
        # 1,2,3-ustunlar
        if a1[0]==a2[0]==a3[0]!=".":
            return (a1[0])
        elif a1[1]==a2[1]==a3[1]!=".":
            return (a1[1])
        elif a1[2]==a2[2]==a3[2]!=".":
            return (a1[2])
    else:
        # dioganallar
        if a1[0]==a2[1]==a3[2]!=".":
            return (a1[0])
        elif a1[2]==a2[1]==a3[0]!=".":
            return (a1[2])
        elif not('.' in a1) and not('.' in a3) and not('.' in a2):
            # G'olib aniqlanmadi
            return False