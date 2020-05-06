from ..dao.mapper import *
class ParaA:

    def method_a1(self, a, b):
        print("%d * %d = %d" % (a, b, a * b))

    def method_a2(self, a, b, c):
        print("min(%d, %d, %d) = %d" % (a, b, c, min(a, b, c)))

class ParaB:

    def method_b1(a, b):
        print("100 * %d + %d = %d" % (a, b, 100 * a + b))

    def method_b2(a, b, c, d):
        print("(%d + %d) * (%d + %d) = %d" % (a, b, c, d, (a + b) * (c + d)))



class ParaC:

    def method_c1(a, b):
        print("%d + %d = %d" % (a, b, a + b))

    def method_c2(c, d, e):
        print("max(%d, %d, %d) = %d" % (c, d, e, max(c, d, e)))

class ParaD:

    def method_d1(self):
        df =Mapper.read_data("select * from TC_PSR_PARA")
        for index, row in df.iterrows():
            print(index, row['TRADE_DATE'], row['PSR'])


