from PIL import Image 
import numpy as np

def msgconv(msg):
    print("Length: ", len(msg))
    pairs = []
    msglen = f"{len(msg):032b}"
    pairs += [msglen[j:j+2] for j in range(0,32,2)]
    for i in msg:
        s = f"{ord(i):08b}"
        pairs += [s[j:j+2] for j in range(0,8,2)]
    return pairs


def stegEncode(path, message):
    pairs = msgconv(message)
    image = np.asarray(Image.open(path))
    image = image.copy()  #makes the image writable

    i = 0
    for row in image:
        for pixel in row:
            s = f"{pixel[0]:08b}"
            t = s[0:-2] + pairs[i] 
            pixel[0] = int(t, 2)

            i += 1

            if i == len(pairs):
                break
        if i == len(pairs):
            break

    Image.fromarray(image).save(path)


def stegDecode(path):
    image = np.asarray(Image.open(path))
    message = ""
    temp = ""

    for pixel in image[0][0:16]: #read the length
        s = f"{pixel[0]:08b}"
        t = s[-2:]
        temp += t

    msgLength = int(temp, 2)
    print("Length: ",msgLength)
    temp = ""

    pixelCount = 0
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if (i==0 and j<16):         #16 coz first 4 bytes are msg length
                continue
            pixel = image[i][j]         
            s = f"{pixel[0]:08b}"
            t = s[-2:]
            temp += t
            pixelCount +=1
            
            if len(temp) == 8:
                message += chr(int(temp, 2))  #concatenate
                temp = ""

            if pixelCount == msgLength*4:
                break
        if pixelCount == msgLength*4:
            break

    return message



if __name__ == "__main__":
    msg = stegDecode("static/images/1678620686.png")
    print(msg)


#DIVIDE BY 4(floor). Multiply by 4. Add msgbit0 + 2*msgbit1
#numbers instead of strings. should be much faster
#make it multichannel ig
