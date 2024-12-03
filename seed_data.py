from app import app, db
from models import News, Document, MenuItem

def seed_menu_items():
    # Очистка существующих пунктов меню
    MenuItem.query.delete()
    
    # Главное меню
    main_menu_items = [
        {'title': 'Главная', 'url': '/', 'position': 1, 'menu_type': 'main'},
        {'title': 'О лицее', 'url': '/about', 'position': 2, 'menu_type': 'main'},
        {'title': 'Новости', 'url': '/news', 'position': 3, 'menu_type': 'main'},
        {'title': 'Учеба', 'url': '/study', 'position': 4, 'menu_type': 'main'},
        {'title': 'Поступление', 'url': '/admission', 'position': 5, 'menu_type': 'main'},
        {'title': 'Контакты', 'url': '/contacts', 'position': 6, 'menu_type': 'main'},
    ]
    
    # Боковое меню
    side_menu_items = [
        {'title': 'Расписание', 'url': '/schedule', 'position': 1, 'menu_type': 'side'},
        {'title': 'Электронный дневник', 'url': '/diary', 'position': 2, 'menu_type': 'side'},
        {'title': 'Достижения', 'url': '/achievements', 'position': 3, 'menu_type': 'side'},
        {'title': 'Внеурочная деятельность', 'url': '/activities', 'position': 4, 'menu_type': 'side'},
        {'title': 'Родителям', 'url': '/parents', 'position': 5, 'menu_type': 'side'},
        {'title': 'Учителям', 'url': '/teachers', 'position': 6, 'menu_type': 'side'},
    ]
    
    # Добавление пунктов меню в базу данных
    for item in main_menu_items + side_menu_items:
        menu_item = MenuItem(**item)
        db.session.add(menu_item)
    
    db.session.commit()

def seed_news():
    # Очистка существующих новостей
    News.query.delete()
    
    news_items = [
        {
            'title': 'День открытых дверей в лицее',
            'content': 'Приглашаем будущих учеников и их родителей на день открытых дверей! Вы сможете познакомиться с нашими учителями, узнать об образовательных программах и посетить мастер-классы.',
            'date_posted': '2024-01-15'
        },
        {
            'title': 'Победа в олимпиаде по математике',
            'content': 'Поздравляем наших учеников с победой в региональном этапе олимпиады по математике! Три ученика лицея заняли призовые места.',
            'date_posted': '2024-01-10'
        },
        {
            'title': 'Новый набор в IT-классы',
            'content': 'Открыт набор в специализированные IT-классы на следующий учебный год. Приглашаем талантливых учеников, увлеченных информационными технологиями.',
            'date_posted': '2024-01-05'
        }
    ]
    
    for item in news_items:
        news = News(title=item['title'], content=item['content'])
        db.session.add(news)
    
    db.session.commit()

def seed_documents():
    # Очистка существующих документов
    Document.query.delete()
    
    documents = [
        {
            'title': 'Правила приема в лицей',
            'description': 'Информация о порядке поступления, необходимых документах и сроках подачи заявлений',
            'category': 'admission'
        },
        {
            'title': 'Образовательная программа',
            'description': 'Основная образовательная программа лицея',
            'category': 'education'
        },
        {
            'title': 'Расписание занятий',
            'description': 'Актуальное расписание занятий на текущий семестр',
            'category': 'schedule'
        },
        {
            'title': 'Список учебников',
            'description': 'Перечень учебников и учебных пособий на текущий учебный год',
            'category': 'education'
        }
    ]
    
    for doc in documents:
        document = Document(**doc)
        db.session.add(document)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_menu_items()
        seed_news()
        seed_documents()
