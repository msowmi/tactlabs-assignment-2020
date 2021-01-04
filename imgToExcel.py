from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb=Workbook()
ws=wb["Sheet"]
img=Image("pic.png")
ws.add_image(img, "D5")
wb.save("Image_workbook.xlsx")


