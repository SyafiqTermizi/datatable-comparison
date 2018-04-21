from django.urls import path

from .views import HumanListViewHtmlTable, HumanListViewHtmlTablePagination, \
                    HumanListViewJqueryTable, HumanListViewJqueryTableAjax, \
                    HumanDetailView


urlpatterns = [
    path('html_table', HumanListViewHtmlTable.as_view(), name='html_table'),
    path('html_table_pagination', HumanListViewHtmlTablePagination.as_view(), name='html_table_pagination'),
    path('jquery_table', HumanListViewJqueryTable.as_view(), name='jquery_table'),
    path('jquery_table_ajax', HumanListViewJqueryTableAjax.as_view(), name='jquery_table_ajax'),
    path('<int:pk>', HumanDetailView.as_view(), name='human_detail' )
]