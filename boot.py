from storage import disable_usb_drive
from usb_cdc import disable

HIDE_DEVICE = False

if HIDE_DEVICE:
    disable_usb_drive()
    disable()
