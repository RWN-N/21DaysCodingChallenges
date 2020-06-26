from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.lang import Builder

Config.set('graphics','width','400')
Config.set('graphics','height','600')

Builder.load_string("""
<TheGrid>:
	ans : inputs
	totalsum : total
	GridLayout:
		cols:1
		size: root.width , root.height
		
		TextInput:
			id : inputs
			multiline : False
			size_hint : (0.2,0.2)
			font_size : 50
			
		TextInput:
			id : total
			multiline : False
			size_hint : (0.2,0.15)
			font_size : 50
			
		GridLayout:
			cols:4
			
			Button:
				text:'C'
				font_size : 40
				on_release:
					inputs.text = ''
					total.text  = ''
					
			Button:
				text:'()'
				font_size : 40
				on_release:
					root.brackets()
				
			Button:
				text:'Delete'
				font_size : 20
				on_release:
					root.backspace()
					
			Button:
				text:'/'
				font_size : 40
				on_release:
					inputs.text += self.text
							
			Button:
				text:'7'
				font_size : 40
				on_release:
					inputs.text += self.text
					
			Button:
				text:'8'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'9'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'*'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'4'
				font_size : 40
				on_release:
					inputs.text += self.text
					
			Button:
				text:'5'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'6'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'-'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'1'
				font_size : 40
				on_release:
					inputs.text += self.text
					
			Button:
				text:'2'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'3'
				font_size : 40
				on_release:
					inputs.text += self.text
			
			Button:
				text:'+'
				font_size : 40
				on_release:
					inputs.text += self.text
			
			Button:
				text:'+/-'
				font_size : 40
				on_release:
					root.plusmin()
					
			Button:
				text:'0'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'.'
				font_size : 40
				on_release:
					inputs.text += self.text
				
			Button:
				text:'='
				font_size : 40
				on_release:
					root.strsum(inputs.text)
				
				
""")

class TheGrid(Widget):
    def strsum(self,anss):
        if self.ans:
            try:
                self.totalsum.text = str(round(eval(anss),ndigits=5))
            except:
                self.totalsum.text = 'Error'
    def backspace(self):
        try:
            self.ans.text = self.ans.text[:len(self.ans.text)-1]
        except:
            pass

    def brackets(self):
        lst = ['+','-','*','/']
        if len(self.ans.text)==0 or self.ans.text[-1] in lst:
            self.ans.text += '('
        elif self.ans.text.count('(') > self.ans.text.count(')') and '(' in self.ans.text and self.ans.text[-1].isdigit() or self.ans.text.count('(') > self.ans.text.count(')'):
            self.ans.text += ')'
        elif self.ans.text[-1]==')' or '(' not in self.ans.text and self.ans.text[-1].isdigit()or self.ans.text[-1]=='(':
            self.ans.text += '*('
        
    def plusmin(self):
        try:
            lst = ['+','-','*','/']
            a = list(self.ans.text)[::-1]
            b = list(self.ans.text)
	
            for i in lst:
                if i in self.ans.text:
                    for j in a:
                        if j in lst:
                            lstindex = abs(a.index(j)+1-len(a))+1
                            b.insert(lstindex,'(-')                         
                            self.ans.text = ''.join(b)
                            return self.ans.text
                        
            else:
                self.ans.text = (self.ans.text[::-1]+'-(')[::-1]
        except:
            pass
                

class CalculatorApp(App):
    def build(self):
        return TheGrid()


if __name__ =='__main__':
    CalculatorApp().run()
