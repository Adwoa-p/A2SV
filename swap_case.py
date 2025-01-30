def swap_case(s):
    ans=""
    for i in s:
        if i.isupper():
            i=i.lower()
            ans+=i
        else:
            i=i.upper()
            ans+=i
    return ans
