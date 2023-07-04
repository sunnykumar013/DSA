# def stock(arr1):
#     print(arr1)
#
#     netprofit = -9872160
#     for i in range(len(arr1)):
#         max_profit =0
#
#         for j in range(i+1,len(arr1)):
#             if arr1[j] > arr1[i]:
#                 profit = arr1[j] - arr1[i]
#
#                 if(profit > max_profit):
#                     max_profit = profit
#
#         netprofit = max(netprofit, max_profit)
#
#     print(netprofit)
#
#

def stock(arr1):
    buy = arr1[0]
    max_profit =0

    for i in range(1,len(arr1)):

        if( buy > arr1[i]):
            buy = arr1[i]

        elif(arr1[i] - buy > max_profit):
            max_profit = arr1[i] - buy

    print(max_profit)



prices = [7, 1, 5, 3, 6, 4]
stock(prices)