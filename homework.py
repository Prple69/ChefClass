class Chef():
    # статический атрибут
    company_name = "Кафе Матвея"
    
    def __init__(self, name, experience, workshop, hours_worked):
        # динамические атрибуты
        self.name = name
        self.experience = experience
        self.workshop = workshop
        self.hours_worked = hours_worked
    
    def about_worker(self):
        print(f'Работник - {self.name}. Опыт работы - {self.experience}')
    
    def assign_to_workshop(self, workshop_name): # статический метод
        self.workshop = workshop_name
        print(f"{self.name} направлен на {workshop_name} ")
    
    # динамический метод
    def assign_to_dish(self, dish_name):
        print(f"{self.name} поручено приготовить {dish_name} в {self.workshop}")
    
    # статический метод
    @staticmethod
    def welcome_message():
        print("Добро пожаловать в ресторан 'Кафе Матвея'! Наши повара готовы приготовить для вас лучшие блюда.")


chef = Chef('Матвей Машуков', 4, 'Горячий цех', 10)
chef.about_worker()
chef.welcome_message()
chef.assign_to_dish('борщ')
chef.assign_to_workshop('разгрузка продуктов')
chef.assign_to_dish('драники')