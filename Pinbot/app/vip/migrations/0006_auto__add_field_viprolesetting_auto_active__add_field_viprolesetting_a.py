# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'VipRoleSetting.auto_active'
        db.add_column(u'vip_viprolesetting', 'auto_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'VipRoleSetting.attract_info'
        db.add_column(u'vip_viprolesetting', 'attract_info',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'VipRoleSetting.auto_active'
        db.delete_column(u'vip_viprolesetting', 'auto_active')

        # Deleting field 'VipRoleSetting.attract_info'
        db.delete_column(u'vip_viprolesetting', 'attract_info')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'vip.userorder': {
            'Meta': {'object_name': 'UserOrder'},
            'actual_price': ('django.db.models.fields.FloatField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'order_type'", 'to': u"orm['contenttypes.ContentType']"}),
            'item_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order_price': ('django.db.models.fields.FloatField', [], {}),
            'order_status': ('django.db.models.fields.CharField', [], {'default': "'unpay'", 'max_length': '30'}),
            'pay_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'payment_terms': ('django.db.models.fields.CharField', [], {'default': "'alipay'", 'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_orders'", 'to': u"orm['auth.User']"})
        },
        u'vip.uservip': {
            'Meta': {'object_name': 'UserVip'},
            'apply_status': ('django.db.models.fields.CharField', [], {'default': "'applying'", 'max_length': '20'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'custom_feed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'custom_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'has_sign': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vip_roles'", 'to': u"orm['auth.User']"}),
            'vip_role': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'setting_roles'", 'to': u"orm['vip.VipRoleSetting']"})
        },
        u'vip.viprolesetting': {
            'Meta': {'object_name': 'VipRoleSetting'},
            'agreement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_apply': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attract_info': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '80', 'blank': 'True'}),
            'auto_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'feed_count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'pinbot_point': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'vip_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['vip']