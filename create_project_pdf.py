from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

def create_project_activity_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Заголовок
    title = Paragraph("Проектная деятельность в Губернском лицее", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))

    # Введение
    intro = Paragraph("Проектная деятельность является неотъемлемой частью образовательного процесса в Губернском лицее.", styles['Normal'])
    story.append(intro)
    story.append(Spacer(1, 12))

    # Цели проектной деятельности
    goals_title = Paragraph("Цели проектной деятельности:", styles['Heading2'])
    story.append(goals_title)
    
    goals = [
        "Развитие критического мышления",
        "Формирование навыков самостоятельной исследовательской работы",
        "Углубленное изучение предметных областей",
        "Подготовка к научной деятельности"
    ]
    
    for goal in goals:
        goal_para = Paragraph(f"• {goal}", styles['Normal'])
        story.append(goal_para)
    
    story.append(Spacer(1, 12))

    # Направления проектной деятельности
    directions_title = Paragraph("Направления проектной деятельности:", styles['Heading2'])
    story.append(directions_title)
    
    directions = [
        "Научно-исследовательские проекты",
        "Социальные проекты",
        "Инженерные и технологические проекты",
        "Творческие и междисциплинарные проекты"
    ]
    
    for direction in directions:
        direction_para = Paragraph(f"• {direction}", styles['Normal'])
        story.append(direction_para)
    
    story.append(Spacer(1, 12))

    # Результаты
    results = Paragraph("Ученики Губернского лицея ежегодно представляют свои проекты на различных конференциях, конкурсах и олимпиадах, демонстрируя высокий уровень подготовки.", styles['Normal'])
    story.append(results)

    # Создание PDF
    doc.build(story)

# Создаем PDF-файл
create_project_activity_pdf("/home/ivan/Desktop/gub_lic_site2/static/pdf/project_activity.pdf")
print("PDF-файл создан успешно!")
