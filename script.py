import cv2
import matplotlib.pyplot as plt
import math

averages = []
testing = 0
puzzle = 0
coding = 0
leaderboard = 0
unknown = 0

cap = cv2.VideoCapture('video.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        a = frame.mean(axis=0).mean(axis=0).mean(axis=0)
        averages.append(a)
        
        if a < 100 or (a > 175 and a < 200):
            testing += 1
        elif a > 130 and a < 160:
            puzzle += 1
        elif a > 230:
            coding += 1
        elif a < 230 and a > 210:
            leaderboard += 1
        else:
            unknown += 1 
    else:
        break

point = None
def show_video_frame(event):
    if event.inaxes == ax1 and event.xdata:
        x = math.floor(event.xdata)
        cap.set(1, x)
        ret, frame = cap.read()
        if ret:
            global point
            if point:
                point[0].remove()
            point = ax1.plot(x, averages[x], marker='o', color='r')
            ax2.imshow(frame)
            plt.draw()

fig, [ax1, ax2] = plt.subplots(2, 1)

ax1.plot(averages)
ax1.set_xlim(left=0, right=len(averages))

plt.connect('motion_notify_event', show_video_frame)
plt.show()

cap.release()
cv2.destroyAllWindows()

print("testing:", 100*testing/len(averages))
print("puzzle:", 100*puzzle/len(averages))
print("coding:",100*coding/len(averages))
print("leaderboard:", 100*leaderboard/len(averages))
print("unknown:", 100*unknown/len(averages))