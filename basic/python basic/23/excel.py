// 함수 들고옴
from openpyxl import load_workbook

// 클래스 형태로 들고옴
wb = load_workbook('excelExam.xlsx')

// active 활성화된 엑셀 시트 (마지막으로 활성화 된 시트)
data = wb.active

// 원하는셀 인덱스
print(data['A1'].value)
print(data['A2'].value)
print(data['B1'].value)
print(data['B2'].value)