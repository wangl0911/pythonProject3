from django.db import models
from untils.base_model import BaseModel
# Create your models here.


class ProjectsModel(BaseModel):
    # unique   确定该字段的唯一性
    name = models.CharField(verbose_name='项目名称', help_text='项目名称', max_length=10, unique=True)
    leader = models.CharField(verbose_name='负责人', help_text='负责人', max_length=10)
    tester = models.CharField('测试人员', max_length=50, help_text='项目测试人员')
    programmer = models.CharField('开发人员', max_length=50, help_text='开发人员')
    publish_app = models.CharField('发布应用', max_length=100, help_text='发布应用')
    desc = models.CharField('简要描述', max_length=200, null=True, blank=True, default='', help_text='简要描述')

    class Meta:
        db_table = 'tb_projects'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name
