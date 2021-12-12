from django.urls import path
from Questions import views

urlpatterns = [
    # path('questions/', views.question_list),
    # path('questions/<int:pk>', views.question_detail),
    path('question/', views.QuestionsList.as_view()),
    path('question/<int:pk>', views.QuestionDetail.as_view())
]
