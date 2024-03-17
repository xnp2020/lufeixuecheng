from selenium import webdriver

# 初始化一个浏览器对象
driver = webdriver.Chrome()

# 打开页面
driver.get("http://192.168.72.65/wcd/system_counter.xml")

# 执行JavaScript
driver.execute_script("location.replace('/wcd/index.html?access=SYS_COU');")

# 获取页面源代码
page_source = driver.page_source
print(page_source)

# 关闭浏览器
driver.quit()
