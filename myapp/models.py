from django.db import models


class Student(models.Model):

       name = models.CharField(max_length=100)
       price = models.FloatField(max_length=100)
       manufacturing = models.CharField(max_length= 500)
       #image = models.ImageField(null=True, blank= True,upload_to= 'images')
       expired = models.CharField(max_length=100)


def __str__(self):
       s = "Tên sản phẩm: " + str(self.name) + ", Gía sản phẩm : " + str(self.price) +",sản xuất "\
       + str(self.manufacturing) + ",Ảnh " + str(self.image) + ", Hết hạn sử dụng " + str(self.expired)
       return s