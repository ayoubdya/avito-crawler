import webbrowser
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler


def open_browser():
  webbrowser.open(f'http://localhost:{PORT}/src/', new=0, autoraise=True)
  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
      print("serving at port", PORT)
      httpd.serve_forever()
    except KeyboardInterrupt:
      httpd.server_close()
      exit(0)
