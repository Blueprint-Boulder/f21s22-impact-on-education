# Generated by Django 3.2.11 on 2022-02-02 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20220202_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='address',
            field=models.CharField(default='Home Address', max_length=300),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='email_address',
            field=models.EmailField(default='Email Address', max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='first_name',
            field=models.CharField(default='First Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='school_choice',
            field=models.CharField(choices=[('S0', 'No school chosen'), ('S1', 'Arapahoe Ridge High School'), ('S2', 'Boulder High School'), ('S3', 'Boulder Prep Charter'), ('S4', 'Boulder TEC'), ('S5', 'Boulder Universal'), ('S6', 'Broomfield High School'), ('S7', 'BVSD Online'), ('S8', 'Centaurus High School'), ('S9', 'Chinnook West'), ('S10', 'Fairview High School'), ('S11', 'Halcyon School'), ('S12', 'Justice High School'), ('S13', 'Monarch High School'), ('S14', 'Nederland Middle-Senior High School'), ('S15', 'New Vista High School'), ('S16', 'Peak to Peak Charter School')], default='SCHOOL0', max_length=3),
        ),
    ]
