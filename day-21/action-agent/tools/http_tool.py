import requests

def http_call(url: str, method="GET", payload=None):
    r = requests.request(method, url, json=payload, timeout=10)
    return {
        "status": r.status_code,
        "data": r.json() if r.headers.get("content-type","").startswith("application/json") else r.text
    }