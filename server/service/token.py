class Token(object):

    def __init__(self):
        self.store_name = self.read_token_archive('store_name')
        self.token = self.read_token_archive('token')

    @staticmethod
    def read_token_archive(key):
        result = None
        token = "key.token"
        with open(token, 'r') as token_read:
            for line in token_read:
                line = line.replace('\n', '')
                line = line.split(':')

                if line[0] == key:
                    result = line[1]

        return result
