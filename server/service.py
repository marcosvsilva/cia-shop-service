import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil
from _config import Config
from _application import Application

# Command line pyinstaller create servicemanager
# pyinstaller -F --hidden-import=win32timezone service.py

class CSAPIServer(win32serviceutil.ServiceFramework):
    _svc_name_ = "CSAPIServer"
    _svc_display_name_ = "Jave API CiaShop Synchronization"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        rc = None
        config = Config()
        application = Application()
        while rc != win32event.WAIT_OBJECT_0:
            time_to_sleep = int(config.get_key('sleep_timer_synchronize')) * 1000
            application.synchronize()

            rc = win32event.WaitForSingleObject(self.hWaitStop, time_to_sleep)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(CSAPIServer)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(CSAPIServer)
