import requests
import random
from configuration import _USE_PROXY_, _PROXY_FILE_


def test_proxy(proxy):
	url = "http://ifconfig.me"
	try:
		res = requests.get(url, proxies={"http": "socks5://{}".format(proxy)})
		# print(res.text)
		return res.text in proxy
	except Exception as e:
		raise e
		return False

def proxy_chain():
	if(_USE_PROXY_):
		with open(_PROXY_FILE_) as f:
			proxies = f.read().strip().split("\n")
		p = proxies[random.randint(0, len(proxies)-1)]
		print("[+] OK! {}".format(p))
		if(test_proxy(p) == False):
			return []
		return p
	else:
		return []


if __name__ == '__main__':
	while(1):
		print(proxy_chain())