- `response.text` 响应体`str`类型
- `respones.content` 响应体`bytes`类型
- `response.status_code` 响应状态码
- `response.request.headers` 响应对应的请求头
- `response.headers` 响应头
- `response.request.headers.get('cookies')` 响应对应请求的`cookie`
- `response.cookies` 响应的`cookie`（经过了`set-cookie`动作）
- `response.url`请求的`URL`
-  `response.history` 历史请求信息,为一个列表

字节流下载

```py
response= requests.get(url,strwam=True)# 设置未True,在调用itre_content()的时候才会请求接口
with open("1.png","wb") as f:
	for chunk in iter_content(chunk_size = 100):
		if chunk:
			f.write(chunk)
```

获取响应头中cookie的两种方式

```python
dict(response.cookie)
requests.utils.dict_from_cookiejar(response.cookies
```

禁止URL自动重定向

```
allow_redirects=False
```

忽略证书错误

```
verify=False
```
