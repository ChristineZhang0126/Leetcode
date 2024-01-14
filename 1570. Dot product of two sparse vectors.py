1570. Dot product of two sparse vectors
given two sparse vectors, compute their dot product.
class sparsevector(object):
    def __init__(self,num):
        self.new_hash = {}
        #self.new_num = num
        for each in range(len(num)):
            self.new_hash[each] = num[each]

        

    def dotproduct(self, num1):
        the_sum = 0    
        for each in num1.new_hash:
            if num1.new_hash[each] != 0 and self.new_hash[each] != 0:
                the_sum += self.new_hash[each] * num1.new_hash[each]
        return the_sum
 #v1 = sparsevector(num1)
 #v2 = sparsevecotr(num2)
 #v1.dotproduct(v2)
 