









:: https://ss64.com/nt/syntax-redirection.html
:: > for overwrite >> for appending
:: comment
:: %%G is the iterating variable
:: FOR /D   Conditionally perform a command on several Directories/Folders.
:: FOR /D [/r] %%parameter IN (folder_set) DO command

::@echo off
::cd "C:\Users\Tyler\LEAGUETOOLMAIN\champ analysis"
::cd "C:\Users\Tyler\LEAGUETOOLMAIN"
::FOR /D %%G IN (Zy*a) DO echo %%G > Zyra\%%G.py
::FOR /D %%G IN (*) DO xcopy Ahri %%G
::FOR /D %%G IN (*) DO
set text = %1
ReplaceText test.py %1 ass
pause














