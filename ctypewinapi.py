import ctypes
from ctypes.wintypes import HWND

user32 = ctypes.windll.user32
dwmapi = ctypes.windll.dwmapi

WM_NCHITTEST = 0x84
HTCAPTION = 0x02


def enable_window_shadow(window):
    hwnd = int(window.winId())
    margins = ctypes.c_int * 4
    dwmapi.DwmExtendFrameIntoClientArea(HWND(hwnd), ctypes.byref(margins(-1, -1, -1, -1)))

    DWMWA_NCRENDERING_POLICY = 2
    DWMNCRP_ENABLED = 2
    dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_NCRENDERING_POLICY, ctypes.byref(ctypes.c_int(DWMNCRP_ENABLED)), ctypes.sizeof(ctypes.c_int))