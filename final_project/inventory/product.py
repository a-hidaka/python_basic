class Product:
    def __init__(self,id,name,price,stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        
    def inint_test(self):
        print(f"{self.name}のIDは{self.id}番。在庫数は{self.stock}で商品単体の価格は{self.price}です。")

    # 商品を登録
products = [
    Product("A001", "ノートパソコン", 80000, 10),
    Product("A002", "マウス", 3000, 50),
    Product("A003", "キーボード", 5000, 30)
]


if __name__ == "__main__":
    question1 = Product("A001","ホッチキス","1000","21")
    question1.inint_test()


