import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

option = webdriver.ChromeOptions()
option.add_argument("-headless")

driver = webdriver.Chrome(options=option)
import time

def bwin_both_teams_score_fb():
    URL = r"https://sports.bwin.de/de/sports/fu%C3%9Fball-4/heute"
    driver.get(url=URL)
    driver.implicitly_wait(5)

    # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/vn-app/vn-dynamic-layout-slot[3]/vn-header/header/vn-dynamic-layout-slot[2]/ms-navigation/div[1]/nav/ms-main-items/ms-scroll-adapter/div/div/div/vn-menu-item[4]')))
    # button.click()

    # calendarbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/vn-app/vn-dynamic-layout-slot[3]/vn-header/header/vn-dynamic-layout-slot[2]/ms-sub-navigation/ms-tab-bar/ms-scroll-adapter/div/div/ul/li[4]/a')))
    # calendarbutton.click()

    # in30minbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-view"]/ms-fixture-list/div/ms-calendar-item-list/div/ms-scroll-adapter/div/div/ms-item[1]/a')))
    # #in30minbutton.click()

    dropdown = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, "title.multiple")))
    ActionChains(driver).move_to_element(dropdown).click().perform()
    time.sleep(1)
    ActionChains(driver).move_by_offset(0,100).click().perform()

    
    dropdown1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, "sort-selector")))
    ActionChains(driver).move_to_element(dropdown1).click().perform()
    time.sleep(1)
    ActionChains(driver).move_by_offset(0,50).click().perform()
    time.sleep(2)
    #quotes scraping
    btts, teams = [], []

    box = driver.find_element(By.XPATH, '//ms-grid')
    rows = WebDriverWait(box, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'grid-event')))

    #quotes from rows
    for row in rows:
        odds = row.find_elements(By.CLASS_NAME, 'grid-option-group')
        try:
            empty_events = row.find_elements(By.CLASS_NAME, 'empty')
            odd = odds[0] if odds[0] not in empty_events else ''
            btts.append(odd.text)
            grandparent = odd.find_element(By.XPATH, './..').find_element(By.XPATH, './..')
            teams.append(grandparent.find_element(By.CLASS_NAME, 'grid-event-name').text)
        except:
            pass

    
    final_btts = []
    for s in btts:
        final_btts.append(str(s).split("\n"))
        
    final_teams = []
    for s in teams:
        final_teams.append(str(s).split("\n"))

    return final_btts,final_teams

def bwin_tn():
    URL = r"https://sports.bwin.de/de/sports/tennis-5"
    driver.get(url=URL)
    driver.implicitly_wait(5)

    # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/vn-app/vn-dynamic-layout-slot[3]/vn-header/header/vn-dynamic-layout-slot[2]/ms-navigation/div[1]/nav/ms-main-items/ms-scroll-adapter/div/div/div/vn-menu-item[4]')))
    # button.click()

    # calendarbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/vn-app/vn-dynamic-layout-slot[3]/vn-header/header/vn-dynamic-layout-slot[2]/ms-sub-navigation/ms-tab-bar/ms-scroll-adapter/div/div/ul/li[4]/a')))
    # calendarbutton.click()

    # in30minbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-view"]/ms-fixture-list/div/ms-calendar-item-list/div/ms-scroll-adapter/div/div/ms-item[1]/a')))
    # #in30minbutton.click()

    #quotes scraping
    btts, teams = [], []

    box = driver.find_element(By.XPATH, '//ms-grid')
    rows = WebDriverWait(box, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'grid-event')))

    #quotes from rows
    for row in rows:
        odds = row.find_elements(By.CLASS_NAME, 'grid-option-group')
        try:
            empty_events = row.find_elements(By.CLASS_NAME, 'empty')
            odd = odds[0] if odds[0] not in empty_events else ''
            btts.append(odd.text)
            grandparent = odd.find_element(By.XPATH, './..').find_element(By.XPATH, './..')
            teams.append(grandparent.find_element(By.CLASS_NAME, 'grid-event-name').text)
        except:
            pass

    
    final_btts = []
    for s in btts:
        final_btts.append(str(s).split("\n"))
        
    final_teams = []
    for s in teams:
        final_teams.append(str(s).split("\n"))

    return final_btts,final_teams

def bwin_ds():
    URL = r"https://sports.bwin.de/de/sports/darts-34"
    driver.get(url=URL)
    driver.implicitly_wait(5)

    # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/vn-app/vn-dynamic-layout-slot[3]/vn-header/header/vn-dynamic-layout-slot[2]/ms-navigation/div[1]/nav/ms-main-items/ms-scroll-adapter/div/div/div/vn-menu-item[4]')))
    # button.click()

    # calendarbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/vn-app/vn-dynamic-layout-slot[3]/vn-header/header/vn-dynamic-layout-slot[2]/ms-sub-navigation/ms-tab-bar/ms-scroll-adapter/div/div/ul/li[4]/a')))
    # calendarbutton.click()

    # in30minbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-view"]/ms-fixture-list/div/ms-calendar-item-list/div/ms-scroll-adapter/div/div/ms-item[1]/a')))
    # #in30minbutton.click()

    #quotes scraping
    btts, teams = [], []

    box = driver.find_element(By.XPATH, '//ms-grid')
    rows = WebDriverWait(box, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'grid-event')))

    #quotes from rows
    for row in rows:
        odds = row.find_elements(By.CLASS_NAME, 'grid-option-group')
        try:
            empty_events = row.find_elements(By.CLASS_NAME, 'empty')
            odd = odds[0] if odds[0] not in empty_events else ''
            btts.append(odd.text)
            grandparent = odd.find_element(By.XPATH, './..').find_element(By.XPATH, './..')
            teams.append(grandparent.find_element(By.CLASS_NAME, 'grid-event-name').text)
        except:
            pass

    
    final_btts = []
    for s in btts:
        final_btts.append(str(s).split("\n"))
        
    final_teams = []
    for s in teams:
        final_teams.append(str(s).split("\n"))

    return final_btts,final_teams

def tipico_both_teams_score_fb():
    #tipico
    driver.get("https://sports.tipico.de/de/heute/fussball")
    driver.implicitly_wait(5)

    #cookies
    try:
        driver.find_element(By.CLASS_NAME, 'evidon-banner-acceptbutton').click()
        time.sleep(3)
    except:
        pass

    #sort after Zeit
    driver.find_element(By.XPATH, '//*[@id="app"]/main/main/section/div/div[1]/div[1]/div/label[1]').click()

    #both teams score
    dropdown = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, "SportHeader-styles-module-drop-down")))
    select = Select(dropdown)
    select.select_by_visible_text('Beide Teams treffen')
    

    #quotes scraping
    btts, teams = [], []

    box = driver.find_element(By.XPATH, '//*[@id="app"]/main/main/section/div/div[1]')
    rows = WebDriverWait(box, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'EventRow-styles-module-event-row')))

    #quotes from rows
    for row in rows:
        odds = row.find_elements(By.CLASS_NAME, 'EventOddGroup-styles-module-odd-group')
        try:
            odd = odds[0]
            btts.append(odd.text)
            grandparent = row.find_element(By.CLASS_NAME, 'EventTeams-styles-module-titles')
            teams.append(grandparent.text)
        except:
            pass



    final_btts = []
    for s in btts:
        final_btts.append(str(s).split("\n"))
        
    final_teams = []
    for s in teams:
        final_teams.append(str(s).split("\n"))

    for i in range(len(final_btts)):
        for j in range(len(final_btts[i])):
            final_btts[i][j] = final_btts[i][j].replace(",", ".")

    return final_btts, final_teams

def tipico_tn():
    #tipico öffnen
    driver.get("https://sports.tipico.de/de/heute/tennis")
    driver.implicitly_wait(5)

    #cookies essen
    try:
        driver.find_element(By.CLASS_NAME, 'evidon-banner-acceptbutton').click()
        time.sleep(3)
    except:
        pass

    #sortieren nach Zeit
    driver.find_element(By.XPATH, '//*[@id="app"]/main/main/section/div/div[1]/div[1]/div/label[1]').click()
    
    #quotes scraping
    btts, teams = [], []

    box = driver.find_element(By.XPATH, '//*[@id="app"]/main/main/section/div/div[1]')
    rows = WebDriverWait(box, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'EventRow-styles-module-event-row')))

    #quotes aus rows raus polishen
    for row in rows:
        odds = row.find_elements(By.CLASS_NAME, 'EventOddGroup-styles-module-odd-group')
        try:
            odd = odds[0]
        except:
            pass
        if (odd):
            btts.append(odd.text)
            grandparent = row.find_element(By.CLASS_NAME, 'EventTeams-styles-module-titles')
            teams.append(grandparent.text)



    final_btts = []
    for s in btts:
        final_btts.append(str(s).split("\n"))
        
    final_teams = []
    for s in teams:
        final_teams.append(str(s).split("\n"))

    for i in range(len(final_btts)):
        for j in range(len(final_btts[i])):
            final_btts[i][j] = final_btts[i][j].replace(",", ".")

    return final_btts, final_teams

def tipico_ds():
    #tipico
    driver.get("https://sports.tipico.de/de/heute/darts")
    driver.implicitly_wait(5)

    #cookies
    try:
        driver.find_element(By.CLASS_NAME, 'evidon-banner-acceptbutton').click()
        time.sleep(3)
    except:
        pass

    #sortieren after Zeit
    driver.find_element(By.XPATH, '//*[@id="app"]/main/main/section/div/div[1]/div[1]/div/label[1]').click()
    
    #quotes scraping
    btts, teams = [], []

    box = driver.find_element(By.XPATH, '//*[@id="app"]/main/main/section/div/div[1]')
    rows = WebDriverWait(box, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'EventRow-styles-module-event-row')))

    #quotes from rows
    for row in rows:
        odds = row.find_elements(By.CLASS_NAME, 'EventOddGroup-styles-module-odd-group')
        try:
            odd = odds[0]
        except:
            pass
        if (odd):
            btts.append(odd.text)
            grandparent = row.find_element(By.CLASS_NAME, 'EventTeams-styles-module-titles')
            teams.append(grandparent.text)



    final_btts = []
    for s in btts:
        final_btts.append(str(s).split("\n"))
        
    final_teams = []
    for s in teams:
        final_teams.append(str(s).split("\n"))

    for i in range(len(final_btts)):
        for j in range(len(final_btts[i])):
            final_btts[i][j] = final_btts[i][j].replace(",", ".")

    return final_btts, final_teams

def calculate_arbitrage(quotes1:list, quotes2:list):
    #input 2 list with quotes
    #output 1 2D list: 
    #1.element True or False (arbitrage works)
    #2-element int:number of quote from first input
    #3.element int:number of quote from second input

    result = []

    i = 0
    while(i < len(quotes1)):
        try:
            quote1 = float(quotes1[i][0])
            quote2 = float(quotes1[i][1])
            quote3 = float(quotes2[i][0])
            quote4 = float(quotes2[i][1])
        except:
            i += 1
            continue

        quote1 = 1 / quote1
        quote2 = 1 / quote2
        quote3 = 1 / quote3
        quote4 = 1 / quote4

        if(quote1 + quote4 < 1):
            #arbitrage possible
            res = []
            element1 = True
            element2 = 0
            element3 = 1
            res.append(element1)
            res.append(element2)
            res.append(element3)
        elif(quote2 + quote3 < 1):
            #arbitrage possible
            res = []
            element1 = True
            element2 = 1
            element3 = 0
            res.append(element1)
            res.append(element2)
            res.append(element3)
        try:
            result.append(res)
        except:
            pass
        #arbitrage impossible
        i += 1
    return result

def find_common_games_case_insensitive(bwin_teams, bwin_odds, tipico_teams, tipico_odds):
    common_games = []
    common_bwin_odds = []
    common_tipico_odds = []

    # Create a dictionary for tipico teams and their odds for quick lookup, using lowercase for case-insensitive matching
    tipico_dict = {tuple(map(str.lower, game)): odds for game, odds in zip(tipico_teams, tipico_odds)}

    for bwin_game, bwin_odd in zip(bwin_teams, bwin_odds):
        bwin_game_tuple = tuple(map(str.lower, bwin_game))

        # Check if the bwin game exists in the tipico dictionary
        if bwin_game_tuple in tipico_dict:
            tipico_odd = tipico_dict[bwin_game_tuple]

            # Add to the common games and odds lists
            common_games.append(bwin_game)
            common_bwin_odds.append(bwin_odd)
            common_tipico_odds.append(tipico_odd)

    return common_games, common_bwin_odds, common_tipico_odds

def main(i:int):
    if i == 0:
        bwinodds,bwinteams = bwin_ds()
        tipicoodds, tipicoteams = tipico_ds()
    elif i == 1:
        bwinodds,bwinteams = bwin_tn()
        tipicoodds, tipicoteams = tipico_tn()
    elif i == 2:
        bwinodds,bwinteams = bwin_both_teams_score_fb()
        tipicoodds, tipicoteams = tipico_both_teams_score_fb()
    
    common_games, common_bwin_odds, common_tipico_odds = find_common_games_case_insensitive(bwinteams, bwinodds, tipicoteams, tipicoodds)

    result = calculate_arbitrage(common_bwin_odds, common_tipico_odds)

    i = 0
    for e in result:
        try:
            if result[i][0] == True:
                print("Arbitrage found:\n")
                print("Game:\n")
                print(common_games[i][0] + " vs. " + common_games[i][1])
                print("-----------")
                print("BWIN: " + common_bwin_odds[i][e[1]] + " | Tipico: " + common_tipico_odds[i][e[2]])
        except:
            pass


main(0)


driver.close()