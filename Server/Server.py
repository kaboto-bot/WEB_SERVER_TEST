# かなり原始的な実装(Socketを使ってHTTP接続を待ち受ける)
# Python 3.11.3

import socket

# from util.status_code import HttpStatus, STATUS_CODES
MAX_REQUESTLINE_STRNUM = 65537


def CreateResponse(status_code):
    if status_code == 200:
        return "200 OK"
    else:
        return "ERROR"

def handle_request(pClientSocket):
    """クライアントからのリクエストを処理する"""
    # TODO 文字コードの解釈 まぁとりあえずutf-8で
    request = pClientSocket.recv(1024).decode('utf-8')
    # リクエストラインだけとる
    headers = request.split('\n')
    http_method, resource_path, http_version = headers[0].split()
    print(f"Received {http_method} METHOD, request_path for {resource_path}, http_version={http_version}")

    # メソッドの解釈
    if http_method == 'GET':
        response_header = http_version + " " + CreateResponse(200)
        response_body = 'Hello World'
        response = response_header + '\n\n' + response_body
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\nOnly GET is supported.'

    print(response)
    pClientSocket.sendall(response.encode('utf-8'))
    pClientSocket.close()


def main():
    """サーバーを起動し、接続を待ち受ける"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    
    print("Listening on port 8000...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        handle_request(client_socket)

if __name__ == '__main__':
    main()
    
# TEST_COMMAND
# curl -X GET http://localhost:8000