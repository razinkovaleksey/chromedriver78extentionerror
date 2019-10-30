import importlib

from selenium.webdriver.chrome.options import Options

wd = importlib.import_module('selenium.webdriver')
chrome = getattr(wd, 'Chrome')

chrome_options = Options()
chrome_options.add_extension('plugin.crx')

driver = chrome(options=chrome_options, service_args=["--verbose", "--log-path=qc1.log"])
