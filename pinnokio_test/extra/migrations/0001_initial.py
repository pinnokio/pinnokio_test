# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestEntry'
        db.create_table('extra_requestentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('method', self.gf('django.db.models.fields.CharField')(default='GET', max_length=10)),
            ('get_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('post_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('meta_data', self.gf('django.db.models.fields.TextField')()),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('creation_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('extra', ['RequestEntry'])

    def backwards(self, orm):
        # Deleting model 'RequestEntry'
        db.delete_table('extra_requestentry')

    models = {
        'extra.requestentry': {
            'Meta': {'ordering': "['-creation_time']", 'object_name': 'RequestEntry'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'get_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_data': ('django.db.models.fields.TextField', [], {}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'GET'", 'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'post_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['extra']