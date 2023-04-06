class deci_binary_conversion:
    def __init__(self, a):
        self.r = ''
        self.bin_ = int(a)
        self.bin_dec = a - self.bin_

    def binary_no(self, bin):
        self.r += str(bin % 2)
        if bin // 2 == 0:
            return int(self.r[::-1])
        else:
            return self.binary_no(bin // 2)

a = int(input())
c = deci_binary_conversion(a)
print(c.binary_no(c.bin_))
