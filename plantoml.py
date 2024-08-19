import os
import re
import subprocess
def plantomlfetcher(plantomlfile = None):
    """
    Author Gaurav sablok
    Universitat Potsdam
    Date 2024-4-19
    A plant ontology extracter from the plant oml files for the plant ontology number 
    to make the links to the graphs. A part of the ontology analyzer package. 
    :param plantomlfile: 
    :return: finalplantontology
    """
    global finalplantontology
    if plantomlfile is not None:
        plantomlread = [i.strip().split("\n") for i in open(plantomlfile).readlines()]
        plantomlfetch = [plantomlread[i] for i in range(len(plantomlread)) if "PO" in ''.join(plantomlread[i])]
        extractplantontology = []
        finalplantontology = []
        for i in range(len(plantomlfetch)):
            if len(re.findall(r"PO_[0-9]{,10}", ''.join(plantomlfetch[i]))) >= 1:
                extractplantontology.append(re.findall(r"PO_[0-9]{,10}", ''.join(plantomlfetch[i])))
        for i in range(len(extractplantontology)):
            if len(''.join(extractplantontology[i])) <= 3:
                pass
            else:
                finalplantontology.append(''.join(extractplantontology[i]))
    return finalplantontology
