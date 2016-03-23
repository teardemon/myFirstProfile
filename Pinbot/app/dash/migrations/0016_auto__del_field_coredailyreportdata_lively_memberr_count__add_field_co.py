# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CoreDailyReportData.lively_memberr_count'
        db.delete_column(u'dash_coredailyreportdata', 'lively_memberr_count')

        # Adding field 'CoreDailyReportData.lively_member_count'
        db.add_column(u'dash_coredailyreportdata', 'lively_member_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'CoreDailyReportData.lively_memberr_count'
        db.add_column(u'dash_coredailyreportdata', 'lively_memberr_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'CoreDailyReportData.lively_member_count'
        db.delete_column(u'dash_coredailyreportdata', 'lively_member_count')


    models = {
        u'dash.coredailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'CoreDailyReportData'},
            'active_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entered_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lively_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lively_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'repeat_visit_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dash.partnerdailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'PartnerDailyReportData'},
            'accept_task_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accept_task_user_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accusation_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accusation_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'all_extra_reward_coin_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'all_reward_coin_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'do_task_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'do_task_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entered_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entered_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'interviewed_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'resume_download_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_download_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_viewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_viewed_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_accedpted_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_accedpted_count_contrast': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'task_accedpted_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_viewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'today_commend_and_check_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'today_commend_and_download_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'today_extra_reward_coin_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'today_reward_coin_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upload_resume_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upload_resume_total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'dash.pinbotdailyreport': {
            'Meta': {'object_name': 'PinbotDailyReport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pay_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'register_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {}),
            'total_pay_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'uv': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'dash.resumedailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'ResumeDailyReportData'},
            'company_card_send_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entered_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'resume_commends_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_down_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resume_view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'dash.userdailyreportdata': {
            'Meta': {'ordering': "['-report_date']", 'object_name': 'UserDailyReportData'},
            'all_total_active_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lively_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'month_lively_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'month_repeat_visit_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_active_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_experience_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_manual_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_register_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_self_member_a_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_self_member_b_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_self_member_c_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_self_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'repeat_visit_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'report_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'total_experience_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_manual_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_register_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_self_member_a_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_self_member_b_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_self_member_c_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_self_member_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'uv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_lively_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_repeat_visit_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['dash']