from selenium import webdriver as web
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import csv
from tqdm import tqdm
from util import Util

class System:
    def __init__(self, browser, visible, overwrite, list_food_names):
        self._list_food_names = list_food_names
        self._browser = browser
        self._visible = visible
        self._overwrite = overwrite
        self._driver = None
        self._dict_macros = {}

    def select_browser(self):
        _options = self.set_visibiliaty()
        match self._browser:
            case 'Chrome':
                self._driver = web.Chrome(options = _options)
            case 'Brave':
                _options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
                self._driver = web.Chrome(options = _options)

    def set_visibiliaty(self):
        _options = Options()
        if not self._visible:
            _options.add_argument("--headless")
        return _options

    def run_system(self):
        try:
            self.select_browser()
            self._driver.maximize_window()
            self._driver.get("https://vitat.com.br/alimentacao/busca-de-alimentos")
            self.get_macros()

        except Exception as e:
            print(type(e).__name__, e, '|', 'line {}'.format(sys.exc_info()[-1].tb_lineno))
            return False
        else:
            return True
    
    def get_macros(self):
        for food in tqdm(self._list_food_names):
            self.search_food(food)
            dict_food_macro = self.get_info_by_dropdown(Select(self._driver.find_element(By.XPATH, '//*[@id="dllMedida"]')))
            self._dict_macros[food] = dict_food_macro

    def search_food(self, food):
        self._driver.find_element(By.XPATH, '//*[@id="input"]').send_keys(food)
        self._driver.find_element(By.XPATH, '//*[@id="input"]').send_keys(Keys.ENTER)
        self._driver.find_element(By.XPATH, '//*[@id="Content"]/div[3]/div[1]/div/div/div/div/ul/li[1]/a').send_keys(Keys.ENTER)

    
    def get_info_by_dropdown(self, drop_down):
        dict_macros_unit_measures = {}
        dict_unit_measures_info = {'12':['Unidade', '1'], '16':['Colher de Sopa','1'], '115':['Gramas (100g)', '100'], '1':['Colher de Sopa','1']}
        for unit_measure in drop_down.options:
            value_unit_measure = unit_measure.get_attribute('value')
            if value_unit_measure in ['12','16','115','1']:  #unidade, colher_de_sopa, gramas
                drop_down.select_by_value(value_unit_measure)
                self._driver.find_element(By.XPATH, '//*[@id="quantidadeMedida"]').clear()
                time.sleep(0.2)
                self._driver.find_element(By.XPATH, '//*[@id="quantidadeMedida"]').send_keys(dict_unit_measures_info[value_unit_measure][1])
                time.sleep(0.2)
                self._driver.find_element(By.XPATH, '//*[@id="form0"]/div[2]/button').send_keys(Keys.ENTER)
                time.sleep(0.5)
                dict_info = self.read_body_web_table()
                dict_macros_unit_measures[dict_unit_measures_info[value_unit_measure][0]] = dict_info
                        
        return dict_macros_unit_measures
        
    
    def read_body_web_table(self):
        dict_info = {}
        table = self._driver.find_element(By.XPATH, '//*[@id="infoNutricional"]/table')
        body = table.find_element(By.TAG_NAME, 'tbody')
        rows = body.find_elements(By.TAG_NAME, 'tr')
        for i, row1 in enumerate(rows):
            if(i in [1,2,4,5,7,8]):
                row2 = row1.find_elements(By.TAG_NAME, 'td')
                dict_info[row2[0].text] = str(row2[1].text).split()[0].replace('.', ',')

        return dict_info

    def write_response_on_file(self):
        try:
            with open('./macros.csv', Util.set_overwriting(self._overwrite), encoding='utf-8-sig') as file_macro:
                write_macro = csv.writer(file_macro, delimiter =';')
                macros_header =['Alimento', 'Unidade de Medida', 'Calorias (kcal)', 'Carboidratos (g)', 'Proteínas (g)', 'Gorduras totais (g)', 'Fibra alimentar (g)', 'Sódio (mg)']
                write_macro.writerow(macros_header)
                for food in tqdm(self._dict_macros):
                    for unit_measure in self._dict_macros[food]:
                        macros_values = list(self._dict_macros[food][unit_measure].values())
                        macros_values.insert(0, food)
                        macros_values.insert(1, unit_measure)
                        write_macro.writerow(macros_values)

        except Exception as e:
            print(type(e).__name__, e, '|', 'line {}'.format(sys.exc_info()[-1].tb_lineno))
            return False
        else:
            return True


    