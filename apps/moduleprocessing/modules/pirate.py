from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

from django.conf import settings
import os

class PirateDataCrawler:
    def __init__(self):
        # 크롬 드라이버 경로 설정
        chrome_driver_path = chrome_driver_path = os.path.join(settings.STATIC_ROOT, 'chromedriver')

        # 크롬 웹드라이버 옵션 설정
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 브라우저를 띄우지 않고 실행하는 headless 옵션 적용
        options.add_argument('--no-sandbox') # --no-sandbox 옵션 적용

        # 크롬 드라이버 생성
        self.__driver = webdriver.Chrome(chrome_driver_path, options=options)

        # 지역 데이터
        self.__country = {'Algeria': 'A001', 'Benin': 'A002', 'Congo': 'A003', 'Democratic Republic of Congo': 'A004', 'Egypt': 'A005', 'Ghana': 'A006', 'Guinea': 'A007', 'Gulf of Aden': 'D003', 'India': 'D002', 'Ivory Coast': 'A010', 'Kenya': 'A011', 'Mozambique': 'A012', 'Nigeria': 'A013', 'Red Sea': 'A014', 'Sierra Leone': 'A015', 'Somalia': 'A016', 'Tanzania': 'A017', 'The Congo': 'A018', 'Togo': 'A019', 'Gabon': 'A020', 'Liberia': 'A021', 'Cameroon': 'A022', 'Angola': 'A023', 'Brazil': 'B001', 'Colombia': 'B002', 'Costa Rica': 'B003', 'Ecuador': 'B004', 'Haiti': 'B005', 'Peru': 'B006', 'Dominican Republic': 'B007', 'Guyana': 'B008', 'Venezuela': 'B009', 'South China Sea': 'C001', 'Vietnam': 'C002', 'China': 'C003', 'Bangladesh': 'D001', 'Pakistan': 'D004', 'Indonesia': 'E001', 'Malacca Straits': 'E002', 'Malaysia': 'E003', 'Philippines': 'E004', 'Singapore Straits': 'E005', 'Thailand': 'E006', 'Iran': 'F001', 'Oman': 'F002', 'Papua New Guinea': 'F003', 'Yemen': 'F004'}

    def getPirateData(self,countryName):
        # 드라이버로 페이지 열기
        url = 'https://www.gicoms.go.kr/pirate/pirate_07.do'
        self.__driver.get(url)

        # "구역" select 태그 선택
        select_zone = Select(self.__driver.find_element(By.NAME,'srcActSeaArea'))
        # "구역" select 태그에서 "현재 해역" 선택

        if countryName in self.__country.keys():
            value = self.__country[countryName]

            select_zone.select_by_value(value)
            # "1주일" radio 버튼 선택
            buttons = self.__driver.find_elements(By.CSS_SELECTOR,'.inline_btn_group.recentlybtns > button')
            buttons[0].click() # 첫번째 버튼 클릭

            #"조회" 버튼 클릭
            self.__driver.find_element(By.CSS_SELECTOR,'.form_footer.search_confirm > button').click()

            # 데이터 로딩 대기
            self.__driver.implicitly_wait(5)

            # HTML 추출
            html = self.__driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # td 추출
            sea = [i.text for i in soup.find_all('td', class_='seawhere')]
            title = [tuple(i.text.split(' ')) for i in soup.find_all('td', class_='title')]

            data = [(s,t[0],t[1]) for s,t in zip(sea,title)]
            

            # 값 반환
            return data
            
        # 셀레니움 드라이버 종료
        # self.__driver.quit()