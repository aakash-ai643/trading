from selenium import webdriver

API_URL = "http://newprojectserver.com:8500/market?symbol=BTC/USDT"  # 🔥 Updated API URL

def test_api_with_browser():
    driver = webdriver.Chrome()
    driver.get(API_URL)
    print(driver.page_source)
    driver.quit()

if __name__ == "__main__":
    test_api_with_browser()
