class Vacancy:
    __slots__ = ['name', 'url', 'salary', 'description']

    def __init__(self, name: str, url: str, salary: int, description: str):
        # Валидация имени
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название вакансии должно быть непустой строкой")

        # Валидация URL
        if not isinstance(url, str) or not url.strip() or not url.startswith(('http://', 'https://')):
            raise ValueError("URL должен быть непустой строкой и начинаться с http:// или https://")

        # Валидация зарплаты
        if not isinstance(salary, (int, type(None))):
            raise TypeError("Зарплата должна быть целым числом или None")
        if isinstance(salary, int) and salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")

        # Валидация описания
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Описание должно быть непустой строкой")

        self.name = name
        self.url = url
        self.salary = salary if salary else 0
        self.description = description

    def to_dict(self):
        """Возвращает представление объекта в виде словаря"""
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary if self.salary != 0 else 'Зарплата не указана',
            'description': self.description
        }

    def __eq__(self, other):
        """Проверка на равенство зарплат"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other):
        """Проверка, что текущая зарплата меньше другой"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary