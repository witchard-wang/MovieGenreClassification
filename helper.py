from colorthief import ColorThief

#@Param in the image path and number of colors
#Return dominant color and array of colors rgb form
def getDomPalette(image_path, count):
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=count)
    return dominant_color, palette
