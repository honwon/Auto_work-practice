from openpyxl import load_workbook

wb = load_workbook("excelExam.xlsx")

# 시트 선택
data = wb["Sheet_test"]

# 영역 지정
area = data['A1:C3']
for row in area:
    for cell in row:
        print(cell.value)

print("-"*20)

# 열 지정
cols = data["A:B"]
for col in cols:
    for cell in col:
        print(cell.value)

print("-"*20)

# 행 지정
rows = data["2:3"]
for row in rows:
    for cell in row:
        print(cell.value)