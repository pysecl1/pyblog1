# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blogs'
        db.create_table('blog_main_blogs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('logo', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(default='today')),
        ))
        db.send_create_signal('blog_main', ['Blogs'])

        # Adding model 'Users'
        db.create_table('blog_main_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('b_day', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('blog_main', ['Users'])

        # Adding model 'Posts'
        db.create_table('blog_main_posts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('blog_main', ['Posts'])


    def backwards(self, orm):
        # Deleting model 'Blogs'
        db.delete_table('blog_main_blogs')

        # Deleting model 'Users'
        db.delete_table('blog_main_users')

        # Deleting model 'Posts'
        db.delete_table('blog_main_posts')


    models = {
        'blog_main.blogs': {
            'Meta': {'object_name': 'Blogs'},
            'created_at': ('django.db.models.fields.DateField', [], {'default': "'today'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog_main.posts': {
            'Meta': {'object_name': 'Posts'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'blog_main.users': {
            'Meta': {'object_name': 'Users'},
            'b_day': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog_main']