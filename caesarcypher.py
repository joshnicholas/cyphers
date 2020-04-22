# This is a basic script to use a caesar cypher (encode a message by replacing each letter with one X spots further down the alphabet)


latin_alpha = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

test_string = "Moe is the owner and operator of Moe's Tavern, frequented by Homer Simpson and other characters including Lenny Leonard, Carl Carlson, Sam and Larry and his former most loyal customer, Barney Gumble. The bar is noted for its depressing atmosphere and uncleanliness. The regular patrons of the tavern have been abandoned by Moe in several episodes in which he changes its target audience."
encrypted_string = "yaq ue ftq aizqd mzp abqdmfad ar yaq'e fmhqdz, rdqcgqzfqp nk tayqd euybeaz mzp aftqd otmdmofqde uzoxgpuzs xqzzk xqazmdp, omdx omdxeaz, emy mzp xmddk mzp tue radyqd yaef xakmx ogefayqd, nmdzqk sgynxq. ftq nmd ue zafqp rad ufe pqbdqeeuzs mfyaebtqdq mzp gzoxqmzxuzqee. ftq dqsgxmd bmfdaze ar ftq fmhqdz tmhq nqqz mnmzpazqp nk yaq uz eqhqdmx qbueapqe uz ituot tq otmzsqe ufe fmdsqf mgpuqzoq."

### DICTIONARY UNPACKERS

def return_key(dict, character):
    for index, letter in dict.items():
        if letter == character.lower():
            return index

def return_value(dict, num):
    return dict[num]

#### ENCRYPT MESSAGE

def cypherisor(dict, string, offset, encrypt):
    temp = ''
    stringy = string.lower()
    for letter in stringy:
        if letter in [',', '.',"'", '!']:
            temp += letter
            continue
        else:
            init_num = return_key(latin_alpha, letter)
            if init_num == None:
                temp += " "
            else:
                if encrypt == True:
                    if init_num >= (27 -offset):
                        init_num -= 26

                    offsetted = init_num + offset
                    new_letter = return_value(latin_alpha, offsetted)    
                    temp += new_letter
                else: 
                    if init_num <= offset:
                        init_num += 26
                    offsetted = init_num - offset
                    new_letter = return_value(latin_alpha, offsetted)    
                    temp += new_letter    
    return temp

crypted = cypherisor(latin_alpha,test_string, 12, True)

print(crypted)

decrypted = cypherisor(latin_alpha,encrypted_string, 12, False)

print(decrypted)


