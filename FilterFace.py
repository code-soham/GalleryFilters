import os
import cv2 as cv

File_object = open("dirName.txt","r")
dir= File_object.readline();
solo=0
group=0
obj=0

haar_cascade= cv.CascadeClassifier('C:\\Users\\soham\\Documents\\CODING\\opencv\\Faces\\haar_face.xml');
for filename in os.listdir(dir):
    if filename.endswith(".jpg"): 
        pathname=os.path.join(dir,filename);
        img=cv.imread(pathname);
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY);
        faces=haar_cascade.detectMultiScale(gray,1.3,5);
        # for (x,y,w,h) in faces:
        #     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2);
        if(len(faces)==0):
            obj+=1;
        elif(len(faces)==1):
            solo+=1;
        else:
            group+=1;
            #  print(os.path.join(dir, filename))
    else:
        continue
print(f'Pictures read :{solo+group+obj}');
print(f'Solo pictures :{solo}');
print(f'Group pictures :{group}');
print(f'Abstract pictures :{obj}');
