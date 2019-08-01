from django.urls import path
from . import views


app_name = 'db'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.plate_list, name='index'),

    path('plate<int:plate_id>/', views.plate_view, name='plate'),
    path('add/', views.plate_add, name='plate_add'),
    path('export/plate<int:plate_id>/', views.plate_export, name='plate_export'),
    path('delete/plate<int:plate_id>/', views.plate_delete, name='plate_delete'),
    path('delete/plate<int:plate_id>/<int:well_id>', views.well_delete, name='well_delete'),
    path('update/plate<int:plate_id>/<int:well_id>', views.well_update, name='well_update'),

    path('plate<int:plate_id>/<int:well_id>', views.well, name='well'),
    path('add_well/<int:plate_id>', views.well_add, name='well_add'),
    # path('plate<int:plate_id>/<int:well_id/<int:sample_id>', views.sample, name='sample'),

    # path('add_data/', views.create_sample, name='add_data'),
    #
    # path('add_data/<int:sample_id>', views.edit_sample, name='edit_sample'),
    # path('add_data/file', views.upload_sample, name='add_file_data'),

    path('view_sample/', views.samples_list, name='samples_list'),
    path('view_sample/<int:sample_id>', views.sample, name='sample'),
    path('add_sample/', views.add_sample, name='sample_add'),
    path('export_sample/export', views.sample_export, name='sample_export'),

    path('delete/sample<int:sample_id>/', views.sample_delete, name='sample_delete'),
    path('edit_sample/<int:sample_id>/', views.edit_sample, name='sample_edit'),

    path('file_sharing/', views.file_sharing, name='file_sharing'),
    path('file_sharing/<int:file_id>', views.delete_file, name='delete_file'),

]