def cost_coffee(kind):
    if kind == 'A':
        cost_cff = 3900
    elif kind == 'CM':
        cost_cff = 4500
    elif kind == 'CL':
        cost_cff = 5000
    elif kind == 'GT':
        cost_cff = 5500
    return cost_cff

def cost_size(size):
    if size == 'G':
        cost_sz = 1000
    elif size == 'R':
        cost_sz = 500
    elif size == 'S':
        cost_sz = 0
    return cost_sz

def cost_total(cost_cff, cost_sz):
    cost_ttl = cost_cff + cost_sz
    return cost_ttl


for i in range(5):
    kind = input("Choose the menu. \n A(아메리카노) / CM(카페모카) / CL(카페라떼) / GT(그린티)")
    size = input("Choose the size. \n G(Grande) / R(Regular) / S(Short)")

    cost_cff = cost_coffee(kind)
    cost_sz  = cost_size(size)
    cost_ttl = cost_total(cost_cff, cost_sz)

    print("The total price is %d \." %cost_ttl)
    print("Thank you for visiting. \n")
