from django.contrib import admin
from django.contrib import admin
from users.models import Customer, Seller

admin.site.register(Seller)
admin.site.register(Customer)

# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     inlines = []

#     model = User
#     # add_form = UserCreationForm
#     # form = UserChangeForm

#     list_display = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'user_groups_display', 'is_staff']

#     add_fieldsets = (
#         *UserAdmin.add_fieldsets,
#         (
#             'Custom fields',
#             {
#                 'fields': (
#                     'phone_number',
#                     'gender',
#                     'groups',
#                 )
#             }
#         )
#     )

#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Custom fields',
#             {
#                 'fields': (
#                     'phone_number',
#                 )
#             }
#         )
#     )

#     def user_groups_display(self, user):
#         try:
#             groups = []
#             for group in user.groups.all():
#                 groups.append(group.name)
#             return ', '.join(groups)
#         except:
#             return '-'