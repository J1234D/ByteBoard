import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeConfiguration
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.oled import OLED, OLED_DisplayMode
from kmk.extensions.RGB import RGB, AnimationModes

#temporary code(I will add new features after getting the components.)
keyboard = KMKKeyboard()

# Matrix
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4, board.D5)
keyboard.diode_orientation = DiodeConfiguration.COL2ROW

# Encoder (Rotation Only)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# A, B pins only (no push button)
encoder_handler.pins = (
    (board.D6, board.D7, None),
)

encoder_handler.map = [
    (
        (KC.VOLU, KC.VOLD),
        None,
    ),
]

# OLED
oled = OLED(
    scl=board.SCL,
    sda=board.SDA,
    width=128,
    height=64,
    flip=False,
    display_mode=OLED_DisplayMode.TXT,
)

keyboard.extensions.append(oled)

# Static Blue RGB
rgb = RGB(
    pixel_pin=board.D9,
    num_pixels=9,
    animation_mode=AnimationModes.STATIC,
)

keyboard.extensions.append(rgb)

# Set static blue
rgb.set_hsv_fill(170, 255, 120)

# Media Keys
keyboard.extensions.append(MediaKeys())

# Keymap
keyboard.keymap = [
    [
        KC.VOLU, KC.MUTE, KC.VOLD,
        KC.MPRV, KC.MPLY, KC.MNXT,
        KC.COPY, KC.PASTE, KC.CUT,
    ],
]

# OLED Startup Screen
def startup():
    oled.text("ByteBoard", 0, 0, 1)
    oled.text("Hackpad v1", 0, 16, 1)
    oled.text("Ready!", 0, 32, 1)
    oled.show()

startup()

keyboard.go()
