sleeptime=1
keyboard.send_keys("/inline math")
time.sleep(sleeptime)

# Press Enter
keyboard.send_keys("<enter>")
time.sleep(sleeptime)

# Paste the previously cut content
keyboard.send_keys("<ctrl>+v")
time.sleep(sleeptime)

# Press Enter
keyboard.send_keys("<enter>")