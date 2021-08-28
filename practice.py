from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# ブラウザのインスタンス作成
browser = webdriver.Chrome(ChromeDriverManager().install())

url = "https://scraping-for-beginner.herokuapp.com/login_page"
browser.get(url)

# 名前入力欄のidを取得し，名前を入力
elem_username = browser.find_element_by_id("username")
elem_username.send_keys("imanishi")

# パスワード入力欄のidを取得し，パスワードを入力
elem_password = browser.find_element_by_id("password")
elem_password.send_keys("kohei")

# ログインボタンのidを取得し，ログインボタンをクリック
login_btn = browser.find_element_by_id("login-btn")
login_btn.click()

# tbodyの取得
elem_tbody = browser.find_element_by_tag_name("tbody")
# thの取得
elems_th = elem_tbody.find_elements_by_tag_name("th")

# 講師名というテキストを取得
elem_teacher = elems_th[0].text

# 出身地のidを取得
elem_td = browser.find_element_by_id("come_from")
# 出身地のテキストを取得
elem_native = elem_td.text

# ulタグのidを取得
elem_nav = browser.find_element_by_id("nav-mobile")
# ulタグ内にあるliを取得
elems_li = elem_nav.find_elements_by_tag_name("li")
# Udemyの属性を取得
elem_href = elems_li[3].find_element_by_tag_name("a").get_attribute("href")

# cssを用いたテキスト取得
elem_css_text = browser.find_element_by_css_selector("#name").text

# xpathを用いたテキスト取得
elem_xpath_text = browser.find_element_by_xpath("//*[@id='name']").text

# ランキングページにアクセス
browser.get("https://scraping-for-beginner.herokuapp.com/ranking/")
# htmlの高さを取得し，その半分の高さを求める
html_height = browser.execute_script("return document.body.scrollHeight")
half_html_height = int(html_height / 2)
# htmlの半分の高さまで移動
browser.execute_script(f"window.scrollTo(0,{half_html_height});")

browser.quit()

# -----------------------------------------------------------------------------
# ヘッドレスモードで実装
options = Options()
options.add_argument("--headless")

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://scraping-for-beginner.herokuapp.com/login_page"
browser.get(url)
elem_username_copy = browser.find_element_by_id("username")
elem_username_copy.send_keys("imanishi")
elem_password_copy = browser.find_element_by_id("password")
elem_password_copy.send_keys("kohei")
login_btn_copy = browser.find_element_by_id("login-btn")
login_btn_copy.click()
elem_tbody_copy = browser.find_element_by_tag_name("tbody")
elems_th_copy = browser.find_elements_by_tag_name("th")
elem_teacher_copy = elems_th_copy[0].text
print(elem_teacher_copy)
browser.quit()

# スクリーンショットを撮る
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://scraping-for-beginner.herokuapp.com/udemy"
browser.get(url)
browser.set_window_size(1600,1200)
browser.save_screenshot("screenshot.png")
