












if True:  # import, change os.cwd
    from bs4 import BeautifulSoup as BS
    from bs4 import Comment
    import requests, os, sys, re
    cwdpath = os.path.dirname(os.path.abspath(__file__))
    # print(os.getcwd())
    # print(repr(cwdpath))
    os.chdir(cwdpath)

if True:    # funcs
    def get_all_strings(tag, strip=False, types=(NavigableString, CData)):
        strings = []
        for desc in tag.descendants:
            if (      (  types is None and not isinstance(desc, NavigableString)  ) 
            or        (  types is not None and type(desc) not in types  )                    ): continue
            
            if strip:
                desc = desc.strip()
                if len(desc) == 0:
                    continue
            strings.append(desc)
        return strings    
    def rough_get_skill(skill, source):
        '''skill= "innate/q/w/e/r" '''
        top = source(class_='skill skill_{}'.format(skill))
        # print(len(top))
        assert len(top) == 1
        bot =  top[0].next_sibling(class_='va-collapsible-content mw-collapsible-content')
        assert len(bot) == 1
        return (top[0], bot[0])
    def f():
        if writethis:
            file = open('f.txt', 'w', encoding='utf-8')
            file.write(writethis)
            file.close()
            print('f fired')
    def del_tag_attrs(attr, code):
        first = code.contents[0]
        def foo(tag):
            try: del tag[attr]
            except TypeError: pass
            # except (TypeError, AttributeError): pass
        for elem in first.next_elements: 
            foo(elem)
        foo(first)
    def unwrap_tags(tagname, code):
        for tag in code(tagname): tag.unwrap()
    def decomp_tags(tagname, code):
        for tag in code(tagname): tag.decompose()

if True:  # make soup
    writethis = None
    champ = 'Aurelion_Sol'
    champ = 'Sion'
    response = requests.get('http://leagueoflegends.wikia.com/wiki/{}/Abilities'.format(champ))
    response.raise_for_status()
    # print(response.content == response.text.encode('utf8'))
    soup = BS(response.text, 'lxml')
    tag = soup('div', id='mw-content-text', class_='mw-content-ltr mw-content-text')[0]

# remove comments
for com in soup(text=lambda txt:isinstance(txt, Comment)): com.extract()                   

# decomp_tags('svg', soup)
unwrap_tags('img', soup) 
# unwrap_tags('i', soup)
# unwrap_tags('table', soup)
# unwrap_tags('td', soup)
# unwrap_tags('tr', soup)
# unwrap_tags('a', soup)
unwrap_tags('b', soup)
# unwrap_tags('p', soup)
# unwrap_tags('noscript', soup)

# unwrap_tags('span', soup)
# del_tag_attrs('href', soup)
# del_tag_attrs('style', soup)
# del_tag_attrs('title', soup)


# skill = rough_get_skill('innate', soup)
# testsoup = BS('<html>' + str(skill[0]) + str(skill[1]) + '<\html>', 'lxml')


# tag = soup('div', id='mw-content-text', class_='mw-content-ltr mw-content-text')[0]
# rough = bs4.BeautifulSoup(str(tag), 'lxml')

# unwrap_tags('div', skill[0])
# unwrap_tags('div', skill[1])

# writethis = tag.prettify()

# roughtxt = tag.get_text()
# roughtxt = re.sub(r'\n+', '\n', roughtxt)
# roughtxt = re.sub(r' +', ' ', roughtxt)
# roughtxt = re.sub(r'\n \n \n', '\n', roughtxt)
# roughtxt = re.sub(r'\n \n', '\n', roughtxt)


# writethis = roughtxt
# writethis = skill[0].prettify() + '\n' * 10 + skill[1].prettify()
# f()

# ['passive-progression tooltips-init-complete',       #    span                
#  'va-collapsible-content mw-collapsible-content',    #    div          
#  'skill skill_innate',                               #    div

# styles = ''
# for elem in testsoup.html.next_elements:
#     if hasattr(elem, 'has_attr'):
#         if elem.has_attr('style'):
#             styles += '\nstyle=\'{}\''.format(elem['style'])
# print(styles)

if True:  # Map-Specific Differences 
    # Garen
    # Thresh
    # Rengar
    # Ornn
    # Nasus
    # Shyvana
    # Taliyah
    # Bard

    pass

if True:  # Alt Collapsible
    # Irelia
    # Kha'Zix
    # Malphite
    # Jax
    # Janna
    # Lissandra
    # Leona
    # Pantheon
    # Xerath
    # Ziggs
    # Zed
    # Vi
    # Volibear
    # Vayne
    # Olaf
    # Shyvana
    # Skarner
    # Soraka
    # Syndra
    # Taliyah
    # Trundle
    # Tryndamere
    # Twitch
    # Udyr

    pass

if True:  # pets
    # Azir          multi tab
    # Zyra
    # Heimerdinger
    # Shaco
    # Mordekaiser 
    # Yorick

    # Wukong        one tab
    # Malzahar
    # Maokai
    # Zac
    # Annie
    # Ivern
    # Gangplank
    # Illaoi
    # Kalista
    # Jhin
    # LeBlanc
    # Elise

    pass

if True:  # other 
    # Yasuo     R collapse
    # Zoe       W collapse
    # Ryze      passive  collapse
    # Bard      passive  collapse
    # Rakan     text before passive
    # Xayah     text before passive
    # Kindred   text before passive

    pass

if True:  # alt skills
    # Sion
    # Riven
    # Corki
    # Kled
    # Rek'Sai
    # Quinn
    # Nidalee
    # Swain
    # Tahm Kench
    # Jayce
    # Lee Sin
    # Gnar

    pass




