# Generated by Django 3.0.7 on 2020-09-20 11:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ospf',
            fields=[
                ('id_instance', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('router_id', models.GenericIPAddressField(null=True)),
                ('interface_name', models.CharField(max_length=200, null=True)),
                ('interface_area', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4294967295)])),
            ],
        ),
        migrations.CreateModel(
            name='OspfAdvArea',
            fields=[
                ('id_instance', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('interface_area', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4294967295)])),
                ('nssa', models.CharField(choices=[('no-summary', 'no-summary'), ('translate-always', 'translate-always'), ('translate-candidate', 'translate-candidate'), ('translate-never', 'translate-never')], max_length=200, null=True)),
                ('stub', models.BooleanField(null=True)),
                ('stub_no_summery', models.BooleanField(null=True)),
                ('default_cost', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(16777214)])),
                ('auth', models.BooleanField(null=True)),
                ('auth_message_digest', models.BooleanField(null=True)),
                ('virtual_link', models.GenericIPAddressField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OspfAdvGlobal',
            fields=[
                ('id_instance', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('passive_interface', models.CharField(max_length=200, null=True)),
                ('redistribute', models.CharField(choices=[('connected', 'connected'), ('bgp', 'bgp'), ('static', 'static'), ('rip', 'rip')], max_length=200, null=True)),
                ('default_metric', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(16777214)])),
                ('timers_lsa_min_interval', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600000)])),
                ('timers_throttle_lsa_all', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)])),
                ('timers_throttle_spf_delay', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600000)])),
                ('timers_throttle_spf_initial_hold_time', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600000)])),
                ('timers_throttle_spf_max_hold_time', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600000)])),
                ('ospf_abr_type', models.CharField(choices=[('cisco', 'cisco'), ('ibm', 'ibm'), ('starndard', 'standard'), ('shortcut', 'shortcut')], max_length=200, null=True)),
                ('max_mertic_router_lsa_on_startup', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)])),
                ('max_mertic_router_lsa_on_shutdown', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)])),
                ('max_mertic_router_lsa_administrative', models.BooleanField(null=True)),
                ('neighbor', models.GenericIPAddressField(null=True)),
                ('neighbor_poll_interval', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('neighbor_poll_interval_priority', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)])),
                ('ospf_rfc1583compatibility', models.BooleanField(null=True)),
                ('auto_cost_reference_bandwidth', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4294967)])),
                ('distance', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(255)])),
                ('distance_ospf_inter_area', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(255)])),
                ('distance_ospf_intra_area', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(255)])),
                ('distance_ospf_external_area', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(255)])),
                ('default_info_originate', models.BooleanField(null=True)),
                ('default_info_originate_always', models.BooleanField(null=True)),
                ('default_info_metric', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(16777214)])),
                ('default_info_metric_type', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('default_info_route_map', models.CharField(max_length=200, null=True)),
                ('log_adjacency_changes', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OspfAdvInterface',
            fields=[
                ('id_instance', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('name', models.CharField(max_length=200)),
                ('hello_interval', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('retransmit_interval', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(65535)])),
                ('transmit_delay', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('dead_interval', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('cost', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)])),
                ('priority', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(255)])),
                ('network_type', models.CharField(choices=[('broadcast', 'broadcast'), ('non-broadcast', 'non-broadcast'), ('point-to-multipoint', 'point-to-multipoint'), ('point-to-point', 'point-to-point')], max_length=19)),
                ('auth_message_digest', models.BooleanField(null=True)),
                ('auth_key', models.CharField(max_length=200, null=True)),
                ('message_digest_key', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(255)])),
                ('md5_key', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]