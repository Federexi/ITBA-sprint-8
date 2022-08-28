# Generated by Django 4.1 on 2022-08-28 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0005_sucursal'),
        ('Clientes', '0003_empleado_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('postal_zip', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('country', models.TextField()),
                ('branch_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Prestamos.sucursal')),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Clientes.cliente')),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Clientes.empleado')),
            ],
            options={
                'db_table': 'direccion',
            },
        ),
    ]