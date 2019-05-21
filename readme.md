browserup-proxy-py
===================

Python client for the BrowserUp Proxy REST API.


How to install
----------------------------------

1. `pip install git+https://github.com/browserup/browserup-proxy-py.git@master#egg=browserup-proxy==0.1.0`
2. Use [bootstrap.sh](https://github.com/browserup/browserup-proxy-py/blob/master/bootstrap.sh) to download `browserup-proxy`, `selenium-server`, `chromedriver` and `geckodriver` (Firefox)
3. Add `tools/chromedriver` and `tools/geckodriver` to OS `PATH`. Example:
   ```
   cd /usr/local/bin
   ln -s ~/projects/browserup-proxy-py/tools/geckodriver geckodriver
   ln -s ~/projects/browserup-proxy-py/tools/chromedriver chromedriver
   ```

How to use with selenium-webdriver
----------------------------------

``` bash
pip install selenium
```

Manually:

``` python 
from browserupproxy import Server
from selenium import webdriver

server = Server("tools/browserup-proxy-1.1.0/bin/browserup-proxy")
server.start()
proxy = server.create_proxy()

profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)

proxy.new_har("google")
driver.get("http://www.google.co.uk")
proxy.har # returns a HAR JSON blob

server.stop()
driver.quit()

```

for Chrome use

```
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
browser = webdriver.Chrome(chrome_options = chrome_options)
```

Running Tests
-------------

```bash
git clone git@github.com:browserup/browserup-proxy-py.git
cd browserup-proxy-py
pyenv virtualenv 3.6.7 browserup-proxy-venv
pyenv activate browserup-proxy-venv
pip install -r requirements/base.txt
pip install -r requirements/dev.txt
./bootstrap.sh
```

Start a browserup instance:

```bash
./start-server.sh
```

In a separate window:

```bash
py.test
```

If you are going to watch the test, the 'human' ones should display an english
muffin instead of the american flag on the 'pick your version' page. Or at
least it does from Canada.

To run the tests in a CI environment, disable the ones that require human
judgement by adding "-m "not human" test" to the py.test command.

```bash
py.test -m "not human" test
```
