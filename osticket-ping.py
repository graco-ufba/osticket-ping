#!/usr/bin/env python3

import os
import activesoup
import time

LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')
SLEEP_DURATION = 20

d = activesoup.Driver()
page = d.get("https://suporteic.ufba.br/scp/login.php")
form = page.form

print(1)
r = form.submit({'userid': LOGIN, 'passwd': PASSWORD})
print(2)
page = d.get("https://suporteic.ufba.br/scp/autocron.php")
print(3)
print(page._raw_response)

time.sleep(SLEEP_DURATION)