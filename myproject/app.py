from pymongo import MongoClient
from selenium import webdriver
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbcgs

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('home.html')

#입력한 기수에 맞는 게시글 DB 저장
@app.route('/api/insert', methods=['POST'])
def post_insert():
    classNum = request.form['classNum']

    driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32/chromedriver')
    driver.implicitly_wait(3)

    # 로그인 전용 화면
    driver.get('https://nid.naver.com/nidlogin.login')
    # 아이디와 비밀번호 입력
    driver.find_element_by_name('id').send_keys('sssw0126')
    driver.find_element_by_name('pw').send_keys('dbscpfls887571')
    # 로그인 버튼 클릭
    driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()

    base_url = 'https://cafe.naver.com/cgsclub'
    driver.get(base_url)
    title_list = driver.find_elements_by_css_selector('ul.cafe-menu-list > li > a.gm-tcol-c')
    title_urls = []

    # 입력한 기수에 맞는 게시글 저장
    for tl in title_list:
        title_name = tl.text.strip()
        if classNum == title_name[0:2] :
            url = tl.get_attribute('href')
            title_urls.append(url)

    print(title_urls)

    post_urls = []
    # 게시글 별 게시물 저장하기
    for tu in title_urls:
        driver.get(tu)
       # iframe으로 프레임 전환
        driver.switch_to.frame('cafe_main')
        #게시글 별 url 저장
        post_list = driver.find_elements_by_css_selector('div#main-area > div.article-board:nth-child(6)'
                                                         '> table > tbody > tr > td.td_article > div.board-list > div > a.article')
        for pl in post_list:
            url = pl.get_attribute('href')
            post_urls.append(url)


    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
