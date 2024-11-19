import requests
import time
from retrying import retry

# response = requests.get('https://www.google.com', timeout=2)
# print(response)

num = 1
@retry(stop_max_attempt_number=3,wait_random_min=1000,wait_random_max=2000)
def test():
    global num
    print(f"num = {num}")
    num += 1
    time.sleep(1)
    for i in 100: # 会报错，看看会不会重试
        print(i)

if __name__ == '__main__':
    # try:
    test()
    # except Exception as e:
    #     print(e)
    # else:
    #     print("ok")