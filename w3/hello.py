# 입력값
a = ['사과', '감', '감', '배', '포도', '포도', '딸기', '포도', '감', '수박', '딸기']


# 채워야하는 함수
def count_list(a_list):
	result = {}
	for fruit in a_list:
		if (fruit in result):
			result[fruit] += 1
		else:
			result[fruit] = 1
	return result

# 결과값
print(count_list(a))

