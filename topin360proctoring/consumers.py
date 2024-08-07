import os
import json
from uuid import uuid4
from proctoring import models
from django.core.files import File
from django.core.files.base import ContentFile
from channels.generic.websocket import WebsocketConsumer


class Proctor(WebsocketConsumer):

    def connect(self):
        self.file_name = uuid4()
        self.accept()
        self.send(text_data=json.dumps({
            'reponse_code': 'Connected'
        }))
        print('[CONNECTED]')

    def disconnect(self, close_code):
        try:
            with open(f'proctoring/media/temp/{self.file_name}.mp4', 'rb') as f:
                models.Video(
                    file=ContentFile(f.read() , name=os.path.basename(f.name)),
                    student_id=models.Student.objects.filter(student_id=self.uid).first(),
                    assessment_id=models.Assessment.objects.filter(assessment_id=self.aid).first()
                ).save()
            os.remove(f'proctoring/media/temp/{self.file_name}.mp4')
        except:
            pass
        print('[Disconnected...]')
        self.close()

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            self.uid = data['uid']
            self.aid = data['aid']
            self.file_name = f'{self.file_name}-{self.uid}-{self.aid}'

        if bytes_data:
            with open(f'proctoring/media/temp/{self.file_name}.mp4', 'ab') as f:
                f.write(bytes_data)
