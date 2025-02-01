# Generated by Django 5.1.3 on 2025-02-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'Hindi'), ('bn', 'Bengali'), ('mr', 'Marathi'), ('ta', 'Tamil'), ('te', 'Telugu'), ('gu', 'Gujarati'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('pa', 'Punjabi'), ('ur', 'Urdu'), ('or', 'Odia'), ('as', 'Assamese'), ('gom', 'Konkani'), ('mai', 'Maithili'), ('ne', 'Nepali'), ('sa', 'Sanskrit'), ('fr', 'French'), ('de', 'German'), ('es', 'Spanish'), ('zh', 'Chinese'), ('ja', 'Japanese'), ('ru', 'Russian'), ('ar', 'Arabic'), ('it', 'Italian'), ('pt', 'Portuguese'), ('ko', 'Korean'), ('tr', 'Turkish'), ('nl', 'Dutch')], default='en', max_length=5),
        ),
        migrations.AlterField(
            model_name='faqtranslation',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'Hindi'), ('bn', 'Bengali'), ('mr', 'Marathi'), ('ta', 'Tamil'), ('te', 'Telugu'), ('gu', 'Gujarati'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('pa', 'Punjabi'), ('ur', 'Urdu'), ('or', 'Odia'), ('as', 'Assamese'), ('gom', 'Konkani'), ('mai', 'Maithili'), ('ne', 'Nepali'), ('sa', 'Sanskrit'), ('fr', 'French'), ('de', 'German'), ('es', 'Spanish'), ('zh', 'Chinese'), ('ja', 'Japanese'), ('ru', 'Russian'), ('ar', 'Arabic'), ('it', 'Italian'), ('pt', 'Portuguese'), ('ko', 'Korean'), ('tr', 'Turkish'), ('nl', 'Dutch')], max_length=5),
        ),
    ]
