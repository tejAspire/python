from openpyxl import Workbook
from openpyxl.styles import Font

# Create a new workbook
wb = Workbook()

# Create sheets and set titles
sheet = wb.active
sheet.title = "Language"
wb.create_sheet(title="Capital")

# Data
lang = ["Kannada", "Telugu", "Tamil"]
state = ["Karnataka", "Telangana", "Tamil Nadu"]
capital = ["Bengaluru", "Hyderabad", "Chennai"]
code = ['KA', 'TS', 'TN']

# Set headers and apply bold font
for sheet_name in ["Language", "Capital"]:
    sheet = wb[sheet_name]
    sheet.cell(row=1, column=1).value = "State"
    sheet.cell(row=1, column=2).value = "Language" if sheet_name == "Language" else "Capital"
    sheet.cell(row=1, column=3).value = "Code"

    ft = Font(bold=True)
    for row in sheet["A1:C1"]:
        for cell in row:
            cell.font = ft

# Populate data
for sheet_name, data in zip(["Language", "Capital"], [state, lang, code] if sheet_name == "Language" else [state, capital, code]):
    sheet = wb[sheet_name]
    for i, value in enumerate(data, start=2):
        sheet.cell(row=i, column=1).value = value

# Save workbook
wb.save("demo.xlsx")
