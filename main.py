from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Ajouter un label
        self.status_label = Label(text='Bienvenue dans l\'application de réservation de trajets.')
        layout.add_widget(self.status_label)

        # Ajouter un bouton pour réserver un trajet
        reserve_button = Button(text='Réserver un trajet')
        reserve_button.bind(on_press=self.reserve_ride)
        layout.add_widget(reserve_button)

        return layout

    def reserve_ride(self, instance):
        self.status_label.text = 'Réservation en cours...'

if __name__ == '__main__':
    MainApp().run()
