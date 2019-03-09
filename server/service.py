import time
import random
from pathlib import Path
from server.win_service import WinService


class Service(WinService):
    _svc_name_ = 'CiaShopServer'
    _svc_display_name_ = 'CiaShop Consumer Api'
    _svc_description_ = 'Service to communicate with the API provided by the CiaShop platform to integrate ERP.'

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            Path(f'c:\\test\\{x}.txt').touch()
            time.sleep(5)


if __name__ == '__main__':
    Service.parse_command_line()
