class deci_binary_conversion:
    def __init__(self, a):
        self.r1 = ''
        self.r2 = ''
        a=float(a)
        self.bin_ = int(a)
        self.bin_dec = a - self.bin_
        self.bn = self.binary_no(self.bin_)
        self.bd = self.binary_dec(self.bin_dec)
        self.result = self.binary_result(self.bn, self.bd)

    def binary_result(self, bn, bd):
        return "{:.4f}".format(float(bn + '.' + bd))

    def binary_no(self, bin_):
        self.r1 += str(bin_ % 2)
        if bin_ // 2 == 0:
            return self.r1[::-1]
        else:
            return self.binary_no(bin_ // 2)

    def binary_dec(self, bin_dec):
        while bin_dec-int(bin_dec)!= 0:
            bin_dec *= 2
            if bin_dec < 1:
                self.r2 += '0'   
            else:
                bin_dec -= 1
                self.r2 += '1'
        return self.r2

class deci_octal_conversion:
    def __init__(self, a):
        self.r1 = ''
        self.r2 = ''
        a=float(a)
        self.oct_ = int(a)
        self.oct_dec = a - self.oct_
        self.on = self.octal_no(self.oct_)
        self.od = self.octal_dec(self.oct_dec)
        self.result = self.octal_result(self.on, self.od)

    def octal_result(self, on, od):
        return "{:.4f}".format(float(on + '.' + od))

    def octal_no(self, oct_):
        self.r1 += str(oct_ % 8)
        if oct_ // 8 == 0:
            return self.r1[::-1]
        else:
            return self.octal_no(oct_ // 8)

    def octal_dec(self, oct_dec):
        while oct_dec-int(oct_dec)!= 0:
            oct_dec *= 8
            if oct_dec < 1:
                self.r2 += '0'   
            else:
                self.r2 += str(int(oct_dec))
                oct_dec -= int(oct_dec)
                
        
        return self.r2

class deci_hexa_conversion:
    def __init__(self, a):
        self.r1 = ''
        self.r2 = ''
        a=float(a)
        self.hex_ = int(a)
        self.hex_dec = a - self.hex_
        self.hn = self.hexa_no(self.hex_)
        self.hd = self.hexa_dec(self.hex_dec)
        self.result = self.hexa_result(self.hn, self.hd)

    def hexa_result(self, hn, hd):
        return "{}.{:.4s}".format(hn,hd)

    def hexa_no(self, hex_):
        if hex_%16<10:
            self.r1 += str(hex_ % 16)
        elif hex_%16==10:
            self.r1+='A'
        elif hex_%16==11:
            self.r1+='B'
        elif hex_%16==12:
            self.r1+='C'
        elif hex_%16==13:
            self.r1+='D'
        elif hex_%16==14:
            self.r1+='E'
        elif hex_%16==15:
            self.r1+='F'
            
        if hex_ // 16 == 0:
            return self.r1[::-1]
        else:
            return self.hexa_no(hex_ // 16)

    def hexa_dec(self, hex_dec):
        while hex_dec-int(hex_dec)!= 0:
            hex_dec *= 16
            if hex_dec < 1:
                self.r2 += '0'   
            else:
                if int(hex_dec)<10:
                    self.r2 += str(int(hex_dec))
                    hex_dec -= int(hex_dec)
                elif int(hex_dec)==10:
                    self.r2+='A'
                    hex_dec -= int(hex_dec)
                elif int(hex_dec)==11:
                    self.r2+='B'
                    hex_dec -= int(hex_dec)
                elif int(hex_dec)==12:
                    self.r2+='C'
                    hex_dec -= int(hex_dec)
                elif int(hex_dec)==13:
                    self.r2+='D'
                    hex_dec -= int(hex_dec)
                elif int(hex_dec)==14:
                    self.r2+='E'
                    hex_dec -= int(hex_dec)
                elif int(hex_dec)==15:
                    self.r2+='F'
                    hex_dec -= int(hex_dec)
                
                    
       
        return self.r2


class binary_to_decimal:
    def __init__(self,a):
        self.r1=0
        self.r2=0
        a=float(a)
        self.bin_value=str(a)
        self.bin_dec,self.bin_poi=(self.bin_value.split('.'))
        self.bd=self.binary_decimal(self.bin_dec)
        self.bp=self.binary_point(self.bin_poi)
        self.result=self.decimal_result(self.bd,self.bp)
    def decimal_result(self,k,t):
        return k+t
        
    def binary_decimal(self,k):
        k=[int(i) for i in k[::-1]]
        for i in range(len(k)):
            self.r1+=k[i]*(2**i)    
        return self.r1
    def binary_point(self,k):
        k=[int(i) for i in k]
        for i in range(len(k)):
            self.r2+=k[i]*(2**(-(i+1)))
        
        return self.r2  
        

class octal_to_decimal:
    def __init__(self,a):
        self.r1=0
        self.r2=0
        a=float(a)
        self.oct_value=str(a)
        self.oct_dec,self.oct_poi=(self.oct_value.split('.'))
        self.od=self.octal_decimal(self.oct_dec)
        self.op=self.octal_point(self.oct_poi)
        self.result=self.decimal_result(self.od,self.op)
    def decimal_result(self,k,t):
        return k+t
        
    def octal_decimal(self,k):
        k=[int(i) for i in k[::-1]]
        for i in range(len(k)):
            self.r1+=k[i]*(8**i)    
        return self.r1
    def octal_point(self,k):
        k=[int(i) for i in k]
        for i in range(len(k)):
            self.r2+=k[i]*(8**(-(i+1)))
        
        return self.r2

class hexa_to_decimal:
    def __init__(self,a):
        self.r1=0
        self.r2=0
        if '.' not in a:
            a=a+'.0'
        self.hex_dec,self.hex_poi=(a.split('.'))
        self.hd=self.hexa_decimal(self.hex_dec)
        self.hp=self.hexa_point(self.hex_poi)
        self.result=self.decimal_result(self.hd,self.hp)
    def decimal_result(self,k,t):
        return k+t
        
    def hexa_decimal(self,k):
        k=k.upper()
        self.l=[] 
        for i in k[::-1]:
            if i=='A':
                self.l.append(10)
            elif i=='B':
                self.l.append(11)
            elif i=='C':
                self.l.append(12)
            elif i=='D':
                self.l.append(13)
            elif i=='E':
                self.l.append(14)
            elif i=='F':
                self.l.append(15)
            else:
                self.l.append(int(i))
        for i in range(len(k)):
            self.r1+=self.l[i]*(16**i)    
        return self.r1
    def hexa_point(self,k):
        k=k.upper()
        self.l=[] 
        for i in k:
            if i=='A':
                self.l.append(10)
            elif i=='B':
                self.l.append(11)
            elif i=='C':
                self.l.append(12)
            elif i=='D':
                self.l.append(13)
            elif i=='E':
                self.l.append(14)
            elif i=='F':
                self.l.append(15)
            else:
                self.l.append(int(i))
        for i in range(len(k)):
            self.r2+=self.l[i]*(16**(-(i+1)))
        
        return self.r2
class hexadecimal_to_binary:
    def __init__(self,a):
        self.result1=hexa_to_decimal(a)
        self.final_result=deci_binary_conversion(self.result1.result)
        self.result=self.resultfin()
    def resultfin(self):
        return self.final_result.result

class octal_to_binary:
    def __init__(self,a):
        self.result1=octal_to_decimal(a)
        self.final_result=deci_binary_conversion(self.result1.result)
        self.result=self.resultfin()
    def resultfin(self):
        return self.final_result.result

class hexadecimal_to_octal:
    def __init__(self,a):
        self.result1=hexa_to_decimal(a)
        self.final_result=deci_octal_conversion(self.result1.result)
        self.result=self.resultfin()
    def resultfin(self):
        return self.final_result.result
class binary_to_octal(binary_to_decimal):
    def __init__(self,a):
        self.r1=''
        self.r2=''
        a=float(a)
        self.binary_value=str(a)
        self.bin_dec,self.bin_poi=(self.binary_value.split('.'))
        self.bo=self.binary_octal(self.bin_dec)
        self.bp=self.bin_oct_point(self.bin_poi)
        self.result=self.decimal_result(self.bo,self.bp)
    def decimal_result(self,k,t):
        return k+'.'+t
    def binary_octal(self,k):
        l=[]
        t=''
        if len(k)%3!=0:
            if len(k)%3==1:
                k='00'+k 
            elif len(k)%3==2:
                k='0'+k
        for i in k[::-1]+'r':
            if len(t)!=3:
                t+=i
            else:
                l.append(t[::-1])
                t=''
                t+=i
        
        for i in l[::-1]:
            k=binary_to_decimal(i)
            self.r1+=str(k.bd)
        
        return(self.r1)
    def bin_oct_point(self,k):
        l=[]
        t=''
        if len(k)%3!=0:
            if len(k)%3==1:
                k+='00' 
            elif len(k)%3==2:
                k+='0'
        for i in k +'r':
            if len(t)!=3:
                t+=i
            else:
                l.append(t)
                t=''
                t+=i 
        for i in l:
            k=binary_to_decimal(i)
            self.r2+=str(k.bd)
        
        return(self.r2)
class binary_to_hexadecimal:
    def __init__(self,a):
        self.r1=''
        self.r2=''
        a=float(a)
        self.binary_value=str(a)
        self.bin_dec,self.bin_poi=(self.binary_value.split('.'))
        self.bo=self.binary_hexal(self.bin_dec)
        self.bp=self.bin_hex_point(self.bin_poi)
        self.result=self.decimal_result(self.bo,self.bp)
    def decimal_result(self,k,t):
        return k+'.'+t
    def binary_hexal(self,k):
        l=[]
        t=''
        if len(k)%4!=0:
            if len(k)%4==1:
                k='000'+k 
            elif len(k)%4==2:
                k='00'+k
            elif len(k)%4==3:
                k='0'+k
        for i in k[::-1]+'r':
            if len(t)!=4:
                t+=i
            else:
                l.append(t[::-1])
                t=''
                t+=i
        
        for i in l[::-1]:
            k=binary_to_decimal(i)
            ro=deci_hexa_conversion(str(k.bd))
            self.r1+=str(ro.hn)
        
        return(self.r1)
    def bin_hex_point(self,k):
        l=[]
        t=''
        if len(k)%4!=0:
            if len(k)%4==1:
                k+='000' 
            elif len(k)%4==2:
                k+='00'
            elif len(k)%4==3:
                k+='0'
        for i in k +'r':
            if len(t)!=4:
                t+=i
            else:
                l.append(t)
                t=''
                t+=i 
        for i in l:
            k=binary_to_decimal(i)
            ro=deci_hexa_conversion(k.bd)
            self.r2+=str(ro.hn)
        
        return(self.r2)
class octal_to_hexadecimal:
    def __init__(self,a):
        self.result1=octal_to_binary(a)
        self.final_result=binary_to_hexadecimal(self.result1.result)
        self.result=self.resultfin()
    def resultfin(self):
        return self.final_result.result
    
def ones_complement(a):
    b=''
    for i in str(a):
        if i=='0':
            b+='1'
        elif i=='1':
            b+='0'
    return b
def twos_complement(a):
    a=ones_complement(a)

    t=''
    if a[-1]!='1':
        r=(int(a[-1]))^1
        print(r)
        for i in a[0:len(a)-1]:
            t+=i
        
        t+=str(r)
        return t
        
    else:
        rep=0
        
        r=(int(a[-1]))^1
        if a[-2]!='1':
            
            q=(int(a[-2]))^1
            for i in a[0:len(a)-2]:
                t+=i
            t=t+str(q)+str(r)
            return t
        else:
            a="0"+a
            while a[-1]!="0":
                a=a[0:len(a)-1]
                rep+=1
            t=a[0:len(a)-1]+str((int(a[-1]))^1)
           
            for i in range(rep):
                t+='0'
            return t[1:len(t)] 
def sevens_complement(a):
    a=list(a)
    k=''
    for i in a:
        k+=str(7-int(i))
    return k
def eights_complement(a):
    a=sevens_complement(a)
    t=''
    rep=0
    if a[-1]!='7':
        t=str(int(a)+1)
    else:

        while a[-1]=='7':
            a='0'+a
            a=a[0:len(a)-1]
            rep+=1
            if a[-1]!='7':
                t=str(int(a)+1)
                break
        t=t[0:len(t)]
        for i in range(rep):
            t+='0'
    return t
hexadecimal={'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
def fifteens_complement(a):
    a=list(a)
    l=[]
    repo=0
    for i in a:
        i=i.upper()
        l.append(hexadecimal[i])
    k=''
    key_list=list(hexadecimal.keys())
    val_list=list(hexadecimal.values())
    for i in l:
        kl=val_list.index(str(15-int(i)))
        k+=key_list[kl]
    return k
def sixteens_complement(a):
    a=fifteens_complement(a)
    print(a)
    a=list(a)
    k=''
    l=[]
    for i in a:
        l.append(hexadecimal[i])
    k=''
    key_list=list(hexadecimal.keys())
    val_list=list(hexadecimal.values())
    if l[-1]!='15':
        l[-1]=str(int(l[-1])+1)
        for i in l:
            kl=val_list.index(str(i))
            k+=key_list[kl]
    else:
        l.insert(0,"0")
        rep=0
        while l[-1]=='15':
            
            l=l[0:len(l)-1]
            rep+=1
            if l[-1]!='15':
                t=str(int(l[-1])+1)
                break
        for i in l[1:len(l)-1]:
            kl=val_list.index(str(i))
            k+=key_list[kl]
        k+=t
        for i in range(rep):
            k+='0'
    return k
class addition_of_binary:
    def __init__(self,a,b):
        self.num1=binary_to_decimal(a)
        self.num2=binary_to_decimal(b)
        self.res=self.result(self.num1,self.num2)
    def result(self,nu1,nu2):
        self.a= deci_binary_conversion(nu1+nu2)
        return self.a
        