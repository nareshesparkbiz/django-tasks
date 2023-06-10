# Generated by Django 4.2.2 on 2023-06-08 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_form_app', '0014_selectmaster_alter_educationdetail_student_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationdetail',
            name='course_name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='WorkExperiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_form_app.basicdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(max_length=100)),
                ('star', models.CharField(max_length=100)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_form_app.basicdetails')),
            ],
        ),
        migrations.CreateModel(
            name='RefranceContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_name', models.CharField(max_length=100)),
                ('ref_contact', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=50)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_form_app.basicdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefered_location', models.CharField(max_length=100)),
                ('expected_ctc', models.CharField(max_length=100)),
                ('current_ctc', models.CharField(max_length=100)),
                ('notice_period', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=100)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_form_app.basicdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('read_status', models.CharField(max_length=10)),
                ('write_status', models.CharField(max_length=10)),
                ('speak_status', models.CharField(max_length=10)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_form_app.basicdetails')),
            ],
        ),
    ]
