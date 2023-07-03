# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started

from pinterest.organic.pins import Pin
import pinterest
# Board information can be fetched from profile page or from create/list board method here:
# https://developers.pinterest.com/docs/api/v5/#operation/boards/list
link = pinterest.oauth2.authorization_url(app_id, redirect_uri)

# Initialize API by passing OAuth2 token
api = pinterest.Pinterest(token="ApFF9WBrjug_xhJPsETri2jp9pxgFVQfZNayykxFOjJQhWAw")
BOARD_ID="<Add your board id here>"
title="yo"
image = "https://www.lego.com/cdn/cs/set/assets/blta7b7b825b6d4fc0a/75313_Prod.png?format=webply&amp;fit=bounds&amp;quality=100&amp;width=320&amp;height=320&amp;dpr=1"
pin_create = Pin.create(
  board_id=BOARD_ID,
  title=title,
  description='Amazing lego for a great deal!',
  media_source={
      "source_type": "image_url",
      "content_type": "image/jpeg",
      "data": "string",
      'url':image,
      }
  )
print("Pin Id: %s, Pin Title:%s" %(pin_create.id, pin_create.title))
