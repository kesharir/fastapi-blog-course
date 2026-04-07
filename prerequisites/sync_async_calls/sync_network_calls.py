import time
import requests


def main():
    request_count=10
    url = "https://httpbin.org/get"
    session = requests.session()
    for i in range(request_count):
        print(f"Making Request {i}")
        resp = session.get(url)
        if resp.status_code == 200:
            pass

start = time.time()
main()
end = time.time()
print("Time Elapsed: ", end - start)

