# from curses.ascii import FF
# import cv2 
# cap=cv2.VideoCapture('video.mp4')
# while(cap.isOpened()):
#     ret,frame=cap.read()
#     if ret==True:
#         cv2.imshow('cat' , frame)
#         if cv2.waitKey(25) & 0xFF==ord('q'): 
#             break

#######################################################

# from curses.ascii import FF
# import cv2 
# import os 
# import shutil 

# filename = 'video2.mp4'

# if os.path.exists('output'):
#     shutil.rmtree('output')
# os.makedirs('output')
# cap = cv2.VideoCapture(filename)
# count = 0

# while cap.isOpened():
#     ret,frame=cap.read()
#     if ret==True:
#         cv2.imshow('video2' , frame)
#         cv2.imwrite("./output/frame%s.jpg" % count,frame)
#         count = count+1

        # if cv2.waitKey(1) & 0xFF==ord('q'): 
#             break
#     else:
#             break
    
# cap.release()
# cv2.destroyAllWindows()

###################################################################

# from curses.ascii import FF
# import cv2
# import os
# import shutil
# from datetime import datetime

# filename = 'video3.mp4'

# # Handle output directory
# output_dir = 'output'
# if os.path.exists(output_dir):
#     print(f"Directory '{output_dir}' already exists and will be deleted.")
#     shutil.rmtree(output_dir)
# os.makedirs(output_dir)

# cap = cv2.VideoCapture(filename)
# if not cap.isOpened():
#     print("Error: Cannot open video file.")
#     exit()

# fps = int(cap.get(cv2.CAP_PROP_FPS))  
# frame_interval = fps  
# count = 0

# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret:
#         if count % frame_interval == 0:  
#             t = datetime.now()
#             ts = t.strftime('%H%M%S')
#             frame_name = f"./{output_dir}/frame_{count}_{ts}.jpg"
#             cv2.imwrite(frame_name, frame)
#             print(f"Saved: {frame_name}")
#         count += 1

#         cv2.imshow('video3', frame)
#         if cv2.waitKey(25) & 0xFF == ord('q'):  
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()

########################################################################
