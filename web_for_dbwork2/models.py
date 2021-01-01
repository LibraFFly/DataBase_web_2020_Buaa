from django.db import models


# Create your models here.

class Recommend_Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    total_hot = models.IntegerField()

    class Meta:
        db_table = "Recommend_Item"


class User_Info(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_grade = models.IntegerField()
    user_major = models.CharField(max_length=100)
    user_grant = models.IntegerField()

    class Meta:
        db_table = "User_Info"


class Broadcast_Record(models.Model):
    broadcast_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    broadcast_time = models.DateField()
    title = models.CharField(max_length=50)

    class Meta:
        db_table = "Broadcast_Record"


class Favorite_Record(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    favorite_time = models.DateField()
    favorite_title = models.CharField(max_length=50)
    favorite_content_id = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=20)

    class Meta:
        db_table = "Favorite_Record"


class Focus_Record(models.Model):
    focus_record_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    focus_id = models.IntegerField()
    focus_time = models.DateField()

    class Meta:
        db_table = "Focus_Record"


class Recommend_Item_Route(models.Model):
    item_route_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    route_name = models.CharField(max_length=50)
    like_num = models.IntegerField()
    watch = models.IntegerField()
    hot = models.IntegerField()

    class Meta:
        db_table = "Recommend_Item_Route"


class Course_Info(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    recommend_learn_grade = models.IntegerField()
    provided_time = models.DateField()
    credits = models.FloatField()
    avg_grades = models.FloatField()

    class Meta:
        db_table = "Course_Info"


class Resource_Web(models.Model):
    resource_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    resource_ISBN = models.CharField(max_length=100)
    resource_name = models.CharField(max_length=100)

    class Meta:
        db_table = "Resource_Web"


class Resource_Book(models.Model):
    resource_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    resource_ISBN = models.CharField(max_length=100)
    resource_name = models.CharField(max_length=100)

    class Meta:
        db_table = "Resource_Book"


class Teacher_Info(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=50)
    teacher_age = models.IntegerField()
    teacher_rank = models.CharField(max_length=50)

    class Meta:
        db_table = "Teacher_Info"


class Recommend_Item_Major(models.Model):
    item_major_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    major_name = models.CharField(max_length=100)
    major_title = models.TextField()
    major_desc = models.TextField()
    major_representive_course_1 = models.IntegerField()
    major_representive_course_2 = models.IntegerField()
    major_representive_course_3 = models.IntegerField()
    major_label_1 = models.CharField(max_length=100)
    major_label_2 = models.CharField(max_length=100)
    major_label_3 = models.CharField(max_length=100)
    like_num = models.IntegerField()
    watch = models.IntegerField()
    hot = models.IntegerField()

    class Meta:
        db_table = "Recommend_Item_Major"


class Major_In_System(models.Model):
    major_id = models.AutoField(primary_key=True)
    major_name = models.CharField(max_length=100)

    class Meta:
        db_table = "Major_In_System"


class Study_Field(models.Model):
    study_field_id = models.AutoField(primary_key=True)
    major_id = models.IntegerField()
    study_field_name = models.CharField(max_length=100)
    study_field_desc = models.TextField()
    representive_teacher_id = models.IntegerField()

    class Meta:
        db_table = "Study_Field"


class Course_Sequence(models.Model):
    route_id = models.IntegerField()
    course_id = models.IntegerField()
    sequence_number = models.IntegerField()

    class Meta:
        db_table = "Course_Sequence"
        unique_together = ("route_id", "course_id")


class Teacher_Course(models.Model):
    course_id = models.IntegerField()
    teacher_id = models.IntegerField()

    class Meta:
        db_table = "Teacher_Course"
        unique_together = ("course_id", "teacher_id")


class StudyField_Teacher(models.Model):
    teacher_id = models.IntegerField()
    study_field_id = models.IntegerField()

    class Meta:
        db_table = "StudyField_Teacher"
        unique_together = ("teacher_id", "study_field_id")


class Course_Major(models.Model):
    course_id = models.IntegerField()
    major_id = models.IntegerField()

    class Meta:
        db_table = "Course_Major"
        unique_together = ("course_id", "major_id")


class Campus_Life(models.Model):
    life_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    recommend_title = models.CharField(max_length=100)
    content = models.TextField()
    author_id = models.IntegerField()
    created_time = models.DateField()
    like_num = models.IntegerField()
    watch = models.IntegerField()
    hot = models.IntegerField()

    class Meta:
        db_table = "Campus_Life"


class Grade_Num(models.Model):
    id = models.AutoField(primary_key=True)
    num = models.IntegerField(default=0)

    class Meta:
        db_table = "Grade_Num"
