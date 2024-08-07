from django.shortcuts import render
from uuid import uuid4
from django.http import Http404, StreamingHttpResponse
import os
from wsgiref.util import FileWrapper
import mimetypes


def home(request):
    proctor_id = uuid4()

    # DUMMY IDs FOR TESTING
    assessment_id = uuid4()
    user_id = uuid4()

    context = {
        'proctor_id': proctor_id,
        'assessment_id': assessment_id,
        'user_id': user_id,
    }
    return render(request, 'proctoring/index.html', context=context)


# def proctor(request, proctor_id, user_id, assessment_id):
#     context = {
#         'proctor_id': proctor_id,
#         'assessment_id': assessment_id,
#         'user_id': user_id,
#     }
#     return render(request, 'proctoring/proctor.html', context=context)


def proctor(request, proctor_id):
    user_id = None
    assessment_id = None

    if request.method == 'GET':
        user_id = request.GET.get('student-id')
        assessment_id = request.GET.get('assessment-id')

    context = {
        'proctor_id': proctor_id,
        'assessment_id': assessment_id,
        'user_id': user_id,
    }
    return render(request, 'proctoring/proctor.html', context=context)


def download_file(request):
    base = '/media/videos/'
    filename = request.path[len(base):-1]
    file = f'proctoring{request.path[:-1]}'
    chunk_size = 8192
    try:
        response = StreamingHttpResponse(
            FileWrapper(
                open(file, "rb"),
                chunk_size,
            ),
            content_type=mimetypes.guess_type(file)[0],
        )
        response["Content-Length"] = os.path.getsize(file)
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response
    except:
        raise Http404
