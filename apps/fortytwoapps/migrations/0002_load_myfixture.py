from django.db import migrations, models

class Migration(migrations.Migration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        from django.core.management import call_command
        call_command("loaddata", "apps/fortytwoapps/fixtures/initial_data.json")

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'fortytwoapps.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '500',
                    'null': 'True', 'blank': 'True'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100',
                      'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '100',
                       'null': 'True', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '100',
                         'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'othercontacts': ('django.db.models.fields.CharField', [], {'max_length': '500',
                              'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': 
                      '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fortytwoapps']
    symmetrical = True
