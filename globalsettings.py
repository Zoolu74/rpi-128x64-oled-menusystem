########
#globals
# debug messages
DEBUGFLAG = 1
# Raspberry Pi pin configuration:
RST = None

#screen configuration
# height of each text line in pixels
TEXT_LINE_X = 10
TEXT_Y_OFFSET = 5
# this oled has two sections, 16 pixel yellow bar at the top and then the remaining 48 pixels are blue
# this var marks the start of the main section of the screen and anything to be displayed in it should be offset by it
MAIN_X = 16
MAX_ITEM_PERSCREEN = 4
SECOND_SCREEN = False
# font settings
# font name and location
FONT_NAME = "./fonts/DejaVuSerif.ttf"
# font size
FONT_SIZE = 10

# screen saver setting
SCREEN_SAVER_TYPE = 0	# 0 = image, 1 = shapes drawing
SCREEN_SAVER_TIMEOUT = 25

# Time to wait between button presses
BUTTON_SLEEP_TIME = 0.5

# Location of menu files
# MENU_FOLDER = "./menus"
MENU_FOLDER = "./example-menus/"
# var to track selected menu 
selectedMenu = 0
############


