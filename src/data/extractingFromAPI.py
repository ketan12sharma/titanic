import requests
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML
# url = 'https://api.data.gov/ed/collegescorecard/v1/schools?school.name=boston%20college&api_key=3N4CW1MSGxFpnZRKwUUOSVGdMiRb6bEXEINhOsXk'
#
# result = requests.get(url)
#
# print(result.status_code)
# print(result.json())
# print(result.text)
#
html_String = """
<!DOCTYPE html>
<html>
<body>

<h2>The select Element</h2>
<p>The select element defines a drop-down list:</p>

<form action="/action_page.php">
  <select name="cars">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
    <option value="fiat">Fiat</option>
    <option value="audi">Audi</option>
  </select>
  <br><br>
  <input type="submit">
</form>

</body>
</html>

"""

ps = BeautifulSoup(html_String)
# print(ps)

# display(HTML(html_String))

body = ps.find(name='body')
# print(body)
print(body.find(name='h2').text)
