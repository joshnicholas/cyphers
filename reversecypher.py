## a simple script to make a reverse alaphabet cipher

latin_alpha = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

test_message = "Moe is portrayed with a generally disagreeable personality: he has a short, violent temper, a penurious nature, a crass and undiplomatic manner of speech, and a mood that rapidly vacillates between anger, indifference and suicidal despair (the latter of which has become more apparent in later episodes of the show). He has an annual Christmas tradition of attempted suicide, but his attempts are comically unsuccessful (landing on a hot-air balloon after jumping out of a plane, for example), and he has already called the suicide hotline so many times that they've blocked his number."
encrypted_message = "nlv rh kligizbvw drgs z tvmvizoob wrhztivvzyov kvihlmzorgb  sv szh z hslig, erlovmg gvnkvi, z kvmfirlfh mzgfiv, z xizhh zmw fmwrkolnzgrx nzmmvi lu hkvvxs, zmw z nllw gszg izkrwob ezxroozgvh yvgdvvm zmtvi, rmwruuvivmxv zmw hfrxrwzo wvhkzri  gsv ozggvi lu dsrxs szh yvxlnv nliv zkkzivmg rm ozgvi vkrhlwvh lu gsv hsld . sv szh zm zmmfzo xsirhgnzh gizwrgrlm lu zggvnkgvw hfrxrwv, yfg srh zggvnkgh ziv xlnrxzoob fmhfxxvhhufo  ozmwrmt lm z slg zri yzoollm zugvi qfnkrmt lfg lu z kozmv, uli vcznkov , zmw sv szh zoivzwb xzoovw gsv hfrxrwv slgormv hl nzmb grnvh gszg gsvb'ev yolxpvw srh mfnyvi."

### access dictionary

def return_key(dict, character):
    for index, letter in dict.items():
        if letter == character.lower():
            return index

def return_value(dict, character):
    for index, letter in dict.items():
        if index == character.lower():
            return letter

### prepare dictionary    

def prep_dict(alphabet):
    temp_dict = {}
    for i in range(int(len(alphabet))):
        temp_dict[alphabet[i]] = alphabet[(int(len(alphabet))-i-1)]
    return temp_dict

#### encrypt/decrypt message

def cryptor(dict, string, encrypt):
    temp = ''
    stringy = string.lower()
    for letter in stringy:
        if letter in [',', '.',"'", '!']:
            temp += letter
            continue
        else:
            if encrypt == True:
                init_letter = return_key(dict, letter)
                if init_letter == None:
                    temp += " "
                else:
                    temp += init_letter
            else:
                init_letter = return_value(dict, letter)
                if init_letter == None:
                    temp += " "
                else:
                    temp += init_letter
    print(temp)

#### let er rip

dicto = prep_dict(latin_alpha)

cryptor(dicto, test_message, True)

cryptor(dicto, encrypted_message, False)