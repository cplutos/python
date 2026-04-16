import pdfplumber

# 加载一个pdf文件
pdf = pdfplumber.open('./test.pdf')

# 得到pdf的元数据和页数
print(pdf.metadata)
print(pdf.pages)

# pdf中每一页都对应一个Page对象
# 第一个page对象
page1 = pdf.pages[0]
page2 = pdf.pages[1]
# 获得page对象中的各种属性
print(page1.page_number)
# print(page1.width)
# print(page1.height)


# 提取内容
# 1.提取文本内容
print(page1.extract_text())
# layout=True 按照原来的布局来提取内容
print(page1.extract_text(layout=True))
# 2.提取图片
print(page2.images)
# 3.提取表格
print(page1.extract_table())