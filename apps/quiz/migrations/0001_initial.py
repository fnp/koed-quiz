from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('ordering', models.SmallIntegerField()),
            ],
            options={
                'ordering': ['question', 'ordering'],
                'verbose_name': 'answer',
                'verbose_name_plural': 'answers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('ordering', models.SmallIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['quiz', 'ordering'],
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('site_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sites.Site', on_delete=models.CASCADE)),
                ('description', models.TextField()),
                ('footer', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'quiz',
                'verbose_name_plural': 'quizzes',
            },
            bases=('sites.site',),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('quiz', models.ForeignKey(to='quiz.Quiz', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['quiz', 'title'],
                'verbose_name': 'result',
                'verbose_name_plural': 'results',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('quiz', 'slug'), ('quiz', 'ordering')]),
        ),
        migrations.AddField(
            model_name='answer',
            name='go_to',
            field=models.ForeignKey(related_name='go_tos', blank=True, to='quiz.Question', null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='quiz.Question', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='result',
            field=models.ForeignKey(blank=True, to='quiz.Result', null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
