try:    
    import product,shop
except ModuleNotFoundError:
     from inventory import product,shop

def all_stock_info():
    for i in product.products:
        print(f"{i.name} {i.stock}")


def add_stock(id, quantity):
    for i in product.products:
        if i.id == id:
            i.stock += quantity
            return
    print("商品IDがありません")
def sell_product(id,quantity):
    if shop.today_weekday == shop.main_store.holiday:
        print("定休日です")
        return
    for i in product.products:
        if i.id == id:
            if i.stock >= quantity:
                i.stock -= quantity
                print(f"{quantity} 個の {i.name} を販売しました。")
                return
            else:
                print("在庫が不足しています。")
                return
    print("商品IDがありません")

def calculate_total_value():
    total_value = 0
    for i in product.products:
        total_value += i.price * i.stock
    print(f"{total_value}円")



if __name__ == "__main__":
    print("商品一覧")
    all_stock_info()


