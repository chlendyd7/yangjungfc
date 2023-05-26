from django.urls import path
from .views import base_views, answer_views, question_views
app_name = 'soccer'

urlpatterns = [
    path('', base_views.home, name='home'),
    # base
    # path('', base_views.index, name='index'),
    path('board', base_views.board, name='board'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # # question
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    # answer
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # # recommend
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]
