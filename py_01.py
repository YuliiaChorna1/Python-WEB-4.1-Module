# У цьому прикладі ми створили дуже простий HTTP сервер, 
# який приймає запити за адресою / та на GET-запит відповідає рядком 'Hello, world!',
# а на POST-запит нічого не робить.

# Клієнт створюємо за допомогою класу HTTPConnection та вказуємо хост (адресу) та порт сервера.
# Клієнт робить GET-запит на http://localhost:8001/, викликаючи метод getresponse, 
# та виводить у консоль тіло відповіді. Щоб перевірити, що відповідь містить тіло, 
# ми можемо перевірити статус-код відповіді (res.status) та причину помилки (res.reason),
# якщо така була.

# Щоб запустити сервер в роботу і не блокувати застосунок, запустимо його в окремому потоці.

# З неочевидного: ми вказали порт, на якому наш сервер очікує на з'єднання як 8001. 
# Якщо порт не вказати, то за замовчуванням буде використаний порт 80, 
# що потребує привілеїв адміністратора.

from threading import Thread
from http import client
from time import sleep
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello world!")

    def do_POST(self):

        pass


httpd = HTTPServer(("localhost", 8001), SimpleHTTPRequestHandler)
server = Thread(target=httpd.serve_forever)
server.start()
sleep(0.5) # sleep(15)

h1 = client.HTTPConnection("localhost", 8001)
h1.request("GET", "/")

res = h1.getresponse()
print(res.status, res.reason)

data = res.read()
print(data)


httpd.shutdown()
