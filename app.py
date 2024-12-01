from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime
import os
from werkzeug.utils import secure_filename
import logging
from flask_login import login_required
from auth import User, init_login_manager, auth_bp
import dotenv
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

from extensions import db
from models import News, Document, MenuItem

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Инициализируем расширения
db.init_app(app)

def get_menu_items(menu_type):
    return MenuItem.query.filter_by(menu_type=menu_type, parent_id=None).order_by(MenuItem.position).all()

@app.context_processor
def inject_menus():
    return {
        'main_menu': get_menu_items('main'),
        'side_menu': get_menu_items('side')
    }

@app.route('/')
def index():
    latest_news = News.query.order_by(News.date_posted.desc()).limit(10).all()
    return render_template('index.html', latest_news=latest_news)

@app.route('/news')
def news_list():
    page = request.args.get('page', 1, type=int)
    news = News.query.order_by(News.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('news_list.html', news=news)

@app.route('/news/<int:news_id>')
def news_detail(news_id):
    news_item = News.query.get_or_404(news_id)
    return render_template('news_detail.html', news=news_item)

@app.route('/documents')
def documents():
    documents_list = Document.query.all()
    return render_template('documents.html', documents=documents_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admission')
def admission():
    return render_template('admission.html')

@app.route('/admission-conditions')
def admission_conditions():
    return render_template('admission_conditions.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/organization_info')
def organization_info():
    return render_template('organization_info.html')

@app.route('/main_info')
def main_info():
    return render_template('main_info.html')

@app.route('/structure')
def structure():
    return render_template('structure.html')

@app.route('/management')
def management():
    return render_template('management.html')

@app.route('/pedagogical_staff')
def pedagogical_staff():
    return render_template('pedagogical_staff.html')

@app.route('/material_support')
def material_support():
    return render_template('material_support.html')

@app.route('/paid_services')
def paid_services():
    return render_template('paid_services.html')

@app.route('/financial_activity')
def financial_activity():
    return render_template('financial_activity.html')

@app.route('/vacant_places')
def vacant_places():
    return render_template('vacant_places.html')

@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html')

@app.route('/international_cooperation')
def international_cooperation():
    return render_template('international_cooperation.html')

@app.route('/food_organization')
def food_organization():
    return render_template('food_organization.html')

@app.route('/admission-documents')
def admission_documents():
    return render_template('admission_documents.html')

@app.route('/payment-details')
def payment_details():
    return render_template('payment_details.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/open-day')
def open_day():
    return render_template('open_day.html')

@app.route('/project-activity')
def project_activity():
    return render_template('project_activity.html')

import os
from flask import send_from_directory, abort

# Путь к директории с PDF-файлами
PDF_DIRECTORY = os.path.join(os.path.dirname(__file__), 'static', 'pdf')

@app.route('/download/project-pdf')
def download_project_pdf():
    filename = 'project_activity.pdf'
    filepath = os.path.join(PDF_DIRECTORY, filename)
    
    # Проверка существования файла
    if not os.path.exists(filepath):
        # Создаем директорию, если она не существует
        os.makedirs(PDF_DIRECTORY, exist_ok=True)
        
        # Создаем пустой PDF-файл, если его нет
        with open(filepath, 'wb') as f:
            f.write(b'%PDF-1.5\n')  # Минимальный PDF-заголовок
    
    try:
        return send_from_directory(
            PDF_DIRECTORY, 
            filename, 
            as_attachment=True,
            download_name='Проектная_деятельность.pdf'
        )
    except FileNotFoundError:
        abort(404)

app.register_blueprint(auth_bp, url_prefix='/auth')
login_manager = init_login_manager(app)

@app.route('/publish_news', methods=['GET', 'POST'])
@login_required
def publish_news():
    if request.method == 'POST':
        try:
            title = request.form['title']
            content = request.form['content']
            image = request.files['image']

            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(image_path)
                image_url = f'/static/uploads/{filename}'
            else:
                image_url = None

            new_news = News(title=title, content=content, image_url=image_url)
            db.session.add(new_news)
            db.session.commit()

            return redirect(url_for('news'))
        except Exception as e:
            logging.error(f'Error publishing news: {e}')
            return render_template('publish_news.html', error=str(e))

    return render_template('publish_news.html')

@app.route('/delete_news', methods=['GET', 'POST'])
@login_required
def delete_news():
    news_list = News.query.all()
    if request.method == 'POST':
        news_id = request.form.get('news_id')
        news_to_delete = News.query.get(news_id)
        if news_to_delete:
            db.session.delete(news_to_delete)
            db.session.commit()
            return redirect(url_for('delete_news'))
    return render_template('delete_news.html', news_list=news_list)

# Создаем все таблицы перед запуском приложения
with app.app_context():
    # Проверяем, существует ли файл базы данных
    if not os.path.exists('site.db'):
        db.create_all()
        # Создаем первого пользователя, если его нет
        if not User.query.filter_by(username='admin').first():
            admin_user = User(username='admin')
            admin_user.set_password('gubernsky2024')
            db.session.add(admin_user)
            db.session.commit()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
