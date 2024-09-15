
from utils.ColorText import colorText

VERSION = "1.10"

changelog = colorText.BOLD + '[ChangeLog]\n' + colorText.END + colorText.BLUE + '''
[1.00 - Beta]
1. Initial Release for beta testing
2. Minor Bug fixes

[1.01]
1. Inside Bar detection added.
2. OTA Software Update Implemented.
3. Stock shuffling added while screening
4. Results will be now also stored in the excel (screenipy-result.xlsx) file.
5. UI cosmetic updates for pretty-printing!

[1.02]
1. Feature added to screen only STAGE-2 stocks.
2. OTA update download bug-fixed.
3. Auto generate default config if not found.
4. Minor bug-fixes.

[1.03]
1. Result excel file will not be overwritten now. Each result file will be saved with timestamp.
2. Candlestick pattern recognition added.

[1.04]
1. OTA Software Update bug-fixed.
2. Minor Improvements.

[1.05]
1. More candlestick pattern added for recognition.
2. Option added to find stock with lowest volume in last 'N'-days to early detect possibility of breakout.
3. Last screened results will be stored and can be viewed with Option > 7.
4. Minor Bug-fixes and improvements.

[1.06]
1. Option > 0 added - Screen stocks by enterning it's name (stock code).
2. Stability fixes and improvements.
3. Last screened results will be stored and can be viewed with Option > 7.

[1.07]
1. Program Window will not automatically close now.
2. Bug fixes and improvements.

[1.08]
1. Prompt added for saving excel after screening.
2. Program back-end architecture updated.

[1.09]
1. RSI based screening added as Option > 5.
2. Minor Performance Improvements.

[1.10]
1. Trend detection for the timeframe of analysis added.
''' + colorText.END