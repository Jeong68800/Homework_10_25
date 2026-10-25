from homework_10_25 import Product , total_price

print("===== 쇼핑몰에 오신 것을 환영합니다! =====")

p1 = Product("치노펜츠" , 29900 , 10)
p2 = Product("슬랙스" , 44900 , 10)
p3 = Product("데님팬츠" , 35900 , None)
p4 = Product("조거팬츠" , 67200 , 3)
p5 = Product("코튼팬츠" , 56900 , 9)
p6 = Product("스웻팬츠" , 49900 , 8)

print("1. 치노펜츠\n2. 슬랙스\n3. 데님팬츠\n4. 조거팬츠\n5. 코튼팬츠\n6. 스웻팬츠")

product_list = [p1, p2, p3, p4, p5, p6]

n=input("구매할 제품 번호 : ")
n=int(n)

if n < 1 or n > 6 :
    print("존재하지 않는 제품 번호입니다.")

else :
    product = product_list[n-1]
    print(f"제품 : {product}")

    quantity = input("수량 : ")
    quantity = int(quantity)

    if product.stock is None :
        print(f"재고가 부족합니다.")

    elif quantity < 1 :
        print("수량을 1개 이상을 선택해주세요.")

    elif quantity > product.stock :
        print(f"재고가 부족합니다. 남은 재고는 {product.stock}개 입니다.")

    else :
        total = total_price(product , quantity)
        if total is not None: #변수가 비어 있지 않다면
            product.stock = product.stock - quantity
            print(f"{product.name} {quantity}개\n결제 금액 : {total}원 입니다.")

