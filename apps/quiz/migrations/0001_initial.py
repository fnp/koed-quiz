# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Result'
        db.create_table('quiz_result', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('quiz', ['Result'])

        # Adding model 'Question'
        db.create_table('quiz_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('ordering', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('quiz', ['Question'])

        # Adding unique constraint on 'Question', fields ['quiz', 'slug']
        db.create_unique('quiz_question', ['quiz_id', 'slug'])

        # Adding unique constraint on 'Question', fields ['quiz', 'ordering']
        db.create_unique('quiz_question', ['quiz_id', 'ordering'])

        # Adding model 'Answer'
        db.create_table('quiz_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Question'])),
            ('go_to', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='go_tos', null=True, to=orm['quiz.Question'])),
            ('result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Result'], null=True, blank=True)),
            ('ordering', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('quiz', ['Answer'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Question', fields ['quiz', 'ordering']
        db.delete_unique('quiz_question', ['quiz_id', 'ordering'])

        # Removing unique constraint on 'Question', fields ['quiz', 'slug']
        db.delete_unique('quiz_question', ['quiz_id', 'slug'])

        # Deleting model 'Result'
        db.delete_table('quiz_result')

        # Deleting model 'Question'
        db.delete_table('quiz_question')

        # Deleting model 'Answer'
        db.delete_table('quiz_answer')


    models = {
        'quiz.answer': {
            'Meta': {'ordering': "['question', 'ordering']", 'object_name': 'Answer'},
            'go_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'go_tos'", 'null': 'True', 'to': "orm['quiz.Question']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.SmallIntegerField', [], {}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Question']"}),
            'result': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Result']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'quiz.question': {
            'Meta': {'ordering': "['quiz', 'ordering']", 'unique_together': "[['quiz', 'slug'], ['quiz', 'ordering']]", 'object_name': 'Question'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.SmallIntegerField', [], {}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'quiz.quiz': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Quiz', 'db_table': "'django_site'", '_ormbases': ['sites.Site'], 'proxy': 'True'}
        },
        'quiz.result': {
            'Meta': {'object_name': 'Result'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['quiz']
