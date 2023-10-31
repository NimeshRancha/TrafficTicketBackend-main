from django.db import migrations
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from api.models import (
    Admin,
    Person,
    Driver, 
    VehicleOwner,
    Vehicle,
    Fine,
    ViolationType,
    Accident,
    Message,
    PoliceOfficer,
    Violation,
    Suggestion,
    Schedule,
    VehicleAccident,
    CameraLocation,
    OfficerLocation
)

# def add_permissions(group,model_permissions):
# Loop through the model_permissions dictionary and add the permissions to the group
    # for model, permission_codenames in model_permissions.items():
    #     content_type = ContentType.objects.get_for_model(model)
    #     for codename in permission_codenames:
    #         permission = Permission.objects.get(content_type=content_type, codename=codename)
    #         group.permissions.add(permission)

def create_groups(apps, schema_editor):
    # create officer group
    officer_group, created = Group.objects.get_or_create(name='officer')
    officer_permissions = {
        Accident: ['view_accident','add_accident'],
        Driver: ['view_driver'],
        Fine: ['view_fine','add_fine'],
        Message: ['view_message','add_message'],
        Person: ['view_person'],
        PoliceOfficer: ['view_policeofficer'],
        Schedule: ['view_schedule'],
        Vehicle: ['view_vehicle'],
        VehicleAccident: ['view_vehicleaccident','add_vehicleaccident'],
        VehicleOwner: ['view_vehicleowner'],
    }
    # add_permissions(officer_group,officer_permissions)
    officer_group.save()

    # create driver group
    driver_group, created = Group.objects.get_or_create(name='driver')
    driver_permissions = {
        Accident: ['view_accident','add_accident'],
        Driver: ['view_driver','add_driver'],
        Fine: ['view_fine'],
        Person: ['view_person','add_person'],
        Suggestion: ['view_suggestion','add_suggestion'],
        Vehicle: ['view_vehicle','add_vehicle'],
        VehicleAccident: ['view_vehicleaccident','add_vehicleaccident'],
        VehicleOwner: ['view_vehicleowner','add_vehicleowner'],
        User: ['view_user','add_user'],
    }
    # add_permissions(driver_group, driver_permissions)
    driver_group.save()

    # create admin group
    admin_group, created = Group.objects.get_or_create(name='admin')
    admin_permissions = {
        Accident: ['view_accident'],
        Admin: ['view_admin'],
        #CameraLocation: ['view_cameralocation','add_cameralocation'],
        Driver: ['view_driver'],
        Fine: ['view_fine'],
        #OfficerLocation: ['view_officerlocation','add_officerlocation'],
        Person: ['view_person','add_person'],
        PoliceOfficer: ['view_policeofficer','add_policeofficer'],
        Schedule: ['view_schedule','add_schedule'],
        Vehicle: ['view_vehicle'],
        VehicleAccident: ['view_vehicleaccident'],
        VehicleOwner: ['view_vehicleowner'],
        Violation: ['view_violation'],
        ViolationType: ['view_violationtype'],
        User: ['view_user','add_user'],
    }
    # add_permissions(admin_group, admin_permissions)
    admin_group.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_cameralocation_police_station_and_more'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
