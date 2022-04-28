import time

from people import People


def encode(pp):
    #start = time.time()
    result = pp.age_quantile + "#" + pp.hemoglobin + "#" + pp.platelets + "#" + pp.MPV + "#" + pp.RBC + \
             "#" + pp.lymphocytes + "#" + pp.MCHC + "#" + pp.leukocytes + "#" + pp.basophils + "#" + pp.MCH + \
             "#" + pp.eosinophils + "#" + pp.MCV + "#" + pp.monocytes + "#" + pp.RDW + \
             "#" + str(pp.detection_coronaviridae) + "#" + str(pp.detection_orthomyxoviridae) + \
             "#" + str(pp.detection_paramyxoviridae) + "#" + str(pp.detection_picornaviridae) + \
             "#" + str(pp.detection_pneumoviridae)
    #print(time.time() - start)
    return result


def decode(aggregation):
    result = aggregation.split('#')
    return result
