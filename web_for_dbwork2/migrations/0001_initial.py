# Generated by Django 3.1.3 on 2020-12-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast_Record',
            fields=[
                ('broadcast_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('broadcast_time', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Broadcast_Record',
            },
        ),
        migrations.CreateModel(
            name='Campus_Life',
            fields=[
                ('life_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('recommend_title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author_id', models.IntegerField()),
                ('created_time', models.CharField(max_length=100)),
                ('like_num', models.IntegerField()),
                ('watch', models.IntegerField()),
                ('hot', models.IntegerField()),
            ],
            options={
                'db_table': 'Campus_Life',
            },
        ),
        migrations.CreateModel(
            name='Course_Info',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('recommend_learn_grade', models.IntegerField()),
                ('provided_time', models.CharField(max_length=50)),
                ('credits', models.FloatField()),
                ('avg_grades', models.FloatField()),
            ],
            options={
                'db_table': 'Course_Info',
            },
        ),
        migrations.CreateModel(
            name='Favorite_Record',
            fields=[
                ('favorite_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('favorite_time', models.CharField(max_length=50)),
                ('favorite_title', models.CharField(max_length=50)),
                ('favorite_content_id', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Favorite_Record',
            },
        ),
        migrations.CreateModel(
            name='Focus_Record',
            fields=[
                ('focus_record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('focus_id', models.IntegerField()),
                ('focus_time', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Focus_Record',
            },
        ),
        migrations.CreateModel(
            name='Major_In_System',
            fields=[
                ('major_id', models.IntegerField(primary_key=True, serialize=False)),
                ('major_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Major_In_System',
            },
        ),
        migrations.CreateModel(
            name='Recommend_Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=50)),
                ('total_hot', models.IntegerField()),
            ],
            options={
                'db_table': 'Recommend_Item',
            },
        ),
        migrations.CreateModel(
            name='Recommend_Item_Major',
            fields=[
                ('item_major_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('major_name', models.CharField(max_length=100)),
                ('major_desc', models.TextField()),
                ('major_representive_course_1', models.IntegerField()),
                ('major_representive_course_2', models.IntegerField()),
                ('major_representive_course_3', models.IntegerField()),
                ('major_label_1', models.CharField(max_length=100)),
                ('major_label_2', models.CharField(max_length=100)),
                ('major_label_3', models.CharField(max_length=100)),
                ('like_num', models.IntegerField()),
                ('watch', models.IntegerField()),
                ('hot', models.IntegerField()),
            ],
            options={
                'db_table': 'Recommend_Item_Major',
            },
        ),
        migrations.CreateModel(
            name='Recommend_Item_Route',
            fields=[
                ('item_route_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('route_name', models.CharField(max_length=50)),
                ('like_num', models.IntegerField()),
            ],
            options={
                'db_table': 'Recommend_Item_Route',
            },
        ),
        migrations.CreateModel(
            name='Resource_Book',
            fields=[
                ('resource_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_id', models.IntegerField()),
                ('resource_ISBN', models.CharField(max_length=100)),
                ('resource_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Resource_Book',
            },
        ),
        migrations.CreateModel(
            name='Resource_Web',
            fields=[
                ('resource_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_id', models.IntegerField()),
                ('resource_ISBN', models.CharField(max_length=100)),
                ('resource_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Resource_Web',
            },
        ),
        migrations.CreateModel(
            name='Study_Field',
            fields=[
                ('study_field_id', models.IntegerField(primary_key=True, serialize=False)),
                ('major_id', models.IntegerField()),
                ('study_field_name', models.CharField(max_length=100)),
                ('study_field_desc', models.TextField()),
                ('representive_teacher_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Study_Field',
            },
        ),
        migrations.CreateModel(
            name='Teacher_Info',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=50)),
                ('teacher_age', models.IntegerField()),
                ('teacher_rank', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Teacher_Info',
            },
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_grade', models.IntegerField()),
                ('user_major', models.IntegerField()),
                ('user_grant', models.IntegerField()),
            ],
            options={
                'db_table': 'User_Info',
            },
        ),
        migrations.CreateModel(
            name='Teacher_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('teacher_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Teacher_Course',
                'unique_together': {('course_id', 'teacher_id')},
            },
        ),
        migrations.CreateModel(
            name='StudyField_Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField()),
                ('study_field_id', models.IntegerField()),
            ],
            options={
                'db_table': 'StudyField_Teacher',
                'unique_together': {('teacher_id', 'study_field_id')},
            },
        ),
        migrations.CreateModel(
            name='Course_Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
            ],
            options={
                'db_table': 'Course_Sequence',
                'unique_together': {('route_id', 'course_id')},
            },
        ),
        migrations.CreateModel(
            name='Course_Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('major_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Course_Major',
                'unique_together': {('course_id', 'major_id')},
            },
        ),
    ]