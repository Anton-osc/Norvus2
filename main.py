from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import escape_markup
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
import requests
import json
import datetime
from datetime import datetime as dt
from random import randint

#VARS
CITY = 'Smila'  # Add settings, add opportunity to change city

class NorVusApp(App):
    def build(self):
        #Vars
        self.timer1 = False
        self.timer2 = False
        self.timer3 = False
        self.timer4 = False
        ##
        self.color = '[color=00FFFF]'
        self.x, self.y = Window.size
        ##
        self.layout2 = FloatLayout(size=(Window.size))
        ##
        if self.x * self.y <= 1000000:
            pos_image = (490, self.y // 2 - 450)
            pos_thermometer = (625, self.y // 2 - 265)
            pos_button2 = (270, self.y // 2 + 30)
            pos_button3 = (20, self.y - 500)
            pos_button4 = (270, self.y // 2 - 200)
            font_size_label2 = '260sp'
            pos_label2 = (-145, self.y // 2 - 350)      # Time
            pos_label3 = (490, self.y // 2 - 250)       # Temperature
            pos_label4 = (490, self.y // 2 - 350)       # Separator
            pos_label5 = (460, self.y // 2 - 620)       # WeekDay
        elif self.x * self.y >= 2400000:
            pos_image = (800, self.y // 2 - 550)
            pos_thermometer = (980, self.y // 2 - 350)
            pos_button2 = (420, self.y // 2 + 30)
            pos_button3 = (20, self.y - 500)
            font_size_label2 = '280sp'
            pos_button4 = (420, self.y // 2 - 400)
            pos_label2 = (-380, self.y // 2 - 520)      # Time
            pos_label3 = (800, self.y // 2 - 350)       # Temperature
            pos_label4 = (800, self.y // 2 - 450)       # Separator
            pos_label5 = (750, self.y // 2 - 850)       # WeekDay
        ##
        self.image_mist = AsyncImage(source='http://openweathermap.org/img/wn/50d@2x.png', pos=pos_image)
        self.image_rain = Image(source='IconsW/rain2.png', pos=pos_image)
        self.image_snow = Image(source='IconsW/snow2.png', pos=pos_image)
        self.image_sun = Image(source='IconsW/sun2.png', pos=pos_image)
        self.image_cloud = Image(source='IconsW/cloud2.png', pos=pos_image)
        self.image_grad = Image(source='IconsW/grad2.png', pos=pos_thermometer)
        self.image_thunder = AsyncImage(source='http://openweathermap.org/img/wn/11d@2x.png', pos=pos_image)
        self.image_internetError = Image(source='IconsW/internet_error.png', pos=pos_image)
        ##
        self.btn2 = Button(text ="Currency",
            font_size ="40sp",
            background_color =(1, 1, 1, 1),
            color =(1, 1, 1, 1),
            size =(50, 50),
            size_hint =(.6, .2),
            pos=pos_button2)

        self.btn3 = Button(text ="",
            font_size ="10sp",
            background_color =(255, 0, 0, 0.006),
            color =(1, 1, 1, 0.006),
            size =(1, 1),
            size_hint =(.200, .700),
            pos=pos_button3) 

        self.btn4 = Button(text ="MeteoStation",
            font_size ="40sp",
            background_color = (255, 20, 147, 0.1),
            color =(1, 1, 1, 1),
            size =(50, 50),
            size_hint =(.6, .2),
            pos=pos_button4)
        ##
        self.btn2.bind(on_press=self.callback2)
        self.btn3.bind(on_press=self.callback3)
        self.btn4.bind(on_press=self.callback4)
        ##
        self.label = Label(text='[font=fonts/digital-7.ttf]' + self.color + escape_markup(self.update_info()) + '[/color][/font]', font_size='70sp', markup=True)
        self.label2 = Label(text='[font=fonts/digital-7.ttf]' + '[color=FFFFFF]' + escape_markup(self.update_time()) + '[/color][/font]', font_size=font_size_label2, pos = pos_label2, markup=True)
        self.label3 = Label(text='[font=fonts/digital-7.ttf]' + '[color=00FFFF]' + escape_markup(self.temperature()) + '[/color][/font]', font_size='70sp', pos = pos_label3, markup=True)
        self.label4 = Label(text='[font=fonts/digital-7.ttf]' + '[color=00FFFF]' + '------' + '[/color][/font]', font_size='30sp', pos = pos_label4, markup=True)
        self.label5 = Label(text='[font=fonts/roboto_thin.ttf]' + '[color=00FFFF]' + escape_markup(self.week_day()) + '[/color][/font]', font_size='30sp', pos = pos_label5, markup=True)
        ##
        self.layout2.add_widget(self.btn2)
        self.layout2.add_widget(self.btn4)
        ##
        return self.layout2

    def update(self):
        self.label.text = '[font=fonts/digital-7.ttf]' + self.color + escape_markup(self.update_info()) + '[/color][/font]'

    def update2_time(self):
        self.label2.text = '[font=fonts/digital-7.ttf]' + '[color=FFFFFF]' + escape_markup(self.update_time()) + '[/color][/font]'

    def update_temperature(self):
        self.label3.text = '[font=fonts/digital-7.ttf]' + '[color=00FFFF]' + escape_markup(self.temperature()) + '[/color][/font]' + '[color=00FFFF][size=90]' + '°' + '[/size]'

    def update_week_day(self):
        self.label5.text = '[font=fonts/roboto_thin.ttf]' + '[color=00FFFF]' + escape_markup(self.week_day()) + '[/color][/font]'

    def callback2(self, event):
        '''Switch to Currency'''
        self.color = '[color=00FFFF]'
        self.update()
        self.layout2.clear_widgets()
        self.layout2.add_widget(self.label)
        self.layout2.add_widget(self.btn3)
        self.timer1 = True
        self.what_update()

    def callback3(self, event):
        '''Switch to Main Menu'''
        self.layout2.clear_widgets()
        self.layout2.add_widget(self.btn2)
        self.layout2.add_widget(self.btn4)
        if self.timer1 == True:
            self.event2.cancel()
        if self.timer4 == True:
            self.event4.cancel()
            self.event5.cancel()
            self.event6.cancel()
        if self.timer2 == True:
            self.event8.cancel()
        self.timer1 = False
        self.timer4 = False
        self.timer2 = False

    def callback4(self, event):
        '''Switch to MeteoStation'''
        self.layout2.clear_widgets()
        self.update_temperature()
        self.layout2.add_widget(self.btn3)
        self.layout2.add_widget(self.label2)
        self.layout2.add_widget(self.label3)
        self.layout2.add_widget(self.label4)
        self.layout2.add_widget(self.label5)
        self.layout2.add_widget(self.image_grad)
        self.weather()
        self.update_week_day()
        self.timer4 = True
        self.what_update()    

    def what_update(self):
        '''Detecting in which section we are'''
        if self.timer4 == True:
            self.event = Clock.schedule_interval(lambda dt: self.update2_time(), 0.5)
            self.event4 = Clock.schedule_interval(lambda dt: self.update_temperature(), 60)
            self.event5 = Clock.schedule_interval(lambda dt: self.weather(), 60)
            self.event6 = Clock.schedule_interval(lambda dt: self.update_week_day(), 60)

        if self.timer1 == True:
            self.event2 = Clock.schedule_interval(lambda dt: self.update(), 60)
  
    def temperature(self):
        '''Get temperature data to display it'''
        global CITY
        try:
            apiKey = '2a4ae60457302d705c3d431e1e465c4c'
            cityName = CITY
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&appid=' + apiKey 

            response = requests.get(url)
            response = response.json()

            temp = response['main']
            temp = temp['temp']
            temp = round(float(temp) -273)
            temp = str(temp)
            return temp
        except:
            return str('')

    def weather(self):
        '''Get weather data to display picture'''
        global CITY
        try:
            apiKey = '2a4ae60457302d705c3d431e1e465c4c'
            cityName = CITY
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&appid=' + apiKey 

            response = requests.get(url)
            response = response.json()
            weather = response['weather']
            weather2 = []
            for i in weather:
                weather2.append(i)
            weather = weather2[0]
            weather = weather['main']
        except:
            weather = 'Internet'

        if weather == 'Clouds':
            self.layout2.clear_widgets()
            self.layout2.add_widget(self.btn3)
            self.layout2.add_widget(self.label2)
            self.layout2.add_widget(self.label3)
            self.layout2.add_widget(self.label4)
            self.layout2.add_widget(self.image_cloud)
            self.layout2.add_widget(self.image_grad)
            self.layout2.add_widget(self.label5)
        elif weather == 'Snow':
            self.layout2.clear_widgets()
            self.layout2.add_widget(self.btn3)
            self.layout2.add_widget(self.label2)
            self.layout2.add_widget(self.label3)
            self.layout2.add_widget(self.label4)
            self.layout2.add_widget(self.image_snow)
            self.layout2.add_widget(self.image_grad)
            self.layout2.add_widget(self.label5)
        elif weather == 'Clear Sky':
            self.layout2.clear_widgets()
            self.layout2.add_widget(self.btn3)
            self.layout2.add_widget(self.label2)
            self.layout2.add_widget(self.label3)
            self.layout2.add_widget(self.label4)
            self.layout2.add_widget(self.image_sun)
            self.layout2.add_widget(self.image_grad)
            self.layout2.add_widget(self.label5)
        elif weather == 'Thunderstorm':
            self.layout2.clear_widgets()
            self.layout2.add_widget(self.btn3)
            self.layout2.add_widget(self.label2)
            self.layout2.add_widget(self.label3)
            self.layout2.add_widget(self.label4)
            self.layout2.add_widget(self.image_thunder)
            self.layout2.add_widget(self.image_grad)
            self.layout2.add_widget(self.label5)
        elif weather == 'Rain':
            self.layout2.clear_widgets()
            self.layout2.add_widget(self.btn3)
            self.layout2.add_widget(self.label2)
            self.layout2.add_widget(self.label3)
            self.layout2.add_widget(self.label4)
            self.layout2.add_widget(self.image_rain)
            self.layout2.add_widget(self.image_grad)
            self.layout2.add_widget(self.label5)
        elif weather == 'Internet':
            self.layout2.clear_widgets()
            self.layout2.add_widget(self.btn3)
            self.layout2.add_widget(self.label2)
            self.layout2.add_widget(self.label3)
            self.layout2.add_widget(self.label4)
            self.layout2.add_widget(self.image_internetError)
            self.layout2.add_widget(self.image_grad)
            self.layout2.add_widget(self.label5)
        else:
            self.layout2.clear_widgets()
            self.layout2.add_widget(self.btn3)
            self.layout2.add_widget(self.label2)
            self.layout2.add_widget(self.label3)
            self.layout2.add_widget(self.label4)
            self.layout2.add_widget(self.image_mist)
            self.layout2.add_widget(self.image_grad)
            self.layout2.add_widget(self.label5)

    def week_day(self):
        '''Identify the week day'''
        week_Day = ''
        day = datetime.datetime.today().weekday()
        if day == 0:
            week_Day = 'Monday'
        elif day == 1:
            week_Day = 'Tuesday'
        elif day == 2:
            week_Day = 'Wednesday'
        elif day == 3:
            week_Day = 'Thursday'
        elif day == 4:
            week_Day = 'Friday'
        elif day == 5:
            week_Day = 'Saturday'
        elif day == 6:
            week_Day = 'Sunday'
        else:
            week_Day = 'NONE'

        return week_Day

    def getbtc(self):
    	try:
            req1 = requests.get('https://blockchain.info/ticker')
            req01 = req1.json()
            blockchain = json.dumps(req01['USD'] ['buy'], indent=2)
            blockchain = round(float(blockchain), 1)
            blockchain = str('BTC:  ') + str(blockchain) + str('$')
            req2 = requests.get('https://api.coingecko.com/api/v3/coins/ethereum')
            req02 = req2.json()
            ether = json.dumps(req02['market_data'] ['current_price'])
            ether = json.loads(ether)
            eter = ether['usd']
            eter = 'ETC:  ' + str(eter) + str('$')
            blockchain = blockchain + '\n\n\n\n' + eter
            return blockchain
    	except:
            return str('Internet Lost!')

    def update_info(self):
        '''Updating currency information'''
        self.btc = self.getbtc()
        return self.btc

    def update_time(self):
        now = datetime.datetime.now()
        self.time_now = now.strftime("%H:%M")
        return self.time_now

    def detect_screen(self):
        self.x, self.y = Window.size
        if self.x > self.y:
            self.label.font_size = '70sp'
        elif self.btc == 'Internet Lost!':
            self.label.font_size = '45sp'
        else:
            self.label.font_size = '55sp'


NorVusApp().run()
