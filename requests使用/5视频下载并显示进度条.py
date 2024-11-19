import requests

url = (
    'https://v9-re1.douyinvod.com/bb034681df25897a0b9f4103b07db957/673c03e1/video/tos/cn/tos-cn-ve-15c000-ce/owA1P7'
    'ZBi88EToAY0QDQsBhIdkNPYzidXMERr/?a=1128&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=2285&bt=2285&cs=0&ds=4&ft='
    'Qimo7J8rffPdHK~2N12NvAq-antLjrKviq_NRkadVWAxejVhWL6&mime_type=video_mp4&qs=0&rc=NGY5ZGlkPDVoOGRkNzg0NEBpajZmOXY5'
    'cjtqdjMzbGkzNEBgYDVhYS8tXl4xYDA0LjFeYSNiLy9yMmQ0b3FgLS1kLWJzcw%3D%3D&btag=80000e000a8000&cquery=100y&dy_q=1731982'
    '614&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=202411191016540D1792AAA62B524F53A2')
response = requests.get(url, stream=True)
video_length= int(response.headers.get('content-length'))

with open("1.mp4", "wb") as f:
    download_length = 0
    for chunk in response.iter_content(1000):
        if chunk:
            f.write(chunk)
            download_length += 1000
            print(f"下载进度：{(download_length / video_length) * 100}%")

