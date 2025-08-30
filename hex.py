def is_valid_hex_code(inp):
    inp = inp.upper()
    txt = "ABCDEF0123456789"
    if inp.startswith("#") and len(inp) == 7 :
        for char in inp[1:] :
            if char in txt :
                continue
            else :
                return False
    else :
        return False
    return True

#inp = input()
#print(is_valid_hex_code(inp))