from django.urls import path
from .views import HospitalCreate, MedicoCreate , PacienteCreate , CronogramaCreate , ConsultaCreate, ComentarioCreate
from .views import  HospitalUpdate, MedicoUpdate , PacienteUpdate,CronogramaUpdate , ConsultaUpdate ,Consulta2Update
from .views import  HospitalDelete,MedicoDelete , Pacientedelete , CronogramaDelete, ConsultaDelete
from .views import  HospitalList,MedicoList ,PacienteList ,CronogramaList ,ConsultaList,ComentarioList





urlpatterns = [
    path('cadastrar/hospital/', HospitalCreate.as_view(),
        name='cadastrar-hospital'),
    path('cadastrar/medico/', MedicoCreate.as_view(),
        name='cadastrar-medico'),
    path('cadastrar/paciente/', PacienteCreate.as_view(),
        name='cadastrar-paciente'),
    path('cadastrar/cronograma/', CronogramaCreate.as_view(),
        name='cadastrar-cronograma'),
    path('cadastrar/consulta/', ConsultaCreate.as_view(),
        name='cadastrar-consulta'),
   
    path('cadastrar/comentario/', ComentarioCreate.as_view(),
        name='cadastra-comentario'),

    path('editar/hospital/<int:pk>', HospitalUpdate.as_view(),
        name='editar-hospital'),
    path('editar/medico/<int:pk>',MedicoUpdate.as_view(),
        name='editar-medico'),
    path('editar/paciente/<int:pk>', PacienteUpdate.as_view(),
        name='editar-paciente'),
    path('editar/cronograma/<int:pk>', CronogramaUpdate.as_view(),
        name='editar-cronograma'),
    path('editar/consulta/<int:pk>', ConsultaUpdate.as_view(),
        name='editar-consulta'),
    path('editar/consulta2/<int:pk>', Consulta2Update.as_view(),
        name='editar-consulta2'),
    

    
    path('excluir/hospital/<int:pk>', HospitalDelete.as_view(),
        name='excluir-hospital'),
    path('excluir/medico/<int:pk>',MedicoDelete.as_view(),
        name='excluir-medico'),
    path('excluir/paciente/<int:pk>', Pacientedelete.as_view(),
        name='excluir-paciente'),
    path('excluir/cronograma/<int:pk>', CronogramaDelete.as_view(),
        name='excluir-cronograma'),
    path('excluir/consulta/<int:pk>',ConsultaDelete.as_view(),
        name='excluir-consulta'),
    
    path('listar/hospital/', HospitalList.as_view(),
        name='listar-hospital'),
    path('listar/Medico/', MedicoList.as_view(),
        name='listar-medico'),
    path('listar/paciente/', PacienteList.as_view(),
        name='Listar-paciente'),
    path('listar/cronograma/',CronogramaList.as_view(),
        name='Listar-cronograma'),
    path('listar/consulta/',ConsultaList.as_view(),
    name='Listar-consulta'),
    path('listar/comentario/',ComentarioList.as_view(),
    name='Listar-comentario'),
    
   
]