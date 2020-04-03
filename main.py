import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from functools import partial

kivy.require('1.11.1')

class LoginScreen(GridLayout):

    def authenticate(self, touch):
        '''if self.username.text == 'dastullo' and self.password.text == 'Sageismine':
            print('Access Granted!')
            Window.size = (500, 200)
            login.sm.current = 'menu'
        else:
            print('Unauthorized Access!')'''
        print('Access Granted!')
        Window.size = (500, 200)
        login.sm.current = 'menu'

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        details = GridLayout(cols = 2)
        details.user_label = Label(text = 'Username')
        self.username = TextInput(multiline = False)
        details.pword_label = Label(text = 'Password')
        self.password = TextInput(password = True, multiline = False)
        btn = Button(text = 'Submit', size_hint = (1, 0.75))
        btn.bind(on_press = self.authenticate)
        details.add_widget(details.user_label)
        details.add_widget(self.username)
        details.add_widget(details.pword_label)
        details.add_widget(self.password)
        self.add_widget(details)
        self.add_widget(btn)

class MenuScreen(BoxLayout):

    def LoginBot(self, touch, call, username, password):
        websites = ['http://instagram.com/', 'http://facebook.com/', 'https://www.reddit.com/login/', 'https://github.com/login']
        comb_xpath = [['//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input','//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'],
                      ['//*[@id="email"]', '//*[@id="pass"]'],
                      ['//*[@id="loginUsername"]', '//*[@id="loginPassword"]'],
                      ['//*[@id="login_field"]', '//*[@id="password"]']]
        option = Options()
        option.add_argument('--disable-notifications')
        ##option.add_experimental_option('prefs', {'profile.default_content_setting_values.notifications:': 1})
        browser = webdriver.Chrome(options = option, executable_path = '/usr/local/bin/chromedriver')
        browser.get(websites[call])
        sleep(2)
        uname_login = browser.find_element_by_xpath(comb_xpath[call][0])
        pword = browser.find_element_by_xpath(comb_xpath[call][1])
        uname_login.send_keys(username)
        pword.send_keys(password)
        pword.send_keys(Keys.ENTER)

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        cols = 1
        grid = GridLayout(cols = 2)
        ig_btn = Button(text = 'Instagram')
        ig_call = partial(self.LoginBot, call = 0, username = 'iammustard_dast', password = 'Mustard@1993')
        ig_btn.bind(on_release = ig_call)
        fb_btn = Button(text = 'Facebook')
        fb_call = partial(self.LoginBot, call = 1, username = '8764810845', password = 'newton1664')
        fb_btn.bind(on_release = fb_call)
        r_btn = Button(text = 'Reddit')
        r_call = partial(self.LoginBot, call = 2, username = 'thenoblesage', password = 'Mustard@1993')
        r_btn.bind(on_release = r_call)
        gh_btn = Button(text='Git Hub')
        gh_call = partial(self.LoginBot, call = 3, username = 'thenoblesage', password = 'Mustard@1993')
        gh_btn.bind(on_release = gh_call)
        grid.add_widget(ig_btn)
        grid.add_widget(fb_btn)
        grid.add_widget(r_btn)
        grid.add_widget(gh_btn)
        self.add_widget(grid)

class LoginApp(App):
    def build(self):
        Window.size = (500, 150)
        self.sm = ScreenManager()
        login_screen = Screen(name = 'login')
        menu_screen = Screen(name = 'menu')
        authentication_page = LoginScreen()
        menu_page = MenuScreen()
        login_screen.add_widget(authentication_page)
        menu_screen.add_widget(menu_page)
        self.sm.add_widget(login_screen)
        self.sm.add_widget(menu_screen)
        return self.sm

if __name__ == '__main__':
    login = LoginApp()
    login.run()