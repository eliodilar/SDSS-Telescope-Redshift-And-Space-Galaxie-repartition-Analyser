# -*- coding: utf-8 -*-

from __future__ import division, print_function

#-------Lib_declaration--------
import os, glob
import PIL as pil 
from tkinter import * 
from tkinter.filedialog import *
import csv
import matplotlib.pyplot as plt
import numpy as np
from vpython import *
from math import *
#------------End_LIB------------


#------------Data---------------
cpt=0
Rvb=[0,0,0]
Cluster_List=[]
Scale_Limit = [0.001]*24
SimMinScaleRed = 0
SimMaxScaleRed = 0
ClusterObjectSIze = 0
ClusterObjectXdyn = 1.00
RedshiftSimulationFrame = Frame()
Frame_List = []
CheckSimulation = 0
Data_Vertex =[0.0000,0.0000,0.0000]

#--------------------------------



class Galactical_Cluster:

    def __init__(self):
      
        self.Obj_Id=0
        self.Ra=0
        self.Dec=0
        self.Z=0
        self.Lumdist=0
        self.Dered_u=0
        self.Dered_r=0
        self.Dered_z=0
        self.Dered_i=0
        self.Dered_g=0
        self.Model_Mag_u=0
        self.Model_Mag_r=0
        self.Model_Mag_z=0
        self.Model_Mag_i=0
        self.Model_Mag_g=0


    def Set_Obj_Id(self, _Value):

        self.Obj_Id = _Value


    def Get_Obj_Id(self):

        return self.Obj_Id 


    def Set_Ra(self, _Value):

        self.Ra = _Value


    def Get_Ra(self):

        return self.Ra


    def Set_Dec(self, _Value):

        self.Dec = _Value


    def Get_Dec(self):

        return self.Dec


    def Set_Z(self, _Value):

        self.Z = _Value


    def Get_Z(self):

        return self.Z


    def Set_Lumdist(self, _Value):

        self.Lumdist = _Value


    def Get_Lumdist(self):

        return self.Lumdist


    def Set_Dered_u(self, _Value):

        self.Dered_u = _Value


    def Get_Dered_u(self):

        return self.Dered_u


    def Set_Dered_r(self, _Value):

        self.Dered_r = _Value


    def Get_Dered_r(self):

        return self.Dered_r


    def Set_Dered_z(self, _Value):

        self.Dered_z = _Value


    def Get_Dered_z(self):

        return self.Dered_z


    def Set_Dered_i(self, _Value):

        self.Dered_i = _Value


    def Get_Dered_i(self):

        return self.Dered_i


    def Set_Dered_g(self, _Value):

        self.Dered_g = _Value


    def Get_Dered_g(self):

        return self.Dered_g


    def Set_Model_Mag_u(self, _Value):

        self.Model_Mag_u = _Value


    def Get_Model_Mag_u(self):

        return self.Model_Mag_u


    def Set_Model_Mag_r(self, _Value):

        self.Model_Mag_r = _Value


    def Get_Model_Mag_r(self):

        return self.Model_Mag_r


    def Set_Model_Mag_z(self, _Value):

        self.Model_Mag_z = _Value


    def Get_Model_Mag_z(self):

        return self.Model_Mag_z


    def Set_Model_Mag_i(self, _Value):

        self.Model_Mag_i = _Value


    def Get_Model_Mag_i(self):

        return self.Model_Mag_i


    def Set_Model_Mag_g(self, _Value):

        self.Model_Mag_g = _Value


    def Get_Model_Mag_g(self):

        return self.Model_Mag_g
    
    def move(evt):
        print("id=", Obj_Id)





    
def Rvb_Converter (Val, Lighting_Range, Min, Max):
    #bug sur purple taille hexa trop grand
    if Lighting_Range == "full":
        ScaleConverter = 16777215 / (Max - Min)
        RVB = format(int(ScaleConverter*Val), '#06X') #affine scale red dec on decimale rvb

    if Lighting_Range == "red":
        ScaleConverter = (16639465-10682368) / (Max - Min)
        RVB = format(int(ScaleConverter*Val) + 10682368, '#06X') #affine scale red dec on decimale rvb

    if Lighting_Range == "purple":
        ScaleConverter = (15657203-5577355) / (Max - Min)
        RVB = format(int(ScaleConverter*Val) + 5577355, '#06X') #affine scale red dec on decimale rvb

    if Lighting_Range == "green":
        ScaleConverter = (13493708-426240) / (Max - Min)
        RVB = format(int(ScaleConverter*Val) + 426240, '#06X') #affine scale red dec on decimale rvb

    if Lighting_Range == "yellow":
        ScaleConverter = (15461580-10461440) / (Max - Min)
        RVB = format(int(ScaleConverter*Val) + 10461440, '#06X') #affine scale red dec on decimale rvb
    
    Str_Conv=str(RVB)

    STR=Str_Conv[2:len(Str_Conv)]

    
    
    if len(STR) < 6:
        
        if len(STR) == 5:
            STR="0"+STR

        if len(STR) == 4:
            STR="00"+STR

        if len(STR) == 3:
            STR="000"+STR

        if len(STR) == 2:
            STR="0000"+STR
            
    return tuple(int(STR[i:i+2], 16) for i in (0, 2 ,4))


    


def ClusterSimulationMappingRedshift():
    #reste a faire l'adaptation des echelles de couleurs pour les differents simulation et diminuer taille du code en incluant dans une boucle for

    Index=listeSim.curselection()  ## Récupération de l'index de l'élément sélectionné
    ListBox = listeSim.get(Index)  ## On retourne l'élément (un string) sélectionné

    cpt = 0
    SimMinScale = float(ScaleMinSim.get())
    SimMaxScale = float(ScaleMaxSim.get())
    CulsterObjectSize = ScaleSimObjectSize.get()
    ClusterObjectXdyn = ScaleSimObjectXdyn.get()
    print("Mapping simulation running.")

    Frame_List.append(canvas(title='Redshift simulation scene',width=2000, height=1000,center=vector(0,0,0), background=color.black))
    
    if ListBox == "Redshift full light spectre":
    
        for Cluster in Cluster_List:   
            Rvb=Rvb_Converter (float(Cluster.Get_Z()),"full" , Scale_Limit[0], Scale_Limit[1])
            cpt=cpt+1
            
            if Cluster.Get_Z() >= SimMinScale and Cluster.Get_Z() <= SimMaxScale:
                #integrer pour l'axe des x une conversion de l'échelle pour adapter la lumdist au cercle trigo de norme 1 -- x = Lumdist * (1 / lumdist_Max) 
                myell = ellipsoid(title = Cluster.Get_Obj_Id(), canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Dec())),sin(float(Cluster.Get_Ra())),float((ClusterObjectXdyn*0.01)*((Scale_Limit[1]/Scale_Limit[2])*float(Cluster.Get_Lumdist())))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = 'galaxie2.jpg')
                

    if ListBox == "Redshift red light spectre":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Z()),"red", Scale_Limit[0], Scale_Limit[1])
            cpt=cpt+1
    
            if Cluster.Get_Z() >= SimMinScale and Cluster.Get_Z() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Dec())),sin(float(Cluster.Get_Ra())),float((ClusterObjectXdyn*0.01)*((Scale_Limit[1]/Scale_Limit[2])*float(Cluster.Get_Lumdist())))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    if ListBox == "Lumdist light spectre":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Lumdist()), "yellow", Scale_Limit[2], Scale_Limit[3])
            cpt=cpt+1
    
            if Cluster.Get_Lumdist() >= SimMinScale and Cluster.Get_Lumdist() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    
    if ListBox == "Dered UV light spectre":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Dered_u()),"purple", Scale_Limit[4], Scale_Limit[5])
            cpt=cpt+1
    
            if Cluster.Get_Dered_u() >= SimMinScale and Cluster.Get_Dered_u() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)



    if ListBox == "Dered Green light spectre":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Dered_r()),"green", Scale_Limit[6], Scale_Limit[7])
            cpt=cpt+1
    
            if Cluster.Get_Dered_r() >= SimMinScale and Cluster.Get_Dered_r() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    if ListBox == "Dered Red light spectre":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Dered_z()),"red", Scale_Limit[8], Scale_Limit[9])
            cpt=cpt+1
    
            if Cluster.Get_Dered_z() >= SimMinScale and Cluster.Get_Dered_z() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    if ListBox == "Dered Infrared 7600":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Dered_i()),"red", Scale_Limit[10], Scale_Limit[11])
            cpt=cpt+1
    
            if Cluster.Get_Dered_i() >= SimMinScale and Cluster.Get_Dered_i() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    if ListBox == "Dered Infrared 9100":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Dered_g()),"red", Scale_Limit[12], Scale_Limit[13])
            cpt=cpt+1
    
            if Cluster.Get_Dered_g() >= SimMinScale and Cluster.Get_Dered_g() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    if ListBox == "ModelMag UV light spectre":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Model_Mag_u()),"red", Scale_Limit[14], Scale_Limit[15])
            cpt=cpt+1
    
            if Cluster.Get_Model_Mag_u() >= SimMinScale and Cluster.Get_Model_Mag_u() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)



    if ListBox == "ModelMag Green light spectre":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Model_Mag_r()),"green", Scale_Limit[16], Scale_Limit[17])
            cpt=cpt+1
    
            if Cluster.Get_Model_Mag_r() >= SimMinScale and Cluster.Get_Model_Mag_r() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    if ListBox == "ModelMag Red light spectre":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Model_Mag_z()),"red", Scale_Limit[18], Scale_Limit[19])
            cpt=cpt+1
    
            if Cluster.Get_Model_Mag_z() >= SimMinScale and Cluster.Get_Model_Mag_z() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    if ListBox == "ModelMag Infrared 7600":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Model_Mag_i()),"red", Scale_Limit[20], Scale_Limit[21])
            cpt=cpt+1
    
            if Cluster.Get_Model_Mag_i() >= SimMinScale and Cluster.Get_Model_Mag_i() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)

    if ListBox == "ModelMag Infrared 9100":
    
        for Cluster in Cluster_List:
            Rvb=Rvb_Converter (float(Cluster.Get_Model_Mag_g()),"red", Scale_Limit[22], Scale_Limit[23])
            cpt=cpt+1
    
            if Cluster.Get_Model_Mag_g() >= SimMinScale and Cluster.Get_Model_Mag_g() <= SimMaxScale:
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Dec()))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( Rvb[0] * (1.0 / 255.0), Rvb[1] * (1.0 / 255.0),Rvb[2] * (1.0 / 255.0)), texture = textures.rough)


    if ListBox == "Cluster Vertex":
        for Cluster in Cluster_List:           

            if Cluster.Get_Z() >= SimMinScale and Cluster.Get_Z() <= Scale_Limit[1]:

                 for Cluster2 in Cluster_List:   
            
                    if Cluster2.Get_Z() >= SimMinScale and Cluster2.Get_Z() <= SimMaxScale:

                        a=vertex( pos=vec(cos(float(Cluster2.Get_Ra())),sin(float(Cluster2.Get_Ra())),cos(float(Cluster2.Get_Ra()))))
                        b=vertex( pos=vec(cos(float(Cluster.Get_Ra()+0.001)),sin(float(Cluster.Get_Ra()+0.001)),cos(float(Cluster.Get_Dec()+0.001))))
                        c=vertex( pos=vec(cos(float(Cluster.Get_Ra())),sin(float(Cluster.Get_Ra())),cos(float(Cluster.Get_Dec()))))
                        T = triangle( v0=a, v1=b, v2=c )


    if ListBox == "Chromatic Builder":
        for Cluster in Cluster_List:   
            cpt=cpt+1
            
            if Cluster.Get_Z() >= SimMinScale and Cluster.Get_Z() <= SimMaxScale:
                #integrer pour l'axe des x une conversion de l'échelle pour adapter la lumdist au cercle trigo de norme 1 -- x = Lumdist * (1 / lumdist_Max) 
                myell = ellipsoid(canvas = Frame_List[len(Frame_List)-1] , pos=vector(sin(float(Cluster.Get_Dec())),sin(float(Cluster.Get_Ra())),float((ClusterObjectXdyn*0.01)*((Scale_Limit[1]/Scale_Limit[2])*float(Cluster.Get_Lumdist())))),
                          axis=vector(1,1,1), length=CulsterObjectSize, height=CulsterObjectSize, width=CulsterObjectSize,
                          color=vector ( 255, 255,255), texture = textures.rough)

    
def ClusterSimulationMappingRedshiftKill():
    for Frame in Frame_List:
        Frame.delete()
        print("Scenes destruct")

def Draw2dCloudPointPlot():
    
    print("Plot under Drawing")
    X=[]
    Y=[]
    
    for Cluster in Cluster_List:
        X.append(float(Cluster.Get_Ra()))
        Y.append(float(Cluster.Get_Z()))
        
    plt.plot(X, Y, 'ro')
    #plt.ylabel('some numbers')
    print("Cloud Point Plot Draw")
    plt.show()


def Draw2dLinePlot():
    
    print("Plot under Drawing")
    X=[]
    Y=[]
    List_X=[]
    List_Y=[]

    
    c = 0
    
    for Cluster in Cluster_List:
        
        if c < 100000:
            X.append(float(Cluster.Get_Ra()))
            Y.append(float(Cluster.Get_Z()))

        c=c+1
            
        if c == 200000:
            List_X.append(X)
            List_Y.append(Y)
            del(X[:])
            del(Y[:])
            c = 0

    c = 0
            
    for Point in List_X:
        
        plt.figure(c + 1)
        plt.plot(List_X[c], List_Y[c]) 
        #plt.ylabel('some numbers')
        c = c + 1
        
    plt.show()
    del(List_X[:])
    del(List_Y[:])
    print("Line Plot Draw")


def RedshiftAnalyser():

    Bool1 = False
    Bool2 = True
    Bool3 = False
    Bool4 = False
    cptLoop = 0
    cpt = 0.0

    #Buffer_Pm4 = [0] * (MaxZ - MinZ) * 10000
    #Buffer_Pm3 = [0] * (MaxZ - MinZ) * 1000
    Buffer_Pm2 = [0] * int((ScaleLim[1] - ScaleLim[0]) * 100)
    Buffer_Pm1 = [0] * int((ScaleLim[1] - ScaleLim[0]) * 10)

        
    for Cluster in Cluster_List:

        if Bool1 == True:
            
            for Pointer in Buffer_Pm1:

                
                if float(Cluster.Get_Z()) > cpt and float(Cluster.Get_Z()) < cpt + 0.1:

                    Buffer_Pm1[cptLoop] = Cluster.Get_Z()

                cptLoop = cptLoop + 1
                cpt = cpt + 0.1


        if Bool2 == True:
            
            for Pointer in Buffer_Pm2:

                
                if float(Cluster.Get_Z()) > cpt and float(Cluster.Get_Z()) < cpt + 0.010000000:

                    Buffer_Pm2[cptLoop] = Cluster.Get_Z()
                    print( Cluster.Get_Z())

                cptLoop = cptLoop + 1
                cpt = cpt + 0.01

    plt.bar(np.arange(len(Buffer_Pm2)), Buffer_Pm2, 0.1, yerr=len(Buffer_Pm2))
    plt.show()


def CloudPointWindows():
    CloudPointWindowActiv=Toplevel(MainWindow)
    
    # Drawing 2D cloud point plot
    buttonDrawCloudPointPlot=Button(CloudPointWindowActiv, text="Drawing cloud point plot", command=Draw2dCloudPointPlot)
    buttonDrawCloudPointPlot.pack()

    # X Row Value actually no data return
    CloudRowX = Entry(CloudPointWindowActiv, textvariable="X axis collumn", width=30)
    CloudRowX .pack()

    # Y row Value actually no data return
    CloudRowY = Entry(CloudPointWindowActiv, textvariable="Y axis collumn", width=30)
    CloudRowY.pack()

def PlotPointWindows():
    PlotPointWindowActiv=Toplevel(MainWindow)
    
    # Drawing 2D line plot
    buttonDrawLinePlot=Button(PlotPointWindowActiv, text="Drawing Line plot", command=Draw2dLinePlot)
    buttonDrawLinePlot.pack()

    # X Row Value actually no data return
    PlotRowX = Entry(PlotPointWindowActiv, textvariable="X axis collumn", width=30)
    PlotRowX .pack()

    # Y row Value actually no data return
    PlotRowY = Entry(PlotPointWindowActiv, textvariable="Y axis collumn", width=30)
    PlotRowY.pack()
    

def RsWindows():
    RsWindowActiv=Toplevel(MainWindow)
    
    # Redshift Histograme
    buttonRedcHist=Button(RsWindowActiv, text="Redshift analyser", command=RedshiftAnalyser)
    buttonRedcHist.pack()

def ClusterSimulatorWindows():
    RsWindowActiv=Toplevel(MainWindow)
    
    # Redshift Histograme
    buttonRedcHist=Button(RsWindowActiv, text="Redshift analyser", command=RedshiftAnalyser)
    buttonRedcHist.pack()
    


filepath = askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')])
_chemin=filepath

_Data_Row_Csv = csv.reader(open(_chemin, newline=''), delimiter=' ', quotechar='|')


print("Application started!!")

cpt = 0
ScaleCount = 0
Count_Loader = 1

for row in _Data_Row_Csv:
    cpt = cpt + 1
    Cluster_Object = Galactical_Cluster()
    Cluster_Object.Set_Obj_Id(str(row[0]))
    Cluster_Object.Set_Ra(float(row[1]))
    Cluster_Object.Set_Dec(float(row[2]))
    Cluster_Object.Set_Z(float(row[3]))
    Cluster_Object.Set_Lumdist(float(row[4]))
    Cluster_Object.Set_Dered_u(float(row[5]))
    Cluster_Object.Set_Dered_r(float(row[6]))
    Cluster_Object.Set_Dered_z(float(row[7]))
    Cluster_Object.Set_Dered_i(float(row[8]))
    Cluster_Object.Set_Dered_g(float(row[9]))
    Cluster_Object.Set_Model_Mag_u(float(row[10]))
    Cluster_Object.Set_Model_Mag_r(float(row[11]))
    Cluster_Object.Set_Model_Mag_z(float(row[12]))
    Cluster_Object.Set_Model_Mag_i(float(row[13]))
    Cluster_Object.Set_Model_Mag_g(float(row[14]))
    Cluster_List.append(Cluster_Object)

    if cpt == 100000 * Count_Loader:
        print(100000*Count_Loader, " object traited")
        print("Data Memory allocation running!!")
        Count_Loader = Count_Loader + 1

    if cpt == 1:
        
        for ScaleLim  in range(0,int(len(Scale_Limit)/2)):
            Scale_Limit[ScaleCount] = float(row[3 + ScaleLim])
            Scale_Limit[ScaleCount + 1] = float(row[3 + ScaleLim])
            ScaleCount = ScaleCount + 2
            
        ScaleCount = 0

    for ScaleLim  in range(0,int(len(Scale_Limit)/2)):
        
        if float(row[3 + ScaleLim]) < float(Scale_Limit[ScaleCount]) and float(row[3 + ScaleLim]) > 0.0:
            Scale_Limit[ScaleCount] = float(row[3 + ScaleLim])

        if float(row[3 + ScaleLim]) > float(Scale_Limit[1 + ScaleCount])and float(row[3 + ScaleLim]) > 0.0:
            Scale_Limit[1 + ScaleCount] = float(row[3 + ScaleLim])

        ScaleCount = ScaleCount + 2

    ScaleCount = 0

Count_Loader =0

print(" ")
print(" ")
print("-----------------------------------------------------")
print("CSV Data traited!!")
print("Number of Galactical_Cluster_Object created = ", cpt)
print("-----------------------------------------------------")

cpt = 0
#for Cluster in Cluster_List:
 #   print(Cluster.Get_Obj_Id())


#------------------------------Main_Loop---------------------------------------

MainWindow = Tk()
MainWindow.title("Never Forget - VER-1")

#image equipe Apollo 1 bug...
img=PhotoImage(file="Apol.gif", master=MainWindow)
canvasf = Canvas(MainWindow)
canvasf.create_image(0, 0,image=img)
canvasf.pack()

# frame fenetre
FrameMainWindow = Frame(MainWindow, borderwidth=4, relief=GROOVE)
FrameMainWindow.pack(side=LEFT )

# frame Redshift simulation
FrameRedShiftSimWindow = Frame(MainWindow, borderwidth=4, relief=GROOVE)
FrameRedShiftSimWindow.pack(side=LEFT)

# frame Redshift simulation
FrameRedShiftSimWindowR1 = Frame(FrameRedShiftSimWindow, borderwidth=4, relief=GROOVE)
FrameRedShiftSimWindowR1.pack(side=LEFT)

# frame Redshift simulation
FrameRedShiftSimWindowR2 = Frame(FrameRedShiftSimWindow, borderwidth=4, relief=GROOVE)
FrameRedShiftSimWindowR2.pack(side=LEFT)


#Titre
labelFenetre = Label(FrameMainWindow, text="SDSS Data Processor.")
labelFenetre.pack()

#Plot Window
ClusterSimulatorWindowOpen=Button(FrameMainWindow, text="Galactical Cluster Simulator", command=ClusterSimulatorWindows)
ClusterSimulatorWindowOpen.pack()

#OpenWindow Cloud Point
CloudPointWindowOpen=Button(FrameMainWindow, text="Cloud point Analyser", command=CloudPointWindows)
CloudPointWindowOpen.pack()

#OpenWindow Cloud Point
PlotPointWindowOpen=Button(FrameMainWindow, text="Plot point Analyser", command=PlotPointWindows)
PlotPointWindowOpen.pack()

#OpenWindow Cloud Point
RedshiftWindowOpen=Button(FrameMainWindow, text="Redshift statistic analyser", command=RsWindows)
RedshiftWindowOpen.pack()

# liste selection color simulation
listeSim = Listbox(FrameRedShiftSimWindowR2, height = 15, width=25)
listeSim.insert(1, "Redshift full light spectre")
listeSim.insert(2, "Redshift red light spectre")
listeSim.insert(3, "Lumdist light spectre")
listeSim.insert(4, "Dered UV light spectre")
listeSim.insert(5, "Dered Green light spectre")
listeSim.insert(6, "Dered Red light spectre")
listeSim.insert(7, "Dered Infrared 7600")
listeSim.insert(8, "Dered Infrared 9100")
listeSim.insert(9, "ModelMag UV light spectre")
listeSim.insert(10, "ModelMag Green light spectre")
listeSim.insert(11, "ModelMag Red light spectre")
listeSim.insert(12, "ModelMag Infrared 7600")
listeSim.insert(13, "ModelMag Infrared 9100")
listeSim.insert(14, "Cluster Vertex")
listeSim.insert(15,"Chromatic Builder")
listeSim.pack()

# Draw a 3d mapping simulation redshift
buttonDraw3dSimulation=Button(FrameRedShiftSimWindowR1, text="3d Redshift mapping simulation", command=ClusterSimulationMappingRedshift)
buttonDraw3dSimulation.pack()

# Draw a 3d mapping simulation redshift Kill scene
buttonDraw3dSimulationKill=Button(FrameRedShiftSimWindowR1, text="Destruct scene", command=ClusterSimulationMappingRedshiftKill)
buttonDraw3dSimulationKill.pack()

# Z lim
ScaleSimZ = Label(FrameRedShiftSimWindowR1, text=("Low limit Z: ", str(Scale_Limit[0]),"Hight limit Z: ",str(Scale_Limit[1])) , bg="white")
ScaleSimZ.pack()

# lum lim
ScaleSimLum = Label(FrameRedShiftSimWindowR1, text=("Low limit Lum: ", str(Scale_Limit[2]),"Hight limit Lum: ",str(Scale_Limit[3])) , bg="white")
ScaleSimLum.pack()

# du lim
ScaleSimDu = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered u: ", str(Scale_Limit[4]),"Hight limit Dered u: ",str(Scale_Limit[5])) , bg="white")
ScaleSimDu.pack()

# dr lim
ScaleSimDr = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered r: ", str(Scale_Limit[6]),"Hight limit Dered r: ",str(Scale_Limit[7])) , bg="white")
ScaleSimDr.pack()

# dz lim
ScaleSimDz = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered z: ", str(Scale_Limit[8]),"Hight limit Dered z: ",str(Scale_Limit[9])) , bg="white")
ScaleSimDz.pack()

# di lim
ScaleSimDi = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered i: ", str(Scale_Limit[10]),"Hight limit Dered i: ",str(Scale_Limit[11])) , bg="white")
ScaleSimDi.pack()

# dg lim
ScaleSimDg = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered g: ", str(Scale_Limit[12]),"Hight limit Dered g: ",str(Scale_Limit[13])) , bg="white")
ScaleSimDg.pack()

# Mu lim
ScaleSimMu = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered u: ", str(Scale_Limit[14]),"Hight limit Dered u: ",str(Scale_Limit[15])) , bg="white")
ScaleSimMu.pack()

# Mr lim
ScaleSimMr = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered r: ", str(Scale_Limit[16]),"Hight limit Dered r: ",str(Scale_Limit[17])) , bg="white")
ScaleSimMr.pack()

# Mz lim
ScaleSimMz = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered z: ", str(Scale_Limit[18]),"Hight limit Dered z: ",str(Scale_Limit[19])) , bg="white")
ScaleSimMz.pack()

# Mi lim
ScaleSimMi = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered i: ", str(Scale_Limit[20]),"Hight limit Dered i: ",str(Scale_Limit[21])) , bg="white")
ScaleSimMi.pack()

# Mg lim
ScaleSimMg = Label(FrameRedShiftSimWindowR1, text=("Low limit Dered g: ", str(Scale_Limit[22]),"Hight limit Dered g: ",str(Scale_Limit[23])) , bg="white")
ScaleSimMg.pack()

# Min scale Sim
ScaleMinSim = Entry(FrameRedShiftSimWindowR1, textvariable="Min Cluster value desired", width=30)
ScaleMinSim .pack()

# Max scale Sim
ScaleMaxSim = Entry(FrameRedShiftSimWindowR1, textvariable="Max Cluster value desired", width=30)
ScaleMaxSim.pack()

#selector for object scale selection 
ScaleSimObjectSize = Scale(FrameRedShiftSimWindowR1, orient='vertical', from_=0, to=0.1,
      resolution=0.001, length=200,
      label='Cluster 0-100%')
ScaleSimObjectSize.pack(side=LEFT)

#selector for object scale selection for x axes 
ScaleSimObjectXdyn = Scale(FrameRedShiftSimWindowR1, orient='vertical', from_=0.0, to=100.00,
      resolution=0.001, length=200,
      label='Lumdist 0-100% ')
ScaleSimObjectXdyn.pack(side=RIGHT)


FrameMainWindow.mainloop()





