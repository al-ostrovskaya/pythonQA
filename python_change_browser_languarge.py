from selenium.webdriver.chrome.options import Options
link = "http://selenium1py.pythonanywhere.com/"
options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)


from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("intl.accept_languages", user_language)
driver_browser = webdriver.Firefox(options=options)