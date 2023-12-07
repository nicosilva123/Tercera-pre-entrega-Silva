from django.urls import path

from AppCoder.views import (
    cursos_buscar_view,
    inicio_view,
    crea_profesor,
    eliminar_profesor,
    editar_profesor,
    Lista_todo,
    eliminar_curso,
    editar_curso,
    crea_curso,
    profesor_buscar,
    crea_estudiante,
    eliminar_estudiante,
    editar_estudiante,
    estudianteBuscar,
    # cursos_todos_view,
    # Lista_profesores,
    # CursoList,
    # CursoCreate,
    # CursoDatail,
    # CursoDelete,
    # CursoUpdate
    )


app_name = "AppCoder"

urlpatterns = [
    path("inicio/", inicio_view, name="inicio"),
    path("leer_todo/",Lista_todo, name="leer_todo"),
    path("crear_curso/", crea_curso, name="crea_curso"),
    path("cursos/buscar", cursos_buscar_view, name="cursos-buscar"),
    path("editar_curso/<int:id>", editar_curso, name="editar_curso"),
    path("eliminar_curso/<int:id>", eliminar_curso, name="eliminar_curso"),
    path("profesorFormulario/", crea_profesor, name="crea_profesor"),
    path("profesor_buscar", profesor_buscar, name="profesor_buscar"),
    path("eliminar_profesor/<int:id>", eliminar_profesor, name="eliminar_profesor"),
    path("editar_profesor/<int:id>", editar_profesor, name="editar_profesor"),
    path("crea_estudiante/", crea_estudiante, name="crea_estudiante"),
    path("eliminar_estudiante/<int:id>", eliminar_estudiante, name="eliminar_estudiante"),
    path("editar_estudiante/<int:id>", editar_estudiante, name="editar_estudiante"),
    path("estudianteBuscar", estudianteBuscar, name="estudianteBuscar"),
    # path("lista-cursos/", CursoList.as_view(), name="lista-cursos"),
    # path("detalle-cursos/<pk>", CursoDatail.as_view(), name="detalle-cursos"),
    # path("crea-curso/", CursoCreate.as_view(), name="crea-curso"),
    # path("editar-curso/<pk>", CursoUpdate.as_view(), name="editar-curso"),
    # path("eliminar-curso/<pk>", CursoDelete.as_view(), name="eliminar-curso"),
]
