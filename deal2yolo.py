import os,shutil
from tqdm import tqdm
from pycocotools.coco import COCO



filePath='person_keypoints_train2017_foot_v1.json'
inImageDir='/datalab/my_project/datasets/train2017'
outImageDir='./images'
outLabelDir='./labels'

cocoFile=COCO(filePath)
jsonFile=cocoFile.dataset

inFileList=os.listdir(inImageDir)
outFileList=os.listdir(outImageDir)

cnt=0

for img in tqdm(jsonFile['images']):
    imgId=img['id']
    imageInfo=cocoFile.loadImgs(imgId)[0]
    name=img['file_name']
    height,width=img['height'],img['width']
    
    line=""


    for annId in cocoFile.getAnnIds(imgIds=[imgId]):
        item=cocoFile.loadAnns([annId])[0]

        minX,maxX,minY,maxY=9999,-9999,9999,-9999
        lminX,lmaxX,lminY,lmaxY=9999,-9999,9999,-9999
        rminX,rmaxX,rminY,rmaxY=9999,-9999,9999,-9999
        l=len(item['keypoints'])

        hasAnno=False
        lhasAnno=False
        rhasAnno=False
        
        leg_hasAnno=False
        leg_lhasAnno=False
        leg_rhasAnno=False

        lower_hasAnno=False

        # # print(l)
        # if l==6*3:
        #     for i in range(6):
        #         if item['keypoints'][i*3+2]==0:
        #             continue
        #         hasAnno=True
        #         minX=min(item['keypoints'][i*3],minX)
        #         maxX=max(item['keypoints'][i*3],maxX)
        #         minY=min(item['keypoints'][i*3+1],minY)
        #         maxY=max(item['keypoints'][i*3+1],maxY)
        #         if i<3:
        #             lhasAnno=True
        #             lminX=min(item['keypoints'][i*3],lminX)
        #             lmaxX=max(item['keypoints'][i*3],lmaxX)
        #             lminY=min(item['keypoints'][i*3+1],lminY)
        #             lmaxY=max(item['keypoints'][i*3+1],lmaxY)
        #         else:
        #             rhasAnno=True
        #             rminX=min(item['keypoints'][i*3],rminX)
        #             rmaxX=max(item['keypoints'][i*3],rmaxX)
        #             rminY=min(item['keypoints'][i*3+1],rminY)
        #             rmaxY=max(item['keypoints'][i*3+1],rmaxY)
        # elif l==(6+17)*3:
        if l==(6+17)*3:

            for i in range(15,23):
                if item['keypoints'][i*3+2]==0:
                    continue
                hasAnno=True
                minX=min(item['keypoints'][i*3],minX)
                maxX=max(item['keypoints'][i*3],maxX)
                minY=min(item['keypoints'][i*3+1],minY)
                maxY=max(item['keypoints'][i*3+1],maxY)
                if i==15 or 17<=i<20:
                    lhasAnno=True
                    lminX=min(item['keypoints'][i*3],lminX)
                    lmaxX=max(item['keypoints'][i*3],lmaxX)
                    lminY=min(item['keypoints'][i*3+1],lminY)
                    lmaxY=max(item['keypoints'][i*3+1],lmaxY)
                else:
                    rhasAnno=True
                    rminX=min(item['keypoints'][i*3],rminX)
                    rmaxX=max(item['keypoints'][i*3],rmaxX)
                    rminY=min(item['keypoints'][i*3+1],rminY)
                    rmaxY=max(item['keypoints'][i*3+1],rmaxY)
                    
            if hasAnno:
                centerX=(maxX+minX)/2
                centerY=(maxY+minY)/2

                boxWidth=maxX-minX
                boxWidth=min(boxWidth*1.2,centerX*2,(width-centerX)*2)
                boxHeight=maxY-minY
                boxHeight=min(boxHeight*1.2,centerY*2,(height-centerY)*2)

                line+=f"1 {centerX/width} {centerY/height} {boxWidth/width} {boxHeight/height}\n"

            if lhasAnno:
                centerX=(lmaxX+lminX)/2
                centerY=(lmaxY+lminY)/2

                boxWidth=lmaxX-lminX
                boxWidth=min(boxWidth*1.2,centerX*2,(width-centerX)*2)
                boxHeight=lmaxY-lminY
                boxHeight=min(boxHeight*1.4,centerY*2,(height-centerY)*2)

                line+=f"2 {centerX/width} {centerY/height} {boxWidth/width} {boxHeight/height}\n"
            if rhasAnno:
                centerX=(rmaxX+rminX)/2
                centerY=(rmaxY+rminY)/2

                boxWidth=rmaxX-rminX
                boxWidth=min(boxWidth*1.2,centerX*2,(width-centerX)*2)
                boxHeight=rmaxY-rminY
                boxHeight=min(boxHeight*1.4,centerY*2,(height-centerY)*2)

                line+=f"2 {centerX/width} {centerY/height} {boxWidth/width} {boxHeight/height}\n"

                
            for i in range(13,15):
                if item['keypoints'][i*3+2]==0:
                    continue
                leg_hasAnno=True
                minX=min(item['keypoints'][i*3],minX)
                maxX=max(item['keypoints'][i*3],maxX)
                minY=min(item['keypoints'][i*3+1],minY)
                maxY=max(item['keypoints'][i*3+1],maxY)
                if i==13:
                    leg_lhasAnno=True
                    lminX=min(item['keypoints'][i*3],lminX)
                    lmaxX=max(item['keypoints'][i*3],lmaxX)
                    lminY=min(item['keypoints'][i*3+1],lminY)
                    lmaxY=max(item['keypoints'][i*3+1],lmaxY)
                else:
                    leg_rhasAnno=True
                    rminX=min(item['keypoints'][i*3],rminX)
                    rmaxX=max(item['keypoints'][i*3],rmaxX)
                    rminY=min(item['keypoints'][i*3+1],rminY)
                    rmaxY=max(item['keypoints'][i*3+1],rmaxY)


                        
            if leg_hasAnno:
                centerX=(maxX+minX)/2
                centerY=(maxY+minY)/2

                boxWidth=maxX-minX
                boxWidth=min(boxWidth*1.2,centerX*2,(width-centerX)*2)
                boxHeight=maxY-minY
                boxHeight=min(boxHeight*1.2,centerY*2,(height-centerY)*2)

                line+=f"3 {centerX/width} {centerY/height} {boxWidth/width} {boxHeight/height}\n"

            if leg_lhasAnno:
                centerX=(lmaxX+lminX)/2
                centerY=(lmaxY+lminY)/2

                boxWidth=lmaxX-lminX
                boxWidth=min(boxWidth*1.2,centerX*2,(width-centerX)*2)
                boxHeight=lmaxY-lminY
                boxHeight=min(boxHeight*1.4,centerY*2,(height-centerY)*2)

                line+=f"4 {centerX/width} {centerY/height} {boxWidth/width} {boxHeight/height}\n"
            if leg_rhasAnno:
                centerX=(rmaxX+rminX)/2
                centerY=(rmaxY+rminY)/2

                boxWidth=rmaxX-rminX
                boxWidth=min(boxWidth*1.2,centerX*2,(width-centerX)*2)
                boxHeight=rmaxY-rminY
                boxHeight=min(boxHeight*1.4,centerY*2,(height-centerY)*2)

                line+=f"4 {centerX/width} {centerY/height} {boxWidth/width} {boxHeight/height}\n"
       
            for i in range(11,13):
                if item['keypoints'][i*3+2]==0:
                    continue
                lower_hasAnno=True
                minX=min(item['keypoints'][i*3],minX)
                maxX=max(item['keypoints'][i*3],maxX)
                minY=min(item['keypoints'][i*3+1],minY)
                maxY=max(item['keypoints'][i*3+1],maxY)

            if lower_hasAnno:
                centerX=(maxX+minX)/2
                centerY=(maxY+minY)/2

                boxWidth=maxX-minX
                boxWidth=min(boxWidth*1.2,centerX*2,(width-centerX)*2)
                boxHeight=maxY-minY
                boxHeight=min(boxHeight*1.2,centerY*2,(height-centerY)*2)

                line+=f"5 {centerX/width} {centerY/height} {boxWidth/width} {boxHeight/height}\n"


            for i in range(1,11):
                if item['keypoints'][i*3+2]==0:
                    continue
                lower_hasAnno=True
                minX=min(item['keypoints'][i*3],minX)
                maxX=max(item['keypoints'][i*3],maxX)
                minY=min(item['keypoints'][i*3+1],minY)
                maxY=max(item['keypoints'][i*3+1],maxY)
                
            centerX=(maxX+minX)/2
            centerY=(maxY+minY)/2

            boxWidth=maxX-minX
            boxWidth=min(boxWidth*1.2,centerX*2,(width-centerX)*2)
            boxHeight=maxY-minY
            boxHeight=min(boxHeight*1.2,centerY*2,(height-centerY)*2)
            line +=f"0 {centerX/width} {centerY/height} {boxWidth/width} {boxHeight/height}\n"
        else:
            print(id,name,l)
            print(item)
            exit()

        cnt+=1

    if line=="":
        continue
    
    with open(outLabelDir+os.sep+os.path.splitext(name)[0]+'.txt','w') as f:
        f.write(line)

    if name in inFileList:
        shutil.copy(inImageDir+os.sep+name,outImageDir+os.sep+name)
    elif name not in outFileList:
        # print(f'download {name}...')
        cocoFile.download(outImageDir,[imgId])

    

    

    



