from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import jsonpickle
import json

def get_every_draft_from_league_bo1(html_page):
    datas_x = []
    datas_y = []
    soup = bs(html_page, 'html.parser')
    for tbody_tag in soup.find_all('tbody'):
        for a_tag in tbody_tag.find_all('a'):
            url_match = a_tag['href']
            req = Request(url=str('https://gol.gg/'+url_match[2:]),headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            pick_blue_side,pick_red_side,last_champ_blue,last_champ_red = extract_champion_names(webpage)
            datas_x.append(pick_blue_side)
            datas_x.append(pick_red_side)
            datas_y.append(last_champ_blue)
            datas_y.append(last_champ_red)
    return datas_x , datas_y
def get_every_draft_from_league_bo3(html_page):
    global verif_trois_game_dans_le_bo3_var
    datas_x = []
    datas_y = []
    soup = bs(html_page, 'html.parser')
    for tbody_tag in soup.find_all('tbody'):
        for a_tag in tbody_tag.find_all('a'):
            url_match = a_tag['href']
            req = Request(url=str('https://gol.gg/'+url_match[2:]),headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            champ_names = extract_champion_names_bo3(webpage)
            num_values = len(champ_names)

            if num_values == 8:
                var_names = ["pick_blue_side_game_1", "pick_red_side_game_1", "pick_blue_side_game_2", "pick_red_side_game_2"]
            elif num_values == 12:
                var_names = ["pick_blue_side_game_1", "pick_red_side_game_1", "pick_blue_side_game_2", "pick_red_side_game_2", "pick_blue_side_game_3", "pick_red_side_game_3"]
            else:
                raise ValueError("Invalid number of champion names returned by extract_champion_names_bo3")
            datas_x.extend([champ_names[0],champ_names[1],champ_names[2],champ_names[3]])
            datas_y.extend([champ_names[4],champ_names[5],champ_names[6],champ_names[7]])
            # for i in range(num_values):
            #     var_name = var_names[i//2] + str((i%2) + 1)
            #     globals()[var_name] = champ_names[i]
            #     datas_x.append(champ_names[i])
            #     if i % 2 == 0:
            #         last_champ_blue = champ_names[i]
            #     else:
            #         last_champ_red = champ_names[i]
            #     if i == num_values - 1:
            #         datas_y.extend([last_champ_blue, last_champ_red])

            # print(verif_trois_game_dans_le_bo3_var)
            # if verif_trois_game_dans_le_bo3:
            #     pick_blue_side_game_1, pick_red_side_game_1,pick_blue_side_game_2 , pick_red_side_game_2, pick_blue_side_game_3, pick_red_side_game_3,last_champ_blue_game_1,last_champ_blue_game_2,last_champ_blue_game_3,last_champ_red_game_1,last_champ_red_game_2,last_champ_red_game_3 = extract_champion_names_bo3(webpage)
            #     datas_x.extend([pick_blue_side_game_1, pick_red_side_game_1,pick_blue_side_game_2 , pick_red_side_game_2, pick_blue_side_game_3, pick_red_side_game_3])
            #     datas_y.extend([last_champ_blue_game_1,last_champ_blue_game_2,last_champ_blue_game_3,last_champ_red_game_1,last_champ_red_game_2,last_champ_red_game_3])
            # else :
            #     pick_blue_side_game_1, pick_red_side_game_1,pick_blue_side_game_2 , pick_red_side_game_2,last_champ_blue_game_1,last_champ_blue_game_2,last_champ_red_game_1,last_champ_red_game_2= extract_champion_names_bo3(webpage)
            #     datas_x.extend([pick_blue_side_game_1, pick_red_side_game_1,pick_blue_side_game_2 , pick_red_side_game_2])
            #     datas_y.extend([last_champ_blue_game_1,last_champ_blue_game_2,last_champ_red_game_1,last_champ_red_game_2])

    return datas_x , datas_y
def extract_champion_names_bo1(html_code):
    soup = bs(html_code, 'html.parser')
    ban_blue_side = []
    ban_red_side = []
    pick_blue_side = []
    pick_red_side = []
    draft = [ban_blue_side,pick_blue_side,ban_red_side,pick_red_side]
    compteur = 0
    compteur_draft = -1
    for img_tag in soup.find_all('img', {'class': 'champion_icon_medium'}):
        if compteur % 5 == 0:
            compteur_draft += 1
        champ_name = img_tag['alt']
        draft[compteur_draft].append(champion_into_number(champ_name))
        compteur += 1
    last_champ_blue=draft[1].pop(-1)
    last_champ_red = draft[3].pop(-1)
    return pick_blue_side,pick_red_side,last_champ_blue,last_champ_red
def verif_trois_game_dans_le_bo3_function(draft):
    global verif_trois_game_dans_le_bo3_var
    if not(draft[11]== []):
        verif_trois_game_dans_le_bo3_var = True
    else:
        verif_trois_game_dans_le_bo3_var=False

def extract_champion_names_bo3(html_code):
    soup = bs(html_code, 'html.parser')
    ban_blue_side_game_1, ban_red_side_game_1 , pick_blue_side_game_1, pick_red_side_game_1, ban_blue_side_game_2, ban_red_side_game_2, pick_blue_side_game_2 , pick_red_side_game_2, ban_blue_side_game_3, ban_red_side_game_3, pick_blue_side_game_3, pick_red_side_game_3 = [],[],[],[],[],[],[],[],[],[],[],[]
    draft = [ban_blue_side_game_1, pick_blue_side_game_1  , ban_red_side_game_1, pick_red_side_game_1, ban_blue_side_game_2,  pick_blue_side_game_2 ,  ban_red_side_game_2, pick_red_side_game_2, ban_blue_side_game_3,  pick_blue_side_game_3 ,ban_red_side_game_3 , pick_red_side_game_3]
    compteur = 0
    compteur_draft = -1

    for img_tag in soup.find_all('img', {'class': 'champion_icon_medium'}):
        if compteur % 5 == 0:
            compteur_draft += 1
        champ_name_link = img_tag['src']
        champ_name = champ_name_link[23:-4]
        draft[compteur_draft].append(champion_into_number(champ_name))
        compteur += 1

    last_champ_blue_game_1 = draft[1].pop(-1)
    last_champ_blue_game_2 = draft[5].pop(-1)
    last_champ_red_game_1 = draft[3].pop(-1)
    last_champ_red_game_2 = draft[7].pop(-1)

    if verif_trois_game_dans_le_bo3_function(draft):
        last_champ_red_game_3 = draft[11].pop(-1)
        last_champ_blue_game_3 = draft[9].pop(-1)
        return pick_blue_side_game_1, pick_red_side_game_1,pick_blue_side_game_2 , pick_red_side_game_2, pick_blue_side_game_3, pick_red_side_game_3,last_champ_blue_game_1,last_champ_red_game_1,last_champ_blue_game_2,last_champ_red_game_2,last_champ_blue_game_3,last_champ_red_game_3
    else:
        return pick_blue_side_game_1, pick_red_side_game_1,pick_blue_side_game_2 , pick_red_side_game_2,last_champ_blue_game_1,last_champ_red_game_1,last_champ_blue_game_2,last_champ_red_game_2


def champion_into_number(champ_name):
    # req = Request(url="https://www.leagueoflegends.com/fr-fr/champions/",headers={'User-Agent': 'Mozilla/5.0'})
    # web_page = urlopen(req).read()
    # soup = bs(web_page,'html.parser')
    # compteur = 0
    # for a_tag in soup.find_all('a',{"class":"style__Wrapper-n3ovyt-0 style__ResponsiveWrapper-n3ovyt-4 ehjaZK elVPdk style__Item-sc-13btjky-3 CanXV isVisible isFirstTime"}):
    #     compteur+=1
    #     lien_page_champ = a_tag["href"]
    #     nom_champ_add = lien_page_champ[17:-1]
    #     all_champion[nom_champ_add]= compteur

    all_champion = {'aatrox': 1, 'ahri': 2, 'akali': 3, 'akshan': 4, 'alistar': 5, 'amumu': 6, 'anivia': 7, 'annie': 8, 'aphelios': 9, 'ashe': 10, 'aurelion sol': 11, 'azir': 12, 'bard': 13, "belveth": 14, 'blitzcrank': 15, 'brand': 16, 'braum': 17, 'caitlyn': 18, 'camille': 19, 'cassiopeia': 20, "chogath": 21, 'corki': 22, 'darius': 23, 'diana': 24, 'dr. mundo': 25, 'draven': 26, 'ekko': 27, 'elise': 28, 'evelynn': 29, 'ezreal': 30, 'fiddlesticks': 31, 'fiora': 32, 'fizz': 33, 'galio': 34, 'gangplank': 35, 'garen': 36, 'gnar': 37, 'gragas': 38, 'graves': 39, 'gwen': 40, 'hecarim': 41, 'heimerdinger': 42, 'illaoi': 43, 'irelia': 44, 'ivern': 45, 'janna': 46, 'jarvan iv': 47, 'jax': 48, 'jayce': 49, 'jhin': 50, 'jinx': 51, 'ksante': 52, "kaisa": 53, 'kalista': 54, 'karma': 55, 'karthus': 56, 'kassadin': 57, 'katarina': 58, 'kayle': 59, 'kayn': 60, 'kennen': 61, "kha'zix": 62, 'kindred': 63, 'kled': 64, "kog'maw": 65, 'leblanc': 66, 'lee sin': 67, 'leona': 68, 'lillia': 69, 'lissandra': 70, 'lucian': 71, 'lulu': 72, 'lux': 73, 'master yi': 74, 'malphite': 75, 'malzahar': 76, 'maokai': 77, 'milio': 78, 'miss fortune': 79, 'mordekaiser': 80, 'morgana': 81, 'nami': 82, 'nasus': 83, 'nautilus': 84, 'neeko': 85, 'nidalee': 86, 'nilah': 87, 'nocturne': 88, 'nunu': 89, 'olaf': 90, 'orianna': 91, 'ornn': 92, 'pantheon': 93, 'poppy': 94, 'pyke': 95, 'qiyana': 96, 'quinn': 97, 'rakan': 98, 'rammus': 99, "reksai": 100, 'rell': 101, 'renata glasc': 102, 'renekton': 103, 'rengar': 104, 'riven': 105, 'rumble': 106, 'ryze': 107, 'samira': 108, 'sejuani': 109, 'senna': 110, 'seraphine': 111, 'sett': 112, 'shaco': 113, 'shen': 114, 'shyvana': 115, 'singed': 116, 'sion': 117, 'sivir': 118, 'skarner': 119, 'sona': 120, 'soraka': 121, 'swain': 122, 'sylas': 123, 'syndra': 124, 'tahm-kench': 125, 'taliyah': 126, 'talon': 127, 'taric': 128, 'teemo': 129, 'thresh': 130, 'tristana': 131, 'trundle': 132, 'tryndamere': 133, 'twisted fate': 134, 'twitch': 135, 'udyr': 136, 'urgot': 137, 'varus': 138, 'vayne': 139, 'veigar': 140, 'velkoz': 141, 'vex': 142, 'vi': 143, 'viego': 144, 'viktor': 145, 'vladimir': 146, 'volibear': 147, 'warwick': 148, 'wukong': 149, 'xayah': 150, 'xerath': 151, 'xin zhao': 152, 'yasuo': 153, 'yone': 154, 'yorick': 155, 'yuumi': 156, 'zac': 157, 'zed': 158, 'zeri': 159, 'ziggs': 160, 'zilean': 161, 'zoe': 162, 'zyra': 163}
    for i in all_champion.keys():
        if i.replace(" ","")==champ_name.lower():
            return all_champion[i]
        elif i.replace("'","")==champ_name.lower():
            return all_champion[i]
        elif i.replace("-","")==champ_name.lower():
            return all_champion[i]
    print(champ_name)
    exit()

def number_into_champion(number):
    all_champion = {'aatrox': 1, 'ahri': 2, 'akali': 3, 'akshan': 4, 'alistar': 5, 'amumu': 6, 'anivia': 7, 'annie': 8, 'aphelios': 9, 'ashe': 10, 'aurelion sol': 11, 'azir': 12, 'bard': 13, "belveth": 14, 'blitzcrank': 15, 'brand': 16, 'braum': 17, 'caitlyn': 18, 'camille': 19, 'cassiopeia': 20, "chogath": 21, 'corki': 22, 'darius': 23, 'diana': 24, 'dr. mundo': 25, 'draven': 26, 'ekko': 27, 'elise': 28, 'evelynn': 29, 'ezreal': 30, 'fiddlesticks': 31, 'fiora': 32, 'fizz': 33, 'galio': 34, 'gangplank': 35, 'garen': 36, 'gnar': 37, 'gragas': 38, 'graves': 39, 'gwen': 40, 'hecarim': 41, 'heimerdinger': 42, 'illaoi': 43, 'irelia': 44, 'ivern': 45, 'janna': 46, 'jarvan iv': 47, 'jax': 48, 'jayce': 49, 'jhin': 50, 'jinx': 51, 'ksante': 52, "kaisa": 53, 'kalista': 54, 'karma': 55, 'karthus': 56, 'kassadin': 57, 'katarina': 58, 'kayle': 59, 'kayn': 60, 'kennen': 61, "kha'zix": 62, 'kindred': 63, 'kled': 64, "kog'maw": 65, 'leblanc': 66, 'lee sin': 67, 'leona': 68, 'lillia': 69, 'lissandra': 70, 'lucian': 71, 'lulu': 72, 'lux': 73, 'master yi': 74, 'malphite': 75, 'malzahar': 76, 'maokai': 77, 'milio': 78, 'miss fortune': 79, 'mordekaiser': 80, 'morgana': 81, 'nami': 82, 'nasus': 83, 'nautilus': 84, 'neeko': 85, 'nidalee': 86, 'nilah': 87, 'nocturne': 88, 'nunu': 89, 'olaf': 90, 'orianna': 91, 'ornn': 92, 'pantheon': 93, 'poppy': 94, 'pyke': 95, 'qiyana': 96, 'quinn': 97, 'rakan': 98, 'rammus': 99, "reksai": 100, 'rell': 101, 'renata glasc': 102, 'renekton': 103, 'rengar': 104, 'riven': 105, 'rumble': 106, 'ryze': 107, 'samira': 108, 'sejuani': 109, 'senna': 110, 'seraphine': 111, 'sett': 112, 'shaco': 113, 'shen': 114, 'shyvana': 115, 'singed': 116, 'sion': 117, 'sivir': 118, 'skarner': 119, 'sona': 120, 'soraka': 121, 'swain': 122, 'sylas': 123, 'syndra': 124, 'tahm-kench': 125, 'taliyah': 126, 'talon': 127, 'taric': 128, 'teemo': 129, 'thresh': 130, 'tristana': 131, 'trundle': 132, 'tryndamere': 133, 'twisted fate': 134, 'twitch': 135, 'udyr': 136, 'urgot': 137, 'varus': 138, 'vayne': 139, 'veigar': 140, 'velkoz': 141, 'vex': 142, 'vi': 143, 'viego': 144, 'viktor': 145, 'vladimir': 146, 'volibear': 147, 'warwick': 148, 'wukong': 149, 'xayah': 150, 'xerath': 151, 'xin zhao': 152, 'yasuo': 153, 'yone': 154, 'yorick': 155, 'yuumi': 156, 'zac': 157, 'zed': 158, 'zeri': 159, 'ziggs': 160, 'zilean': 161, 'zoe': 162, 'zyra': 163}
    for i in all_champion.keys():
        if all_champion[i]==number:
            return i
all_champion = {'aatrox': 1, 'ahri': 2, 'akali': 3, 'akshan': 4, 'alistar': 5, 'amumu': 6, 'anivia': 7, 'annie': 8, 'aphelios': 9, 'ashe': 10, 'aurelion sol': 11, 'azir': 12, 'bard': 13, "belveth": 14, 'blitzcrank': 15, 'brand': 16, 'braum': 17, 'caitlyn': 18, 'camille': 19, 'cassiopeia': 20, "chogath": 21, 'corki': 22, 'darius': 23, 'diana': 24, 'dr. mundo': 25, 'draven': 26, 'ekko': 27, 'elise': 28, 'evelynn': 29, 'ezreal': 30, 'fiddlesticks': 31, 'fiora': 32, 'fizz': 33, 'galio': 34, 'gangplank': 35, 'garen': 36, 'gnar': 37, 'gragas': 38, 'graves': 39, 'gwen': 40, 'hecarim': 41, 'heimerdinger': 42, 'illaoi': 43, 'irelia': 44, 'ivern': 45, 'janna': 46, 'jarvan iv': 47, 'jax': 48, 'jayce': 49, 'jhin': 50, 'jinx': 51, 'ksante': 52, "kaisa": 53, 'kalista': 54, 'karma': 55, 'karthus': 56, 'kassadin': 57, 'katarina': 58, 'kayle': 59, 'kayn': 60, 'kennen': 61, "kha'zix": 62, 'kindred': 63, 'kled': 64, "kog'maw": 65, 'leblanc': 66, 'lee sin': 67, 'leona': 68, 'lillia': 69, 'lissandra': 70, 'lucian': 71, 'lulu': 72, 'lux': 73, 'master yi': 74, 'malphite': 75, 'malzahar': 76, 'maokai': 77, 'milio': 78, 'miss fortune': 79, 'mordekaiser': 80, 'morgana': 81, 'nami': 82, 'nasus': 83, 'nautilus': 84, 'neeko': 85, 'nidalee': 86, 'nilah': 87, 'nocturne': 88, 'nunu': 89, 'olaf': 90, 'orianna': 91, 'ornn': 92, 'pantheon': 93, 'poppy': 94, 'pyke': 95, 'qiyana': 96, 'quinn': 97, 'rakan': 98, 'rammus': 99, "reksai": 100, 'rell': 101, 'renata glasc': 102, 'renekton': 103, 'rengar': 104, 'riven': 105, 'rumble': 106, 'ryze': 107, 'samira': 108, 'sejuani': 109, 'senna': 110, 'seraphine': 111, 'sett': 112, 'shaco': 113, 'shen': 114, 'shyvana': 115, 'singed': 116, 'sion': 117, 'sivir': 118, 'skarner': 119, 'sona': 120, 'soraka': 121, 'swain': 122, 'sylas': 123, 'syndra': 124, 'tahm-kench': 125, 'taliyah': 126, 'talon': 127, 'taric': 128, 'teemo': 129, 'thresh': 130, 'tristana': 131, 'trundle': 132, 'tryndamere': 133, 'twisted fate': 134, 'twitch': 135, 'udyr': 136, 'urgot': 137, 'varus': 138, 'vayne': 139, 'veigar': 140, 'velkoz': 141, 'vex': 142, 'vi': 143, 'viego': 144, 'viktor': 145, 'vladimir': 146, 'volibear': 147, 'warwick': 148, 'wukong': 149, 'xayah': 150, 'xerath': 151, 'xin zhao': 152, 'yasuo': 153, 'yone': 154, 'yorick': 155, 'yuumi': 156, 'zac': 157, 'zed': 158, 'zeri': 159, 'ziggs': 160, 'zilean': 161, 'zoe': 162, 'zyra': 163}
a = []
for i in all_champion.keys():
    a.append(i)
print(a)
# reqe = Request(url="https://gol.gg/tournament/tournament-matchlist/LPL%20Spring%202023/",headers={'User-Agent': 'Mozilla/5.0'})
# webpagee = urlopen(reqe).read()
# datas_x,datas_y = get_every_draft_from_league_bo3(webpagee)
# print(datas_x,datas_y)
# datas_x_json = jsonpickle.encode(datas_x, indent=4)
# with open('data_x_lpl.json',"w") as file:
#     file.write(datas_x_json)
# datas_y_json = jsonpickle.encode(datas_y, indent=4)
# with open('data_y_lpl.json',"w") as file:
#     file.write(datas_y_json)
# # print(champion_into_number('xerath'))
# reqe = Request(url="https://gol.gg/game/stats/48090/page-summary/",headers={'User-Agent': 'Mozilla/5.0'})
# webpagee = urlopen(reqe).read()
# extract_champion_names_bo3(webpagee)


