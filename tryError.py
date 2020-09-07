try:
    print("오류 뜨기 전")
    print(int('asdf'))
except Exception as e:
    print(e)
finally:
    print("none")