import time
baari_2 = "Kadi tu es Gali de hi , Agle morr te milda si , Tainu khabar si saari ke , Haal jo mere dil da si , Tu bhul gaya saariyan oh gallan , Te mai na bhulli ve sajna , Ke aj mainu vekh k vi hath te , Teri chaah dulli na sajna , Vekhi teri wafa sajna , Bhul gayi si mai raah sajna , Jandi jandi kho gayi saah , Khwaabaan de vich tere , Main taan hi uchiyan deewaran rakhiyan , Iss dil de chaar chufere , Naale saambh k rakhiya si , Koi dil ch na laa de dere"
song = baari_2.split(",")
for i in range(0,len(song),1):
    print(song[i])
    time.sleep(1)