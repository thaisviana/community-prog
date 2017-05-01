from .models import VideoContent, PDFContent, Category, Project, Event

VideoContent.register_admin()
PDFContent.register_admin()
Category.register_admin()
Project.register_admin()
Event.register_admin()