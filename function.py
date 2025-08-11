# def cal_sum(a, b):
#     # sum = a + b
#     # print(sum)
#     return a + b
# # cal_sum(2, 10)
# sum = cal_sum(20, 20)
# print(sum)

# def print_hello():
#     print("heloo")

# print_hello()    
# print_hello()

def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

cal_avg(98, 97, 95)

cities = ["ktm", "nuwakot", "pokhara", "latitpur"]


def print_len(list):
    print(len(list))

print_len(cities)  

def cal_fact(n):
    fact = 1
    for i in range (1, n+1):
        fact *= i
        print(fact)
cal_fact(5)   

def converter(usd_val):
    npr_val = usd_val * 136
    print(usd_val, "usd=", npr_val, "npr")

converter(45)   
