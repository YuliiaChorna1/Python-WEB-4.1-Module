from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# do_GET do_POST do_PATCH do_DELETE

friends_list = []

class FriendsRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/friends":

            print(friends_list)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"hello world")

        else:

            self.send_response(404)

    def do_POST(self):

        if self.path == "/friends":
            
            content_len = int(self.headers.get("Content-Length"))

            post_body = self.rfile.read(content_len)
            print(post_body)
            friends_list.append(post_body)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"friend has been added")

    def do_DELETE(self):

        if self.path == "/friends":
            
            print(friends_list)
            friends_list.pop()
            print(friends_list)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"friend has been deleted")

# json.dump(response, wfile)

server = HTTPServer(("localhost", 8001), FriendsRequestHandler)
server.serve_forever()
