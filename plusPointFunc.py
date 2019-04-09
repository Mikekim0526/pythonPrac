percent=[0.012, 0.02, 0.018, 0.015]

while 1:
    item=int(input("구매한 상품을 입력하세요.  (1)화장품 (2)커피 (3)도서 (4)의류"))-1
    cost=int(input("구매한 가격을 입력하세요."))

    def point(item, cost) :
        plus=cost*percent[item]
        return plus

    print("%d 원 적립되었습니다. \n" %point(item, cost))
