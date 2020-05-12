
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:20:21 2020

@author: Eshika Mahajan
"""

#IMPORTING NECESSARY LIBRARIES
from bs4 import BeautifulSoup
infile = open("chemsep1.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml') #GIVING COMMAND TO PARSE XML FILE
compound = soup.findAll('compound')  #FETCHING THE COMPONENTS FROM TAGNAME =COMPOUND


class ChemsepDatabase():
    
    def __init__(self):
        
        self.comp_name_list=list()
        self.name = 'chemsep'
        for comp in compound:
            
            self.compName=comp.CompoundID.attrs['value']
            self.comp_name_list.append(self.compName+'(' + self.name + ')')
#CREATING LIST CONTAINING ALL THE COMPOUNDS FROM DATABASE
        
        
    def get_comp_name_list(self):
        return self.comp_name_list  #RETURNING THE ABOVE MADE LIST
    
    #attrib:
    #CAS fro CAS Number
    #CompoundID for Name
    #Smiles for Molecular Formula
    #MolecularWeight for Molecular Weight


#GETTING 'ATTRIBUTE''S VALUE OF THE COMPOUND 'COMPS'
#COMP IS AN ITERATING VALUE IN THE XML TAG COMPOUND    
#IN DATABASE CHEMSEP, NOT EVERY COMPOUND HAS SMILES THUS BEFORE FETCHING THE SMILES VALUE IT 
#WAS NECESSARY TO CHECK WHTHER THE COMPOUND HAS SMILES TAG OR NOT
    
    def get_value(self,comps,attrib):
        self.comps=comps
        self.x=''
        for comp in compound:
            compName = comp.CompoundID.attrs['value']
            if compName==comps:
                
                if attrib=='CAS':
                    try:
                        self.x=comp.CAS.attrs['value']                        
                    except IndexError:
                        self.x = "0"
                            
                elif attrib=='MolecularWeight':
                    try:
                        self.x=comp.MolecularWeight.attrs['value']
                    except IndexError:
                        self.x = "-"                
        return (self.x)
    
    
    def fetching_attrib(self,comp,attrib):
        for i in compound:
            compName = i.CompoundID.attrs['value']
            if compName==comp:
                xyz= i.findAll(attrib)
        return(xyz)



    def checking_attrib(self,xyz):
        if xyz:
            return 1
        else:
            return 0
    
    def get_value_smiles(self,comps,attrib):
        self.comps=comps
        self.x=''
        for comp in compound:
            compName = comp.CompoundID.attrs['value']
            if compName==comps:
                x=self.checking_attrib(self.fetching_attrib(comps,attrib))
                if x:
                    yz= comp.Smiles.attrs['value']
   
                else:
                    yz="-"
                
        return (yz)
    


