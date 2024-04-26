@echo off

set dc_bot_token=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
set dc_channel_id=1111111111111111111

set msg=Hi Test

.\dist\main.exe %dc_bot_token% %dc_channel_id% "%msg%"

timeout 5