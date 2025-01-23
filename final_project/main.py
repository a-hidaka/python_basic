
from inventory import invrentory_manager,shop

invrentory_manager.all_stock_info()

invrentory_manager.all_stock_info()
if __name__ == "__main__":
    print("<X001>の場合")
    invrentory_manager.all_stock_info()
    invrentory_manager.add_stock("X001", 10)
    invrentory_manager.all_stock_info()

    print("\n<A001>の場合")
    invrentory_manager.all_stock_info()
    invrentory_manager.add_stock("A001", 10)
    invrentory_manager.all_stock_info()

# if __name__ == "__main__":
#     print("<X001>の場合")
#     invrentory_manager.sell_product("X001", 5)
#     invrentory_manager.all_stock_info()

#     print("\n<A001>の場合")
#     invrentory_manager.sell_product("A001", 5)
#     invrentory_manager.all_stock_info()

if __name__ == "__main__":
    print("<A001>の場合")
    invrentory_manager.sell_product("A001", 30)
    invrentory_manager.all_stock_info()

if __name__ == "__main__":
    invrentory_manager.calculate_total_value()

if __name__ == "__main__":
    invrentory_manager.sell_product("A002", 10)