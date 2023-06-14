'''import http.server
python -m http.server'''  ''' generate error since this is not correct format'''

'''from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.serve_forever()

*payload 1 check status run sucess but more time require
'''
import webbrowser

payload = "<script>alert('XSS!');</script>"
url = "https://www.webpagetest.org/" + payload

webbrowser.open(url)




