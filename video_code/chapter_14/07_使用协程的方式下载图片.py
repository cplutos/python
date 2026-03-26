import aiohttp
import asyncio

from requests import session


async def download_picture(session,url):
    print(f'开始下载：{url}')
    response = await session.get(url)
    # 等待数据（防止数据过大，需要等数据读完）
    content = await response.read()
    print('下载完毕')
    with open(url[-70:],'wb') as file:
        file.write(content)
    # 释放连接资源
    await response.release()
async def main():
    url_list = [
        'https://cn.bing.com/images/search?view=detailV2&ccid=SJGV7f%2fd&id=53EC550078F02521BDBE072C5B9F05556FE9A0DA&thid=OIP.SJGV7f_dRfnt_tPF_JGmXgHaE8&mediaurl=https%3a%2f%2fpic4.zhimg.com%2fv2-232e47ec472ead43ffbc339cafd1c447_b.jpg&exph=387&expw=580&q=%e4%b8%96%e7%95%8c%e6%97%85%e6%b8%b8%e8%83%9c%e5%9c%b0&FORM=IRPRST&ck=303D5E9AB1E1DAA50E25F87476E9F3D7&selectedIndex=0&itb=0',
        'https://cn.bing.com/images/search?view=detailV2&ccid=GUiUnh3Z&id=ED5CB77EB75446D1888C1B04F591657EB641E110&thid=OIP.GUiUnh3ZAVW0KO4i2N7H_AHaE6&mediaurl=https%3a%2f%2fpic3.zhimg.com%2fv2-d1f733345b0d11ea4d1bde0e2511dbc8_720w.jpg%3fsource%3d172ae18b&exph=384&expw=578&q=%e4%b8%96%e7%95%8c%e6%97%85%e6%b8%b8%e8%83%9c%e5%9c%b0&FORM=IRPRST&ck=013AE326E8DBEBEEAED85C0F4D6F9EF2&selectedIndex=1&itb=0',
        'https://cn.bing.com/images/search?view=detailV2&ccid=zNMgWWy5&id=666E40C8BA031BFDDDFD0338D9780D40B6F48D6E&thid=OIP.zNMgWWy5sEmcLZ6JB5x5kAHaE7&mediaurl=https%3a%2f%2fts1.tc.mm.bing.net%2fth%2fid%2fR-C.ccd320596cb9b0499c2d9e89079c7990%3frik%3dbo30tkANeNk4Aw%26riu%3dhttp%253a%252f%252fwww.finebornchina.cn%252fuploads%252fallimg%252f140430%252f1-140430150445413.jpg%26ehk%3dHjpp13uPkWtPTUVLZH%252f7V3MKAnXYJJNjmjRq1TE136k%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=553&expw=830&q=%e4%b8%96%e7%95%8c%e6%97%85%e6%b8%b8%e8%83%9c%e5%9c%b0&FORM=IRPRST&ck=8D97C5A80E41D1F957FFB0C7E114953C&selectedIndex=3&itb=0'
    ]
    # 创建回话对象
    session = aiohttp.ClientSession()
    coroutine_list = [download_picture(session,url) for url in url_list]
    # 将多个
    await asyncio.gather(*coroutine_list)

    await session.close()

asyncio.run(main())
