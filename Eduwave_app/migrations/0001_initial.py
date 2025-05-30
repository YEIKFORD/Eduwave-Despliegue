# Generated by Django 5.1.3 on 2025-04-12 01:54

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ambiente', models.CharField(max_length=100, unique=True)),
                ('estado', models.CharField(choices=[('A', 'Apto'), ('N', 'No apto')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_DANE', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramaFormacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad', models.CharField(choices=[('V', 'Virtual'), ('P', 'Presencial')], default='P', max_length=1)),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2, unique=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAmbiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=450)),
            ],
        ),
        migrations.CreateModel(
            name='TipoNovedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_adquisicion', models.DateField()),
                ('num_placa_almacen', models.CharField(max_length=45)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=20)),
                ('estado', models.CharField(choices=[('A', 'Apto'), ('N', 'No apto')], default='A', max_length=1)),
                ('ambiente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mobiliarios', to='Eduwave_app.ambiente')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='CentroFormacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_ficha', models.CharField(max_length=45, unique=True)),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.programaformacion')),
            ],
        ),
        migrations.CreateModel(
            name='Red',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('centro_formacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.centroformacion')),
            ],
        ),
        migrations.AddField(
            model_name='programaformacion',
            name='red',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.red'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='regional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.regional'),
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('centro_formacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.centroformacion')),
            ],
        ),
        migrations.AddField(
            model_name='ambiente',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.sede'),
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='ambiente',
            name='tipo_ambiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.tipoambiente'),
        ),
        migrations.CreateModel(
            name='Usuario',
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
                ('tipo_doc', models.CharField(choices=[('TI', 'Tarjeta de identidad'), ('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('OT', 'Otro')], default='CC', max_length=2)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('numero_doc', models.CharField(default='', max_length=30, unique=True)),
                ('ficha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Eduwave_app.ficha')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.rol')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=450)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('evidencia', models.FileField(blank=True, null=True, upload_to='evidencias/')),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aprobado'), ('C', 'Cerrado')], default='P', max_length=1)),
                ('tipo_falta', models.CharField(blank=True, choices=[('Leve', 'Leve'), ('Grave', 'Grave'), ('Gravisima', 'Gravísima')], max_length=10, null=True)),
                ('ambiente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Eduwave_app.ambiente')),
                ('tipo_novedad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.tiponovedad')),
                ('creado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='novedades_creadas', to=settings.AUTH_USER_MODEL)),
                ('usuarios', models.ManyToManyField(blank=True, related_name='novedades_aprendiz', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
