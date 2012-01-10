# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Quiz.footer'
        db.add_column('quiz_quiz', 'footer', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Quiz.footer'
        db.delete_column('quiz_quiz', 'footer')


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
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Quiz']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'quiz.quiz': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Quiz', '_ormbases': ['sites.Site']},
            'description': ('django.db.models.fields.TextField', [], {}),
            'footer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'site_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True', 'primary_key': 'True'})
        },
        'quiz.result': {
            'Meta': {'ordering': "['quiz', 'title']", 'object_name': 'Result'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Quiz']"}),
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
