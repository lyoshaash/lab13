from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from my_calculator_package.calculations import RoomCalculation
from my_calculator_package.docx_saver import DocxSaver
import os


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.length_input = TextInput(hint_text='Длина комнаты (м)')
        self.width_input = TextInput(hint_text='Ширина комнаты (м)')
        self.height_input = TextInput(hint_text='Высота комнаты (м)')
        self.num_apartments_input = TextInput(hint_text='Количество квартир (необязательно)', text='1')
        self.num_floors_input = TextInput(hint_text='Количество этажей (необязательно)', text='1')

        self.add_widget(self.length_input)
        self.add_widget(self.width_input)
        self.add_widget(self.height_input)
        self.add_widget(self.num_apartments_input)
        self.add_widget(self.num_floors_input)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

        self.calculate_button = Button(text='Рассчитать')
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)

        self.save_button = Button(text='Сохранить в DOCX')
        self.save_button.bind(on_press=self.save_results)
        self.add_widget(self.save_button)

    def calculate(self, instance):
        length = float(self.length_input.text)
        width = float(self.width_input.text)
        height = float(self.height_input.text)
        num_apartments = float(self.num_apartments_input.text or 1)
        num_floors = float(self.num_floors_input.text or 1)

        calculation = RoomCalculation(length, width, height, num_apartments, num_floors)
        volume = calculation.calculate_volume()
        heat_power = calculation.calculate_heat_power()

        self.result_label.text = (f"Объем помещения: {volume:.2f} куб. м\n"
                                  f"Тепловая мощность для обогрева помещения: {heat_power:.2f} кВт")

    def save_results(self, instance):
        length = float(self.length_input.text)
        width = float(self.width_input.text)
        height = float(self.height_input.text)
        num_apartments = float(self.num_apartments_input.text or 1)
        num_floors = float(self.num_floors_input.text or 1)

        calculation = RoomCalculation(length, width, height, num_apartments, num_floors)
        volume = calculation.calculate_volume()
        heat_power = calculation.calculate_heat_power()

        # Укажите путь для сохранения файла
        save_path = os.path.join(os.getcwd(), 'Результаты расчетов.docx')
        DocxSaver.save_results_to_docx(length, width, height, num_apartments, num_floors, volume, heat_power, save_path)
        self.result_label.text += "\nРезультаты сохранены в файл 'Результаты расчетов.docx'"


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()
