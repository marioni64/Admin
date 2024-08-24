from django.db import models

class UserProfile(models.Model):
    user_id = models.IntegerField(primary_key=True)  # Поле для идентификатора пользователя
    name = models.CharField(max_length=255)  # Имя пользователя
    phone_number = models.CharField(max_length=15)  # Телефонный номер
    personal_code = models.CharField(max_length=20)  # Личный код
    is_active = models.BooleanField(default=True)  # Активен ли пользователь
    has_subscription = models.BooleanField(default=False)  # Имеет ли подписку
    is_staff = models.BooleanField(default=False)  # Является ли сотрудником
    subscription_end_date = models.DateField()  # Дата окончания подписки

    def __str__(self):
        return self.name

class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)  # Поле с автоинкрементом
    user_id = models.IntegerField()  # Поле для идентификатора пользователя
    service_id = models.IntegerField()  # Поле для идентификатора услуги
    visit_date = models.DateField()  # Дата визита
    status = models.IntegerField()  # Статус визита (например, завершен/отменен)

    def __str__(self):
        return f"Visit {self.visit_id} by User {self.user_id} on {self.visit_date}"


class Abonement(models.Model):
    abonement_id = models.AutoField(primary_key=True)  # ID абонемента (автоинкремент)
    name = models.CharField(max_length=255)  # Название абонемента
    description = models.TextField()  # Описание абонемента
    duration_type = models.IntegerField()  # Тип длительности (например, дни или месяцы)
    duration_unit = models.IntegerField()  # Единица длительности (например, 1 месяц, 3 месяца)
    total_sessions = models.IntegerField()  # Количество занятий
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена абонемента
    is_online = models.BooleanField(default=False)  # Онлайн или оффлайн абонемент
    discount = models.IntegerField(default=0)  # Скидка в процентах
    is_active = models.BooleanField(default=False)  # Активен ли абонемент

    def __str__(self):
        return self.name
