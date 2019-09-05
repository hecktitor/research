#Hector A. Sierra
import numpy as np
import matplotlib.pyplot as plt

def FromHexToDec(num):#Converts Hexadecimal numbers to Decimals in the byte order required
	x = int.from_bytes(num, byteorder='little', signed = True)
	return x





wav = open("gamecubemono.wav", "rb")#Opens file and enables read only


#The skip variables are for skipping the content that its not going to be used
skip = wav.read(16)#Reads through the first 20 bytes

SubChunk1Size = FromHexToDec(wav.read(4))
print("Subchunk1Size = ", SubChunk1Size)

AudioFormat = FromHexToDec(wav.read(2))
print("Audio Format = ", AudioFormat)
NumChannel = FromHexToDec(wav.read(2))
print("Num Channel =", NumChannel)
#Verifies is its Mono or Stereo
if NumChannel == 1:
	print("Channel = Mono")
else: 
	print("Channel = Stereo")

SampleRate = FromHexToDec(wav.read(4))
print("Sample Rate =", SampleRate)


skip2 = wav.read(6)

BitsPerSample = FromHexToDec(wav.read(2))
print("Bits Per Sample =", BitsPerSample)


while b'data' != wav.read(4):#verify if there is extra data between fmt and data subchunks
	extra = FromHexToDec(wav.read(4))#reads the size of estra data
	wav.read(extra)#read the extra data


Subchunk2Size = FromHexToDec(wav.read(4))#Size of the file 
print("Subchunk2Size =", Subchunk2Size)



BytesPerSample = BitsPerSample/8

AudioLenght =  Subchunk2Size / (SampleRate * NumChannel * BytesPerSample ) #Duration of the sound
print("Audio lenght = ", AudioLenght)


BytesPerSample = BitsPerSample/8
BytesPerSample = int(BytesPerSample)
f = Subchunk2Size/(NumChannel * BytesPerSample)
print("f = ", f)

print (BytesPerSample)
TotalBytes = int(f)#Number of bytes in the data

sampleList = []

for i in range(TotalBytes):
	print(i, "  ", end = "")
	for j in range(NumChannel):
		
		sample = FromHexToDec(wav.read(BytesPerSample))
		print(sample, "  ", end = "" )
		sampleList.append(sample)
	print()



# plt.plot(sampleList)
# plt.title("Gamecube wave form")
# plt.ylable("Frequency")
# plt.xlable("Time")
# plt.show()

wav.close()
