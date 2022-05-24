import imgbbpy
import pandas as pd
import os


def photo_to_excel(username, src):
    df = pd.read_excel('тест.xlsx', sheet_name='тест')
    client = imgbbpy.SyncClient('d3a3ff742c0c449c2ccc67e5837c010d')
    image = client.upload(file=src)
    df.loc[-1, ['имя', 'фото']] = username, image.url
    df.to_excel('тест.xlsx', sheet_name='тест', index=False)
    os.remove(src)