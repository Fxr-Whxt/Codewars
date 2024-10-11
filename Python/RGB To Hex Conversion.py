'''The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
Examples (input --> output):

255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

'''


def color(RGB):
    if RGB > 255:
        RGB = 255
    elif RGB < 0:
        RGB = 0
    RGB = hex(RGB)[2:].upper()
    if len(RGB)<2:
        RGB = '0'+RGB
    return RGB    


def rgb(r, g, b):
    return color(r)+color(g)+color(b)