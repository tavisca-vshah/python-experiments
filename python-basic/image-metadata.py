from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import PIL.ExifTags
import json

# path to the image or video
imagename = "/content/image.jpg"

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exifdata = image.getexif()
gpsInfo = None
# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    if tag == "GPSInfo":
      gpsInfo = data

gpsinfo = {}
for key in gpsInfo.keys():
  decode = GPSTAGS.get(key,key)
  gpsinfo[decode] = gpsInfo[key]

print(json.dump(gpsinfo))