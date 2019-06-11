algorithm = []
algorithm2 = []
pick = []

def enc(character , val):    
    encrypterchar = "(" + hex(int(ord(character)+ val)) + ")"
    return encrypterchar

def dec(character , val):    
    number = int(character, 16)
    number = number - val
    intnum = int(number)
    decryptchar = chr(intnum)
    return decryptchar

def enc2(character , val):
    encrypterchar = chr(ord(character)+val)
    return encrypterchar

def dec2(character , val):
    decrypterchar = chr(ord(character)-val)   
    return decrypterchar

def keycheck(keystring):
    if len(keystring) != 16:
        print ("Key must be 16 characters long")
        keychecker = False
        return False
    
    
    algorithm_calc(keystring)      
    return True

def algorithm_calc(key):      
    a = []
    count = 0
    for i in key:
        a.insert(count,ord(i))
        count+=1
        
    algorithm.insert(0, a[0] / a[1] * a[2] / a[3] * a[4] / a[5] * a[6] * a[7] / a[8] * a[9] * a[10] * a[11] / a[12] * a[13] * a[14] * a[15])		   
    algorithm.insert(1, a[0] * a[1] / a[2] * a[3] / a[4] * a[5] / a[6] * a[7] * a[8] * a[9] * a[10] * a[11] / a[12] * a[13] / a[14] * a[15]) 
    algorithm.insert(2, a[0] * a[1] * a[2] / a[3] * a[4] / a[5] * a[6] / a[7] * a[8] * a[9] / a[10] / a[11] * a[12] / a[13] * a[14] / a[15]) 
    algorithm.insert(3, a[0] * a[1] * a[2] * a[3] / a[4] * a[5] * a[6] * a[7] / a[8] * a[9] / a[10] * a[11] / a[12] * a[13] / a[14] * a[15]) 
    algorithm.insert(4, a[0] / a[1] / a[2] * a[3] * a[4] * a[5] / a[6] * a[7] * a[8] / a[9] * a[10] * a[11] * a[12] / a[13] * a[14] * a[15]) 
    algorithm.insert(5, a[0] * a[1] * a[2] / a[3] * a[4] / a[5] * a[6] * a[7] * a[8] * a[9] * a[10] / a[11] * a[12] * a[13] / a[14] * a[15]) 
    algorithm.insert(6, a[0] * a[1] * a[2] * a[3] / a[4] * a[5] * a[6] / a[7] * a[8] / a[9] * a[10] * a[11] * a[12] / a[13] * a[14] / a[15]) 			   

    algorithm2.insert(0, a[1]  + a[4]  - a[7]  + a[10]  + a[14]  + a[2]  - a[9]  - a[0]  - a[5]  - a[15]  - a[12]  + a[13]  + a[11]  + a[6]  - a[3]  - a[8] )			   
    algorithm2.insert(1, a[2]  - a[5]  + a[10]  + a[4]  - a[15]  + a[1]  + a[14]  + a[9]  - a[3]  + a[12]  - a[6]  + a[8]  - a[0]  - a[11]  - a[7]  - a[13] )
    algorithm2.insert(2, a[0]  - a[1]  + a[2]  + a[3]  - a[4]  + a[5]  + a[6]  - a[7]  - a[8]  + a[9]  + a[10]  - a[11]  + a[12]  - a[13]  + a[14]  - a[15] )
    algorithm2.insert(3, a[0]  + a[1]  - a[2]  - a[3]  + a[4]  - a[5]  + a[6]  - a[7]  + a[8]  + a[9]  + a[10]  + a[11]  + a[12]  + a[13]  + a[14]  + a[15] )
    algorithm2.insert(4, a[0]  + a[1]  + a[2]  + a[3]  + a[4]  + a[5]  + a[6]  + a[7]  + a[8]  + a[9]  - a[10]  + a[11]  + a[12]  + a[13]  - a[14]  + a[15] )
    
    pick.insert(0, (a[0] * a[1]) %((a[14] * a[15]) % 500))
    pick.insert(1, (a[2] * a[3]) %((a[14] * a[15]) % 300))
    pick.insert(2, (a[4] * a[5]) %((a[14] * a[15]) % 999))
    pick.insert(3, (a[6] * a[7]) %((a[14] * a[15]) % 888))
    pick.insert(4, (a[8] * a[9]) %((a[14] * a[15]) % 623))
    pick.insert(5, (a[10] * a[11]) %((a[14] * a[15]) % 562))
    pick.insert(6, (a[12] * a[13]) %((a[14] * a[15]) % 894))

    for x in range(5):
        if algorithm2[x] < 0:
            algorithm2[x]+= 185
    
    for i in range(7):
        pick[i] = pick[i] % 10
        if pick[i] == 0:
		        pick[i] = 3           
    return

def encode_text(key,text):
    enctext = ""

    if  keycheck(key) == False:
        print ("Error no key")
        return
        
    maxcount  = len(text)
    
    for i in range(maxcount):
        if i % pick[0] == 0:
            enctext += enc(text[i], algorithm[0])
        elif i % pick[1] == 0:
            enctext += enc(text[i], algorithm[1])
        elif i % pick[2] == 0:
            enctext += enc(text[i], algorithm[2])
        elif i % pick[3] == 0:
            enctext += enc(text[i], algorithm[3])
        elif i % pick[4] == 0:
            enctext += enc(text[i], algorithm[4])
        elif i % pick[5] == 0:
            enctext += enc(text[i], algorithm[5])
        else:
            enctext += enc(text[i], algorithm[6])

    text2 = enctext
    enctext = ""
    maxcount = len(text2)

    for i in range(maxcount):
        if i % pick[6] == 0:
            enctext += enc2(text2[i], algorithm2[0])
        elif i % pick[5] == 0:
            enctext += enc2(text2[i], algorithm2[1])
        elif i % pick[4] == 0:
            enctext += enc2(text2[i], algorithm2[2])
        elif i % pick[3] == 0:
            enctext += enc2(text2[i], algorithm2[3])			
        else:
            enctext += enc2(text2[i], algorithm2[4])

    return enctext

def decode_text(key, text):
    dectext = ""

    if  keycheck(key) == False:
        print ("Error no key")
        return

    maxcount  = len(text)

    for i in range(maxcount):
        if i % pick[6] == 0:
            dectext += dec2(text[i], algorithm2[0])
        elif i % pick[5] == 0:
            dectext += dec2(text[i], algorithm2[1])
        elif i % pick[4] == 0:
            dectext += dec2(text[i], algorithm2[2])
        elif i % pick[3] == 0:
            dectext += dec2(text[i], algorithm2[3])
        else:
            dectext += dec2(text[i], algorithm2[4]);               

    text2 = dectext
    dectext = ""
    maxcount = len(text2)

    count = 0
    textarray = []

    for i in range(maxcount):
        if text2[i] == "(":
            holder = ""
        elif text2[i] == ")":
            textarray.insert(count,holder)
            count +=1
        else:
            holder+= text2[i]                
    
    for i in range(count):
        if i % pick[0] == 0:
            dectext += dec(textarray[i], algorithm[0])
        elif i % pick[1] == 0:
            dectext += dec(textarray[i], algorithm[1])
        elif i % pick[2] == 0:
            dectext += dec(textarray[i], algorithm[2])
        elif i % pick[3] == 0:
            dectext += dec(textarray[i], algorithm[3])
        elif i % pick[4] == 0:
            dectext += dec(textarray[i], algorithm[4])
        elif i % pick[5] == 0:
            dectext += dec(textarray[i], algorithm[5])
        else:
            dectext += dec(textarray[i], algorithm[6])

    return  dectext      

# code example on how to encrypt and decrypt
print (encode_text("A000000000000000","Hello world"))
print(decode_text("A000000000000000", "ÐʁȉÛǵʳÛʁØØǅʉÑɹǁĠÛʵĊʄǁØǁʇÝɺƹØȉʴáʴÑÐǁˉÛʵǳÛØʁØʇǴÑƹʁĠʴǊĎƺɹØˉÛČǳʄØʁǁÚØɺÐʁȉÛǵʳÛʁǁØǈʈÑɹØĠǄʵĊʄǁØØʇĎɺƹØȉʴĉʃƺÐǁˉÛʵĊÛǁʁØʇǴÑÐʁĠʴǊÜƺ"))