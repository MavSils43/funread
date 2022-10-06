# Generated by Django 4.1.1 on 2022-10-05 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.AutoField(db_column='BookID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=200)),
                ('category', models.IntegerField(blank=True, db_column='Category', null=True)),
                ('portrait', models.CharField(blank=True, db_column='Portrait', max_length=200, null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='CreatedAt', null=True)),
                ('lastupdateat', models.DateTimeField(blank=True, db_column='LastUpdateAt', null=True)),
                ('state', models.IntegerField(db_column='State')),
                ('sharedbook', models.IntegerField(blank=True, db_column='SharedBook', null=True)),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createby', to='Users.user')),
                ('updatedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updatedby', to='Users.user')),
            ],
        ),
    ]