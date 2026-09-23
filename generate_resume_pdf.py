import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "Khushi_Kumari_Resume.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=28,
    bottomMargin=28
)

styles = getSampleStyleSheet()

# Custom styles
name_style = ParagraphStyle(
    'NameStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=22,
    alignment=1, # Center
    textColor=colors.HexColor('#000000')
)

contact_style = ParagraphStyle(
    'ContactStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=12,
    alignment=1, # Center
    textColor=colors.HexColor('#333333')
)

section_title_style = ParagraphStyle(
    'SectionTitleStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10.5,
    leading=13,
    textColor=colors.HexColor('#000000'),
    spaceBefore=6,
    spaceAfter=2,
    textTransform='uppercase'
)

item_header_left = ParagraphStyle(
    'ItemHeaderLeft',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=12,
    textColor=colors.HexColor('#000000')
)

item_header_right = ParagraphStyle(
    'ItemHeaderRight',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=12,
    alignment=2, # Right
    textColor=colors.HexColor('#000000')
)

item_sub_left = ParagraphStyle(
    'ItemSubLeft',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=11.5,
    textColor=colors.HexColor('#222222')
)

item_sub_right = ParagraphStyle(
    'ItemSubRight',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=11.5,
    alignment=2, # Right
    textColor=colors.HexColor('#000000')
)

bullet_style = ParagraphStyle(
    'BulletStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.8,
    leading=11,
    leftIndent=12,
    firstLineIndent=-8,
    spaceAfter=1.5,
    textColor=colors.HexColor('#111111')
)

skills_label_style = ParagraphStyle(
    'SkillsLabelStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.8,
    leading=11,
    textColor=colors.HexColor('#000000')
)

skills_val_style = ParagraphStyle(
    'SkillsValStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.8,
    leading=11,
    textColor=colors.HexColor('#111111')
)

story = []

# Header
story.append(Paragraph("Khushi Kumari", name_style))
story.append(Spacer(1, 2))
story.append(Paragraph("+91 7856051758 &bull; kgkhushikumari2323@gmail.com &bull; LinkedIn &bull; GitHub", contact_style))
story.append(Spacer(1, 4))

def add_section_header(title):
    story.append(Paragraph(title, section_title_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#000000"), spaceBefore=1, spaceAfter=4))

# Education
add_section_header("Education")
t_data = [[
    Paragraph("Vellore Institute of Technology, Vellore", item_header_left),
    Paragraph("May 2027", item_header_right)
]]
t = Table(t_data, colWidths=[380, 160])
t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
story.append(t)

t_data_sub = [[
    Paragraph("Bachelor of Technology in Information Technology", item_sub_left),
    Paragraph("CGPA: 7.98/10", item_sub_right)
]]
t_sub = Table(t_data_sub, colWidths=[380, 160])
t_sub.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
story.append(t_sub)
story.append(Spacer(1, 3))

# Work Experience
add_section_header("Work Experience")
t_exp = [[
    Paragraph("AI/ML Intern | <i>National Informatics Centre (NIC), Patna</i>", item_header_left),
    Paragraph("May 2026 – June 2026", item_header_right)
]]
t = Table(t_exp, colWidths=[380, 160])
t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
story.append(t)

exp_bullets = [
    "&bull; Developed a <b>Vision-Based Classroom Attendance System</b> using <b>YOLOv8</b> object detection on annotated educational datasets with 2 classes: students and teachers.",
    "&bull; Achieved <b>91.5% mAP50, 92.0% precision, and 86.3% recall</b>, automating classroom attendance monitoring through real-time object detection.",
    "&bull; Processed and annotated classroom image datasets using <b>Roboflow</b> and developed a production-ready <b>FastAPI</b>-based inference pipeline.",
    "&bull; Developed a <b>YOLOv8s-based water-body identification system</b> for village environments, classifying 4 categories: lakes, canals, handpumps, and wells.",
    "&bull; Internship Certificate"
]
for b in exp_bullets:
    story.append(Paragraph(b, bullet_style))
story.append(Spacer(1, 3))

# Projects
add_section_header("Projects")

projects = [
    ("Vision-Based Classroom Attendance System | <i>Python, PyTorch, YOLOv8, OpenCV, Flask, FastAPI</i>", "GitHub Link", [
        "&bull; Built an AI-based student head detection and counting system using custom <b>YOLOv8</b>, achieving <b>92%+ mAP50 precision</b> and 30-50ms inference time.",
        "&bull; Engineered system to handle real-world challenges like crowding, blur, low light, and varied angles while excluding teachers to accurately count students.",
        "&bull; Developed end-to-end processing pipeline supporting batch image detection and Flask/FastAPI web interface."
    ]),
    ("Cognitive Sovereignty Enforcement System | <i>Android, Kotlin, Jetpack Compose</i>", "GitHub Link", [
        "&bull; Built a notification control system using NotificationListenerService to regulate notifications across <b>15+ applications</b> through a token-based economy.",
        "&bull; Developed an <b>adaptive AI layer</b> analyzing 7-day behavioral patterns, dynamically adjusting app usage limits and reducing unnecessary notifications by <b>30%</b>.",
        "&bull; Automated daily token resets and restriction workflows using <b>WorkManager</b> for seamless background processing."
    ]),
    ("Judicial Outcome Prediction System | <i>PySpark, Hadoop, NLP, XGBoost</i>", "GitHub Link", [
        "&bull; Built a Big Data pipeline using PySpark and HDFS to process <b>10,000+ legal records</b> for judicial outcome prediction.",
        "&bull; Applied NLP techniques including tokenization and Named Entity Recognition (NER) to extract features from large-scale legal datasets.",
        "&bull; Developed an XGBoost-based prediction model achieving <b>86% accuracy</b> with explainable AI techniques for model interpretability."
    ]),
    ("Fuzzy Concept-Bottleneck Skin Cancer Diagnosis | <i>Python, Flask, OpenCV, Fuzzy Logic, AWS</i>", "GitHub Link", [
        "&bull; Developed an interpretable skin-lesion diagnosis pipeline combining segmentation, geometric features, fuzzy concepts, and concept-bottleneck modeling for explainable diagnosis.",
        "&bull; Prepared <b>2,594 ISIC 2018 image-mask pairs</b> (1,815 training, 389 validation, and 390 test samples) for lesion segmentation.",
        "&bull; Built a Flask web application with interactive ABCDE fuzzy concepts and verified deployment across <b>10 AWS services</b> including EC2, S3, RDS, IAM, CloudWatch, and API Gateway."
    ])
]

for title, link, bullets in projects:
    t_proj = [[
        Paragraph(title, item_header_left),
        Paragraph(link, item_header_right)
    ]]
    t = Table(t_proj, colWidths=[420, 120])
    t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t)
    for b in bullets:
        story.append(Paragraph(b, bullet_style))
    story.append(Spacer(1, 2))

# Skills
add_section_header("Skills")
skills_data = [
    ("Programming Languages:", "Python, Java, C++, JavaScript, SQL, Kotlin"),
    ("ML & AI:", "YOLO (YOLOv5, YOLOv8), OpenCV, scikit-learn, XGBoost, NLP, NER, PySpark, Hadoop, Pandas, NumPy"),
    ("Web Technologies:", "Node.js, Express.js, REST APIs, HTML, CSS"),
    ("Databases:", "MongoDB, SQL (MySQL), DynamoDB"),
    ("Cloud Platforms:", "AWS (EC2, S3, RDS, IAM, CloudWatch, API Gateway, Secrets Manager, Cognito, SNS)"),
    ("Tools & Frameworks:", "Git, GitHub, VS Code, Flask, FastAPI")
]

for label, val in skills_data:
    t_sk = [[
        Paragraph(label, skills_label_style),
        Paragraph(val, skills_val_style)
    ]]
    t = Table(t_sk, colWidths=[130, 410])
    t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t)
story.append(Spacer(1, 3))

# Achievements
add_section_header("Achievements")
achievements = [
    "&bull; Secured <b>1st Place</b> in Script Showdown, Yantra 2026 (VIT) &mdash; Certificate",
    "&bull; Awarded <b>Certificate of Appreciation</b> for contribution to RC Cars Building & Racing Event (SME, VIT).",
    "&bull; Successfully completed <b>Full Stack Development Virtual Internship</b> at Cognifyz Technologies."
]
for a in achievements:
    story.append(Paragraph(a, bullet_style))
story.append(Spacer(1, 3))

# Additional Information
add_section_header("Additional Information")
add_info = [
    "<b>Relevant Coursework:</b> Data Structures and Algorithms, DBMS, Operating Systems, Computer Networks, Cloud Computing, Machine Learning",
    "<b>Areas of Interest:</b> Machine Learning, Computer Vision, Artificial Intelligence, Backend Development",
    "<b>Extracurricular Activities:</b> IET-VIT & Creativity Club Member (2023 – 2024)"
]
for i in add_info:
    story.append(Paragraph("&bull; " + i, bullet_style))

doc.build(story)
print("PDF generated successfully:", pdf_path)
