import requests

topic = 'dsi_c2_brs'
title = 'Hello, world!'
message = 'Hello, world from Simeon!'

# send a message through ntfy.sh
requests.post(
    'https://ntfy.sh/' + topic,
    data=message.encode('utf-8'),
    headers={'Title': title}
)
