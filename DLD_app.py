class deci_binary_conversion:
    def __init__(self, a):
        self.r1 = ''
        self.r2 = ''
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
a = float(input())
c = deci_binary_conversion(a)
print(c.result)
class deci_octal_conversion:
    def __init__(self, a):
        self.r1 = ''
        self.r2 = ''
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
                
        print(self.r2)
        return self.r2

ck = deci_octal_conversion(a)
print(ck.result)
