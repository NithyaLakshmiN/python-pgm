# for i in range(0,6):
#     for j in range (6):
#         print("*",end = " ")
#     print()
#
#     #o/p
#     # * * * * * *
#     # * * * * * *
#     # * * * * * *
#     # * * * * * *
#     # * * * * * *
#     # * * * * * *

############################################################################
# for i in range (0,6):
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print()
#
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
#     * * * * * *

############################################################################
# for i in range (0,6):
#     for j in range(6-i):
#         print("*", end=" ")
#     print()
#
#     * * * * * *
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *

############################################################################
#
# for i in range (0,6):
#     for j in range(i,6):
#          print(" ", end=" ")
#     for j in range(i+1):
#        print("*", end=" ")
#     print()
#
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
#     * * * * * *

############################################################################


for i in range (0,6):
    for j in range(i,6):
         print(" ", end=" ")
    for j in range(6-i):
       print("*", end=" ")
    print()
#
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
#     * * * * * *

############################################################################