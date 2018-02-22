alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
keimeno=raw_input("dose keimeno:")
keim=[]
rot13=[]
for i in range(len(keimeno)):
    keim.append(keimeno[i])
for i in range(len(keim)):
    for j in range(len(alphabet)):
        if(keim[i]==alphabet[j]):
            if(j+13<=25):
                rot13.append(alphabet[j+13])
            else:
                rot13.append(alphabet[j+13-26])
print rot13