#emfanisi minimatos
number= raw_input("give number 1 - 1000:")

#dimiourgia listwn
dozens=["I","II","III","IV","V","VI","VII","VIII","IX"]
hundreds=["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
thousands=["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
dozensthousands=["M","MM","MMM","M-V","-V","-VM","-VMM","-VMMM","M-X"]
hundredsthousands=["-X","-X-X","-X-X-X","-X-L","-L","-L-X","-L-X-X","-L-X-X-X","-X-C"]
million=["-C","-C-C","-C-C-C","-C-D","-D","-D-C","-D-C-C","-D-C-C-C","-C-M"]

#spasimo arithmou se psifia
num= int(number)
unit = num%10
dozen = (num//10)%10
hundred= ((num//10)//10)%10
thousand=(num//1000)%10
dozthous=(num//1000)//10%10
hundthous=(num//10000)//10

#sinartisi opou o arithmos einai megaliteros tou 1000
def big1000(num):
    if (thousand != 0 and dozthous != 0 and hundthous != 0):
        return million[hundthous - 1] + hundredsthousands[dozthous - 1] + dozensthousands[thousand - 1]
    elif (thousand == 0 and dozthous != 0 and hundthous != 0):
        return million[hundthous - 1] + hundredsthousands[dozthous - 1]
    elif (dozthous == 0 and thousand != 0 and hundthous != 0):
        return million[hundthous - 1] + dozensthousands[thousand - 1]
    elif (hundthous == 0 and dozthous != 0 and thousand != 0):
        return hundredsthousands[dozthous - 1] + dozensthousands[thousand - 1]
    elif (hundthous == 0 and thousand == 0 and dozthous != 0):
        return hundredsthousands[dozthous - 1]
    elif (hundthous == 0 and dozthous == 0 and thousand != 0):
        return dozensthousands[thousand - 1]
    elif (thousand == 0 and dozthous == 0 and hundthous != 0):
        return million[hundthous - 1]
    elif (thousand == 0 and dozthous == 0 and hundthous != 0):
        return million[hundthous - 1]

#sinartisi opou o arithmos einai mikroteros tou 1000
def small1000(num):
    if (unit != 0 and dozen != 0 and hundred != 0):
        return thousands[hundred - 1] + hundreds[dozen - 1] + dozens[unit - 1]
    elif (unit == 0 and dozen != 0 and hundred != 0):
        return thousands[hundred - 1] + hundreds[dozen - 1]
    elif (dozen == 0 and unit != 0 and hundred != 0):
        return thousands[hundred - 1] + dozens[unit - 1]
    elif (hundred == 0 and dozen != 0 and unit != 0):
        return hundreds[dozen - 1] + dozens[unit - 1]
    elif (hundred == 0 and unit == 0 and dozen != 0):
        return hundreds[dozen - 1]
    elif (hundred == 0 and dozen == 0 and unit != 0):
        return dozens[unit - 1]
    elif (unit == 0 and dozen == 0 and hundred != 0):
        return thousands[hundred - 1]
    elif (unit == 0 and dozen == 0 and hundred != 0):
        return thousands[hundred - 1]
    elif(unit == 0 and dozen == 0 and hundred == 0):
        return ""

#elegxos arithmou na einai mikroteros tou 1000
if(num<1000):
    latin = small1000(num)

#elegxos arithmou na einai megaliteros tou 1000 kai mikroteros kai ison tou 999999
elif(num>1000 and num<=999999):
    latin= str(big1000(num))+str(small1000(num))
else:
    #emfanisi minimatos
    print ("this number is out of limits")

#tipwse aakeraio arithmo
print unit
print dozen
print hundred
print thousand
print dozthous
print hundthous

#tipwse latiniko arithmo
print latin