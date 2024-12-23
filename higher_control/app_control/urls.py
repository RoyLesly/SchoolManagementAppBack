from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *
from .viewsStats import *


app_name = "higher_control.app_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register('domain',  DomainView, "domain" ),
router.register('field',  FieldView, ",field" ),
router.register('mainspecialty',  MainSpecialtyView, ",mainspecialty" ),
router.register('specialty',  SpecialtyView, "specialty" ),
router.register('maincourse',  MainCourseView, "maincourse" ),
router.register('course',  CourseView, "course" ),
router.register('course-upload',  CourseUploadView, "course-upload" ),
router.register('course-module',  CourseModuleView, "course-module" ),
router.register('course-module-detail',  CourseModuleDetailView, "course-module-detail" ),
router.register('result',  ResultView, "result" ),
router.register('level',  LevelView, "level" ),
router.register('publish',  PublishView, "publish" ),
router.register('school-info-higher',  SchoolInfoHigherView, "school-info-higher" ),
router.register('school-identification-higher',  SchoolIdentificationHigherView, "school-identification-higher" ),
router.register('sys-category',  SysCategoryView, "sys-category" ),
router.register('sys-constants',  SysConstantView, "sys-constants" ),

router.register('get-domain',  GetDomainView, "get-domain" ),
router.register('get-field',  GetFieldView, "get-field" ),
router.register('get-mainspecialty',  GetMainSpecialtyView, "get-mainspecialty" ),
router.register('get-specialty',  GetSpecialtyView, "get-specialty" ),
router.register('get-maincourse',  GetMainCourseView, "get-maincourse" ),
router.register('get-course',  GetCourseView, "get-course" ),
router.register('get-course-upload',  GetCourseUploadView, "get-course-upload" ),
router.register('get-course-module',  GetCourseModuleView, "get-course-module" ),
router.register('get-course-module-detail',  GetCourseModuleDetailView, "get-course-module-detail" ),
router.register('get-result',  GetResultView, "get-result" ),
router.register('get-result-transcript',  GetResultTranscriptView, "get-result-transcript" ),
router.register('get-level',  GetLevelView, "get-level" ),
router.register('get-publish',  GetPublishView, "get-publish" ),
router.register('get-school-info',  GetSchoolInfoView, "get-school-info-higher" ),
router.register('get-settings',  GetSchoolSettingsView, ",get-transcript-application" ),
router.register('get-school-identification',  GetSchoolIdentificationView, "get-school-identification-higher" ),
router.register('get-sys-category',  GetSysCategoryView, "get-setting-higher" ),
router.register('get-sys-constant',  GetSysConstantView, "get-sys-constant" ),

router.register('semester',  GetSemesterView, "semester" ),
router.register('academic-year',  GetAcademicYearView, "academic-year" ),


#Statistics

router.register('get-stats-by-domain',  GetStatsByDomainView, "get-stats-by-domain" ),
router.register('get-stats-by-specialty',  GetStatsBySpecialtyView, "get-stats-by-specialty" ),
router.register('get-stats-students-pending-fees',  GetStatsStudentsPendingFeesView, "get-stats-students-pending-fees" ),
router.register('get-stats-user-card-count',  GetStatsUserCardCountView, "get-stats-user-card-count" ),
router.register('get-stats-finance-chart-count',  GetStatsFinanceChartView, "get-stats-finance-chart-count" ),
router.register('get-stats-profile-sex-chart-count',  GetStatsSexChartView, "get-stats-profile-sex-chart-count" ),
router.register('get-stats-user-sex-chart-count',  GetStatsUsersSexChartView, "get-stats-user-sex-chart-count" ),
router.register('get-stats-by-specialties-and-levels-count',  GetStatsBySpecialtiesAndLevelsView, "get-stats-by-specialties-and-levels-count" ),
router.register('get-stats-by-specialties-and-levels-income',  GetStatsBySpecialtyAndLevelIncomeView, "get-stats-by-specialties-and-levels-income" ),


urlpatterns = [
    path('', include(router.urls)),
]
