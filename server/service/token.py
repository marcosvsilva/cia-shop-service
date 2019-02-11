class Token(object):

    def __init__(self):
        self.archive = "../key.token"
        self.store_name = self.read_token_archive('store_name')
        self.token = self.read_token_archive('token')

    def read_token_archive(self, key):
        result = None
        with open(self.archive, 'r') as archive_read:
            for line in archive_read:
                line = line.replace('\n', '')
                line = line.split(':')

                if line[0] == key:
                    result = line[1]

        return result

    def get_store_name(self):
        return self.store_name

    def get_token(self):
        return self.token