from storage import disable_usb_drive
from usb_cdc import disable

HIDE_DEVICE = True

if HIDE_DEVICE:
    disable_usb_drive()
    disable()
