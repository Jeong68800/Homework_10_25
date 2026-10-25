class Product :
    def __init__(self , name , price , stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self) :
        return f"(제품이름 : {self.name} , 가격 : {self.price} , 재고 : {self.stock})"


def total_price(product , quantity):
    payment_amount = product.price*quantity

    if payment_amount >= 80000 :
        print("현재 주문 금액이 기준을 충족하여 배송비 0원 혜택이 적용되었습니다")
        return payment_amount # payment_amount = payment_amount

    elif 30000 <= payment_amount < 80000 :
        return payment_amount + 4000 # payment_amount = payment_amount + 4000

    else :
        print("30,000원 이상시 배송가능 합니다.")
        return None
