from bs4 import BeautifulSoup
import requests
import time


def get_doc():

	BASE_URL 	= "https://gall.dcinside.com/mgallery/board/view/"
	url 		= 'https://gall.dcinside.com/mgallery/board/lists?id=vr_games_xuq'
	# 파라미터 설정
	params = {'id' : 'vr_games_xuq'}

	# 헤더 설정
	headers = {
		'Accept' 			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'Accept-Encoding'	: 'gzip, deflate, br',
		'Connection'		: 'keep-alive',
		'User-Agent' 		: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
	}
	resp = requests.get(url, params=params, headers=headers)
	print(resp)
	#print(resp.content)
	try:
		soup 		= BeautifulSoup(resp.content, 'html.parser')
		contents 	= soup.find('tbody').find_all('tr')
		#print(contents)
	except:
		print('Fail')
		return 0


	doc = []

	# 한 페이지에 있는 모든 게시물을 긁어오는 코드 
	for i in contents:
		print('-'*15)
		
		# 제목 추출
		title_tag = i.find('a')
		title = title_tag.text
		print("제목: ", title)
		
		# 글쓴이 추출
		writer_tag = i.find('td', class_='gall_writer ub-writer').find('span', class_='nickname')
		if writer_tag is not None: # None 값이 있으므로 조건문을 통해 회피 
			writer = writer_tag.text
			print("글쓴이: ", writer)
			
		else:
			print("글쓴이: ", "없음")
			writer = '없음'
		
		# 유동이나 고닉이 아닌 글쓴이 옆에 있는 ip 추출
		ip_tag = i.find('td', class_='gall_writer ub-writer').find('span', class_='ip')
		if ip_tag is not None:  # None 값이 있으므로 조건문을 통해 회피 
			ip = ip_tag.text
			print("ip: ", ip)
		else: 
			ip = None
		
		# 날짜 추출 
		date_tag = i.find('td', class_='gall_date')
		date_dict = date_tag.attrs
		if len(date_dict) is 2:
			print("날짜: ", date_dict['title'])
			date = date_dict['title']
		
		else:
			print("날짜: ", date_tag.text)
			date = date_tag.text
			pass
		
		# 조회 수 추출
		views_tag = i.find('td', class_='gall_count')
		views = views_tag.text
		print("조회수: ", views)
		
		# 추천 수 추출
		recommend_tag = i.find('td', class_='gall_recommend')
		recommend = recommend_tag.text
		print("추천수: ", recommend)

		article = {'title': title, 'writer':writer, 'ip':ip, 'date':date, 'views':views, 'recommend':recommend}
		doc.append(article)




	for article in doc:
		if article['writer'] == '와사비':
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


while(True):
	
	get_doc()
	time.sleep(6)
