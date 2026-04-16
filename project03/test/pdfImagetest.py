import pdfplumber

# 加载一个pdf文件
pdf = pdfplumber.open('./test.pdf')

# pdf中每一页都对应一个Page对象
# 第一个page对象
page1 = pdf.pages[0]
# 第二个page对象
page2 = pdf.pages[1]


print(page1.images)
print(page2.images)

# 直接提取某一页图片，有才提取
# img = page2.images[0]
# ppoint = (img['x0'],img['top'],img['x1'],img['bottom'])
# page2.crop(ppoint).to_image().save('test1.png')

# 整个页面提取为图片
# antialias=True 开启抗锯齿
# resolution=1080 高清1080p
# page1.to_image(antialias=True,resolution=1080).show()
page1.to_image(antialias=True).save('test2.png')
page1.to_image(antialias=True,resolution=1080).save('test3.png')

