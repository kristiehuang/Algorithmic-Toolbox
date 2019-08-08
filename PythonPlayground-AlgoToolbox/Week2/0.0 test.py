#
def dec_to_bin(n):
    bin = ""

    if (n >= 2):
        addBin = dec_to_bin(n/2)
        textHalf = dec_to_bin(n%2)
        bin += (addBin + textHalf)
        return bin
    else: #number less than 2
        return str(n)


print dec_to_bin(5)
# print "hello"
#
# #
# # 4
#
# adbin = decToBin(2)
# texthalf = "0"
# bin = decToBin(2) + "0"
#         addBin = decToBin(1)
#         texthalf = "0"
#         bin = b
#
# def decimalToBinary(n):
#     bin = ""
#     if(n > 1):
#         # divide with integral result
#         # (discard remainder)
#         decimalToBinary(n//2)
#
#     bin += str(n%2)
#     return bin
#         return "0"
#
#
#
# # Driver code
# if __name__ == '__main__':
#     print(decimalToBinary(2))
