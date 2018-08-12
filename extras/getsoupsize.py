








if True:  # import, change os.cwd
    from bs4 import BeautifulSoup as BS
    from bs4 import Comment
    import requests, os, sys, time, re
    cwdpath = os.path.dirname(os.path.abspath(__file__))
    # print(os.getcwd())
    # print(repr(cwdpath))
    os.chdir(cwdpath)

with open('champs.txt') as champfile:
    champs = champfile.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
champs = [x.strip() for x in champs]

sizes = {}
# testchamps = ['Zoe', 'Zac', 'Ashe', 'Bard', 'Braum']

if True:  # make soup
    for champ in champs:
        response = requests.get('http://leagueoflegends.wikia.com/wiki/{}/Abilities'.format(champ))
        response.raise_for_status()
        soup = BS(response.text, 'lxml')
        tag = soup('div', id='mw-content-text', class_='mw-content-ltr mw-content-text')[0]

        str_txt = tag.get_text()
        str_txt = re.sub(r'\n+', '\n', str_txt)
        str_txt = re.sub(r' +', ' ', str_txt)
        str_txt = re.sub(r'\n \n \n', '\n', str_txt)
        str_txt = re.sub(r'\n \n', '\n', str_txt)


        sizes[len(str_txt)] = champ
        print('{} done'.format(champ))
        time.sleep(1)
        pass

sorted_nums = sorted(sizes.keys())
result = [str((num, sizes[num])) for num in sorted_nums]

with open('txtonlysize.txt', 'a') as resultfile:
    for x in result:
        resultfile.write(x + '\n')
