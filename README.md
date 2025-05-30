# UI-тесты для Stellar Burgers

Проект содержит автоматизированные UI-тесты веб-приложения Stellar Burgers с использованием Page Object Pattern.

## Структура тестов

### Основные модули тестирования:
- `test_forgot_password_page.py`: Тесты восстановления пароля
  - Навигация на страницу восстановления
  - Отправка email для сброса пароля
  - Взаимодействие с элементами формы

- `test_login_page.py`: Тесты авторизации
  - Выход из системы

- `test_main_page.py`: Тесты главной страницы
  - Навигация в конструктор бургеров
  - Работа с модальными окнами ингредиентов
  - Оформление заказа (drag-and-drop)

- `test_order_feed_page.py`: Тесты ленты заказов
  - Открытие деталей заказа
  - Проверка счетчиков заказов
  - Отображение заказов в ленте

- `test_profile_page.py`: Тесты профиля пользователя
  - Навигация в профиль
  - История заказов

## Особенности реализации
- Использование `pytest` и `allure` для организации тестов и отчетности
- Применение Page Object Pattern для удобства поддержки
- Параметризованные тесты и фикстуры для повторного использования кода
- Пометка тестов, не работающих в Firefox (`@pytest.mark.skip`)
- Проверка как UI-элементов, так и URL-адресов

Тесты охватывают ключевые пользовательские сценарии работы с приложением.
