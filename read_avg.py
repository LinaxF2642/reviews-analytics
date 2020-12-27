# Q1 這一百萬筆資料平均的長度

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0:
			print(len(data))
print('ˇ檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('平均是', sum_len/len(data))
