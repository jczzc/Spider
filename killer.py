import os
os.system("""TASKKILL /T /IM "checkrs.exe" /IM "rscheck.exe" /IM "REDAgent.exe" /F""")
while True:pass
