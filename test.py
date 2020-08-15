import xlrd
from x_forecast import forecast

data = xlrd.open_workbook('M3C.xls')
Sheet = 'M3Year'
ind = data.sheet_by_name(Sheet)
Rows = ind.nrows
MM = []
for row in range(1, Rows):
    item = []
    for col in range(6, 53):
        val = ind.cell(row, col).value
        if val != '':
            item.append(round(val))
    MM.append(item)
forecast.Forecast_method(MM[0], 6)
