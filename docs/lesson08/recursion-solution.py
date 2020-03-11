def fiboancci(n, remember = dict()):
    if n <= 2:
        return 1
    if n in remember:
        return remember[n]
    result = fiboancci(n-1) + fiboancci(n-2)
    remember[n] = result
    return result

for i in range(100):
    print("fib({}) = {}".format(i,fiboancci(i)))


def wildcard_binary(pattern):
    if pattern.find("*") >= 0:
        wildcard_binary(pattern.replace("*","0",1))
        wildcard_binary(pattern.replace("*","1",1))
    else:
        print(pattern)

wildcard_binary("110*0*")
wildcard_binary("****")

def count_steps(stairs):
    if stairs == 0:
        return 0
    elif stairs == 1:
        return 1
    elif stairs == 2:
        return 2
    return count_steps(stairs-1) + count_steps(stairs-2) + count_steps(stairs-3)

print(count_steps(5))   # 11
print(count_steps(20))  # 101902

def coins(cents, quarters = 0, dimes = 0, nickles = 0, pennies = 0):
    if cents <= 0:
        print("Quarters: {} Dimes: {} Nickles: {} Pennies: {}".format(quarters, dimes, nickles, pennies))
        return
    if cents >= 25:
        coins(cents - 25, quarters + 1, dimes, nickles, pennies)
    if cents >= 10:
        coins(cents - 10, quarters, dimes + 1, nickles, pennies)
    if cents >= 5:
        coins(cents - 5, quarters, dimes, nickles + 1, pennies)
    if cents >= 1:
        coins(cents - 1, quarters, dimes, nickles, pennies + 1)

coins(20)

def find_
