from urllib.parse import urlparse,parse_qs
url="https://example.com/employees?name=Anand&salary=25000"
parsed_url=urlparse(url)
dct=parse_qs(parsed_url.query)
print("Query parameters:",dct)