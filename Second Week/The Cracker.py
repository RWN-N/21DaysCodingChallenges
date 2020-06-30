import pandas as pd
df = pd.read_excel('files.xlsx',index_col=0)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import StringProperty,ObjectProperty
from kivy.uix.popup import Popup

Config.set('graphics','width','800')
Config.set('graphics','height','600')

codee = ''
coded = ''

class P(Popup):
    text = StringProperty('')
    def cehistory(self):
        global codee
        EncodeWindow().cecode()
        codee=''
    def cdhistory(self):
        global coded
        DecodeWindow().cdcode()
        coded=''

class PP(Popup):
    etext = StringProperty('')
    dtext = StringProperty('')
    def cehistory(self):
        global codee
        EncodeWindow().cecode()
        codee=''
    def cdhistory(self):
        global coded
        DecodeWindow().cdcode()
        coded=''
    
class MainWindow(Screen):
    def mhistorybtn(self):
        global codee
        global coded
        showing = PP()
        showing.etext = codee
        showing.dtext = coded
        showing.open()
        
class EncodeWindow(Screen):
    ein,eout = ObjectProperty(None),ObjectProperty(None)
    ecode = ''
    def ehistorybtn(self):
        showing = P()
        showing.text = EncodeWindow.ecode
        showing.edtext = 'e'
        showing.open()
    def cecode(self):
        EncodeWindow.ecode = ''
    def encoding(self):
        global codee
        decodedan = [str(df.loc[i,j]) for i in df.index for j in df.columns]
        encodedan = [i+j for i in df.index for j in df.columns]
        encodedan.append('~')
        decodedan.append(' ')
        self.eout.text = ''
        try:
            if len(self.ein.text)!=0:
                for i in list(self.ein.text.lower()):
                    self.eout.text += encodedan[decodedan.index(i)]
            else:
                raise Exception
        except:
            pass
        else:
           EncodeWindow.ecode += f'>>>{self.ein.text} --> {self.eout.text}\n'
           codee += f'>>>{self.ein.text} --> {self.eout.text}\n'
class DecodeWindow(Screen):
    din,dout = ObjectProperty(None),ObjectProperty(None)
    dcode = ''
    def dhistorybtn(self):
        showing = P()
        showing.text = DecodeWindow.dcode
        showing.edtext = 'd'
        showing.open()
    def cdcode(self):
        DecodeWindow.dcode = ''
    def decoding(self):
        global coded
        decodedan = [str(df.loc[i,j]) for i in df.index for j in df.columns]
        encodedan = [i+j for i in df.index for j in df.columns]
        encodedan.append('~~')
        decodedan.append(' ')
        self.dout.text = ''
        din = self.din.text.replace('~','~~').upper()
        dinlist = [din[i:i+2]
                   for i in range(0,len(din),2)]
        try:
            if len(din)%2==0 and len(din)!=0 and '' not in din:
                for i in dinlist:
                    self.dout.text += decodedan[encodedan.index(i)].upper()
            else:
                raise Exception
        except:
            pass
        else:
            DecodeWindow.dcode += f'>>>{self.din.text} --> {self.dout.text}\n'
            coded += f'>>>{self.din.text} --> {self.dout.text}\n'
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('encodedecode.kv')

class DecodeEncode(App):
    def build(self):
        self.title = 'Cracker App'
        return kv

if __name__ == '__main__':
    DecodeEncode().run()
