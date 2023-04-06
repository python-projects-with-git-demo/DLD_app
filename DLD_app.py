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

