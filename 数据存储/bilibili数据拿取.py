import requests
import csv

class Bilibili(object):
    def __init__(self):
        self.url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?category_id=&search_type=video&ad_resource=5654&__refresh__=true&_extra=&context=&page=2&page_size=42&pubtime_begin_s=0&pubtime_end_s=0&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E7%BE%8E%E5%A5%B3&qv_id=RQbivkhQdwc6Pf7CJIXqolzlpKgj4Muq&source_tag=3&gaia_vtoken=&dynamic_offset=36&web_location=1430654&w_rid=2b2af3c9b03865e836dab3ba6945768a&wts=1732118575'

        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'Cookie': "i-wanna-go-back=-1; buvid4=A95643F0-AF4A-FE12-6F8C-1267EDE052A024776-022081509-HOmfFsh%2Fns0qWvxGgSEhdg%3D%3D; DedeUserID=1920683741; DedeUserID__ckMd5=d229b1301b78b06d; buvid3=1DB77409-5BD4-02BD-8C26-38AE9665BA5D21328infoc; b_nut=1700919521; b_ut=5; enable_web_push=DISABLE; header_theme_version=CLOSE; rpdid=|(umkm|ku)|J0J'u~|RlRm~)u; PVID=1; home_feed_column=5; is-2022-channel=1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; fingerprint=c0ddf6a269c15270cb37afea5ccb9b43; buvid_fp_plain=undefined; buvid_fp=219910beb15bd62f4835589014ea3de7; _uuid=4A471862-5FDB-645D-D1EE-BA75AA10E485D69772infoc; browser_resolution=1920-1065; SESSDATA=d1510213%2C1747669847%2C26b46%2Ab1CjCr7mXQBKJpJ1A6LdmwXimJm4w5gxE2daEYi7pmVLTYP8qK9KpZN8C6G9M7fzR764ESVjZ0c2p0SGdqM3VhcjhtT1M2c3FGZ2xDRW9SRjE4MTNDQ1lLTjBTeHg2MVNaeUU3WjUteGFTYWlEQ3pHdS1DcEl1UHB1VnRvcG83dm5aRUVkUXVaYVJ3IIEC; bili_jct=f77062406d3e53c035da97e45d68036d; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzIzNzcwNjgsImlhdCI6MTczMjExNzgwOCwicGx0IjotMX0.Ddnm17hUBd_z60WxRqubxvPhMpoWTr4GnfZQQ-17bY4; bili_ticket_expires=1732377008; CURRENT_QUALITY=0;"
        }

        self.response = requests.get(self.url, headers=self.headers).json()
        for item in self.response["data"]["result"]:
            print(item["author"])
            print("arcurl")
            print("tag")

    def save_list(self):
        with open("bilibili.csv", "w", encoding='utf-8') as csvfile:
            field_names = ["author","arcurl","tag"]
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for item in self.response["data"]["result"]:
                csv_list = list()
                csv_list.append(item["author"])
                csv_list.append(item["arcurl"])
                csv_list.append(item["tag"])
                writer.writerow(csv_list)

    def save_dict(self):
        with open("bilibili_dict.csv", "w", encoding='utf-8') as csvfile:
            field_names = ["author","arcurl","tag"]
            # 按行写入的是一个字典，也可以把字典写成一个列表，用writerows()
            csv_writer = csv.DictWriter(csvfile,fieldnames=field_names)
            csv_writer.writeheader()
            dicts = []
            for item in self.response["data"]["result"]:
                csv_dict = dict()
                csv_dict["author"] = item["author"]
                csv_dict["arcurl"] = item["arcurl"]
                csv_dict["tag"] = item["tag"]
                dicts.append(csv_dict)
            csv_writer.writerows(dicts)




if __name__ == '__main__':
    bilibili = Bilibili()
    bilibili.save_dict()
