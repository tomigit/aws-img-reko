import boto3

s3 = boto3.resource('s3')

# Pobieranie listy obiektów do indeksowania
images=[('image1.jpg','Elon Musk'),
      ('image2.jpg','Elon Musk'),
      ('image3.jpg','Bill Gates'),
      ('image4.jpg','Bill Gates'),
      ('image5.jpg','Sundar Pichai'),
      ('image6.jpg','Sundar Pichai')
      ]

# Iteracja po liście, aby przesłać obiekty do S3 
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('famouspersons-img-012345x','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
