from server.win_service import WinService
from server.application import Application


class Service(WinService):
    _svc_name_ = 'CiaShopServer'
    _svc_display_name_ = 'CiaShop Consumer Api'
    _svc_description_ = 'Service to communicate with the API provided by the CiaShop platform to integrate ERP.'

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        application = Application()
        while self.isrunning:
            application.syncronize()


if __name__ == '__main__':
    Service.parse_command_line()
