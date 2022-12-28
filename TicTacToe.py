import kivy
import weakref
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
Builder.load_file("TicTacToe.kv")

turn = 0
def check_answers(location):
    for i in range(1,3):
        if location[0][0] == i and location[1][0] == i and location[2][0] == i:
            return i
        elif location[0][1] == i and location[1][1] == i and location[2][1] == i:
            return i
        elif location[0][2] == i and location[1][2] == i and location[2][2] == i:
            return i
        elif location[0][0] == i and location[0][1] == i and location[0][2] == i:
            return i
        elif location[1][0] == i and location[1][1] == i and location[1][2] == i:
            return i
        elif location[2][0] == i and location[2][1] == i and location[2][2] == i:
            return i
        elif location[0][0] == i and location[1][1] == i and location[2][2] == i:
            return i
        elif location[0][2] == i and location [1][1] == i and location[2][0] == i:
            return i
    return 0
class BoxButton(Button):
    position = f'0_0'
    
    def show(self):
        global turn 

        update_location = TicTacToeScreen()

    
        if turn % 2 == 0 and (self.text != 'x' and self.text != 'o'):
            update_location.location[int(self.position[0])][int(self.position[-1])] = 1
            self.text = "o"
            self.font_size = 50
            turn += 1
        elif turn % 2 != 0 and (self.text != 'x' and self.text != 'o'):
            update_location.location[int(self.position[0])][int(self.position[-1])] = 2
            self.text = "x"
            self.font_size= 50
            turn  += 1
        else:
            print("ช่องนี้ถูกเลือกแล้ว")

        if check_answers(update_location.location) == 1:
            pop = Popup(title='Announce!!',
                content=Label(text='o winner',font_size=50),
                size_hint=(None, None), size=(400, 400))
            pop.open()
            
        elif check_answers(update_location.location) == 2:
            pop = Popup(title='Announce!!',
                content=Label(text='x winner',font_size=50),
                size_hint=(None, None), size=(400, 400))
            pop.open()
            
        

class TicTacToeScreen(BoxLayout):
    location = [[0,0,0],[0,0,0],[0,0,0]]
    def create_table(self):

        for i in range(9):
            box = BoxButton(text=str(i))
            box.position = f'{i // 3}_{i% 3}'
            self.ids['gameTable'].add_widget(box)

    def clear(self):
        global turn
        turn = 0
        self.ids['gameTable'].clear_widgets()

            
        
    

class MyGame(App):
    def build(self):
        return TicTacToeScreen()

if __name__ == "__main__":
    MyGame().run()