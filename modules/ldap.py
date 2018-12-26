from django_python3_ldap.utils import format_search_filters, sync_user_relations
from django.contrib.auth.models import Group, User


# def custom_format_search_filters(ldap_fields):
    # Add in simple filters.
    # ldap_fields["memberOf"] = "BPM"
    # Call the base format callable.
    # search_filters = format_search_filters(ldap_fields)
    # Advanced: apply custom LDAP filter logic.
    # search_filters.append("(|(memberOf=groupA)(memberOf=GroupB))")
    # All done!
    # return search_filters


def custom_format_search_filters(ldap_fields):
    # Add in simple filters.
    ldap_fields["objectclass"] = "person"
    # ldap_fields["groups"] = "App_Admin"
    # Call the base format callable.
    search_filters = format_search_filters(ldap_fields)
    # Advanced: apply custom LDAP filter logic.
    # search_filters.append("(|(memberOf=groupA)(memberOf=GroupB))")
    # search_filters.append("(memberOf=CN=OrganizerEKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my)")
    # search_filters.append("(|(memberOf=CN=OrganizerEKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my)(memberOf=CN=LeadAuditorEKSA,OU=Users,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my))")
    # search_filters.append("(|(memberOf=groupA)(memberOf=GroupB))")
    # search_filters.append("(memberOf=CN=EKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my)")
    # search_filters.append("(memberOf=CN=EKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my)")
    # search_filters.append("(&(objectclass=person)(memberOf=CN=EKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my))")
    # All done!
    return search_filters


def custom_sync_user_relations(user, ldap_attributes):
    # print(str(user) + 'from custom_sync_user_relation... ')
    # print(str(user) + 'from custom_sync_user_relation... ')
    print(str(ldap_attributes['memberOf']))
    print(str(ldap_attributes['extensionattribute6']))
    print(str(ldap_attributes['displayname']))
    # for l in ldap_attributes['memberOf']:
    #     # For OrgnizerKESA members update
    #     if 'CN=OrganizerEKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my' == l:
    #         if not user.groups.filter(name='OrganizerEKSA').exists():
    #             my_group = Group.objects.get(name='OrganizerEKSA')
    #             my_group.user_set.add(user)
    #             print("You've joined the group [OrganizerEKSA] now...")
    #         else:
    #             print("You've already in : OrganizerEKSA ")

    #     # For LeadAuditorEKSA members update
    #     if 'CN=LeadAuditorEKSA,OU=Users,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my' == l:
    #         if not user.groups.filter(name='LeadAuditorEKSA').exists():
    #             my_group = Group.objects.get(name='LeadAuditorEKSA')
    #             my_group.user_set.add(user)
    #             print("You've joined the group [LeadAuditorEKSA] now...")
    #         else:
    #             print("You've already in : LeadAuditorEKSA ")


    # if user.groups.filter(name='OrganizerEKSA').exists():
    # 'CN=OrganizerEKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my'
    # my_group = Group.objects.get(name='my_group_name') 
    pass
	# 
	# search_filters = sync_user_relations(user, ldap_attributes)
    # print(str(user) + 'from custom_sync_user_relation... ')
    # print(user)
    # print(ldap_attributes)
	# print(ldap_attributes['memberOf'][0])
	# for l in ldap_attributes['memberOf']:
	# 	if 'CN=LeadAuditorEKSA,OU=Users,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my' == l:
	# 		print(l)
	# pass
    # print(user + 'from custom_sync_user_relation')