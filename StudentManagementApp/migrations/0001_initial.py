# Generated by Django 3.2.7 on 2021-10-02 09:33

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attandance',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('attandanceDate', models.DateTimeField(auto_now_add=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=255)),
                ('Created_at', models.DateField(auto_now_add=True)),
                ('Updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Address', models.TextField()),
                ('Created_at', models.DateField(auto_now_add=True)),
                ('Updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Student')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('subjectName', models.CharField(max_length=255)),
                ('Created_at', models.DateField(auto_now_add=True)),
                ('Updated_at', models.DateField(auto_now_add=True)),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.courses')),
                ('staffID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.staffs')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=20)),
                ('Profile', models.FileField(upload_to='')),
                ('Address', models.TextField()),
                ('Created_at', models.DateField(auto_now_add=True)),
                ('Updated_at', models.DateField(auto_now_add=True)),
                ('session_start_year', models.DateField()),
                ('session_end_year', models.DateField()),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.courses')),
            ],
        ),
        migrations.AddField(
            model_name='staffs',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='NotificationStudent',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStaff',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('leaveStatus', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('staffID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.staffs')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveReportStudent',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('leaveDate', models.CharField(max_length=255)),
                ('leaveMessage', models.TextField()),
                ('leaveStatus', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveReportStaff',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('leaveDate', models.CharField(max_length=255)),
                ('leaveMessage', models.TextField()),
                ('leaveStatus', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('staffID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.staffs')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackStudent',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('feedbackReply', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackStaff',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('feedbackReply', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('staffID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.staffs')),
            ],
        ),
        migrations.CreateModel(
            name='AttandanceReport',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('attandanceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.attandance')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='StudentManagementApp.student')),
            ],
        ),
        migrations.AddField(
            model_name='attandance',
            name='subjectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagementApp.subject'),
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Created_at', models.DateField(auto_now_add=True)),
                ('Updated_at', models.DateField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
