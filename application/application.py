from CiaShopServer.service.request import Request
from CiaShopServer.model.response import Response


def read_token_archive(archive, key):
    result = None
    with open(archive, 'r') as archive_read:
        for line in archive_read:
            line = line.replace('\n', '')
            line = line.split(':')

            if line[0] == key:
                result = line[1]

    return result


archive = "../key.token"
store_name = read_token_archive(archive, 'store_name')
token = read_token_archive(archive, 'token')

request = Request(token=token, store_name=store_name)
request_text = request.get_orders()

response = Response(request_text)
response.printr()