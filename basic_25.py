try:
    # 例外が発生する可能性のあるコード
    number = 0
    result = 10 / number
    print(result)
except TypeError as error:
    # TypeErrorが発生した場合の処理
    print("タイプエラーです",f"error内容:{error}")
except ZeroDivisionError as error:
    print(f"ゼロで割れません:{error}")
except Exception:
    print("エラーが出てる、何かはわからん")
finally:
    print("try-exceptが終わったよ")


    

