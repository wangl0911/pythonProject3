from django.db import models
from untils.base_model import BaseModel
# Create your models here.


class Interfaces(BaseModel):
    name = models.CharField(verbose_name='接口名称', max_length=200, unique=True, help_text='接口名称')
    project = models.ForeignKey('projects.ProjectsModel', on_delete=models.CASCADE,
                                related_name='interfaces', help_text='所属项目')
    tester = models.CharField('测试人员', max_length=50, help_text='测试人员')
    desc = models.CharField('简要描述', max_length=200, null=True, blank=True, help_text='简要描述')

    class Meta:
        db_table = 'tb_interfaces'
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

