import webbrowser
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler


def open_browser():
  webbrowser.open(f'http://localhost:{PORT}/src/', new=0, autoraise=True)
  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      exit(0)
