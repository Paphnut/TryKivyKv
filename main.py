#import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.accordion import Accordion
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
#from kivy.core.window import Window

class Accor(Accordion):
    #Функция инициализации
    def __init__(self,**kwargs):
        super(Accor, self).__init__(**kwargs)
        self.ids.min1.bind(on_press=self.pressmin1)
        self.ids.plu1.bind(on_press=self.pressplu1)
        self.ids.min2.bind(on_press=self.pressmin2)
        self.ids.plu2.bind(on_press=self.pressplu2)
        self.ids.min3.bind(on_press=self.pressmin3)
        self.ids.plu3.bind(on_press=self.pressplu3)
        self.ids.submit2.bind(on_press=self.days_select)
        self.ids.submit3.bind(on_press=self.premium_and_result)

    def pressmin1(self, instance):
        if (int(self.ids.days1.text) > 0):
            days1 = int(self.ids.days1.text) - 1
            self.ids.days1.text = str(days1)
            if (int(self.ids.days2.text) > days1):
                ds = int(self.ids.days1.text)
                self.ids.days2.text = str(ds)
            else:
                pass
            if (int(self.ids.days3.text)>days1):
                ds1 = int(self.ids.days1.text)
                self.ids.days3.text = str(ds1)
            else:
                pass
        else:
            pass

    def pressplu1(self, instance):
        days1 = int(self.ids.days1.text) + 1
        self.ids.days1.text = str(days1)

    def pressmin2(self, instance):
        if (int(self.ids.days2.text) > 0):
            days2 = int(self.ids.days2.text)-1
            self.ids.days2.text = str(days2)
        else:
            return
    def pressplu2(self, instance):
        if (int(self.ids.days2.text) < int(self.ids.days1.text)):
            days2 = int(self.ids.days2.text)+1
            self.ids.days2.text = str(days2)
        else:
            pass

    def pressmin3(self, instance):
        if (int(self.ids.days3.text) > 0):
            days3 = int(self.ids.days3.text)-1
            self.ids.days3.text = str(days3)
        else:
            pass
    def pressplu3(self, instance):
        if (int(self.ids.days3.text) < int(self.ids.days1.text)):
            days3 = int(self.ids.days3.text)+1
            self.ids.days3.text = str(days3)
        else:
            pass

    checks = []
    def checkbox_click(self, instance, value, price):
        if value == True:
            Accor.checks.append(price)
            price1 = ''
            for x in Accor.checks:
               price1 = f'{price1} {x}'
            self.ids.item1.title = f'Вы выбрали: {price1}'
        else:
            Accor.checks.remove(price)
            price1 = ''
            for x in Accor.checks:
                price1 = f'{price1} {x}'
            self.ids.item1.title = f'Вы выбрали: {Accor.checks}'
    days = []
    cat1 = [3025,3350,2150]
    cat2 = [2605,2660,1680]
    cat3 = [2190,2480,1715]
    cat4 = [1775,2050,1500]
    def days_select(self, instance):
        Accor.days = []
        Accor.days.append(self.ids.days1.text)
        Accor.days.append(self.ids.days2.text)
        Accor.days.append(self.ids.days3.text)
#        print('Дней'+Accor.days[0]+'не рабочих'+Accor.days[1]+'ночных'+Accor.days[2])
        self.ids.item2.title = 'Вы указали всего дней: '+Accor.days[0]+', из них не рабочих-'+Accor.days[1]+' и ночью-'+Accor.days[2]+'.'

    def premium_and_result(self, instance):
#        Accor.premium = 0.0
#        Accor.premium = float(self.ids.premium.text)/100

        Accor.result = (Accor.cat4[1] * int(Accor.days[1])) + (Accor.cat4[0] * int(Accor.days[2])) + (Accor.cat4[2] * (int(Accor.days[0])-int(Accor.days[1])-int(Accor.days[2])))
        Accor.res = round(Accor.result * 1.15,2)
        print(Accor.res)
        self.ids.resultat.text = str(Accor.res)
        self.ids.item4.title = 'Итоговая сумма: '+str(Accor.res)+' рублей.'

class AccorApp(App):
    def build(self):
        return Accor()

# run the App
if __name__ == '__main__':
    AccorApp().run()