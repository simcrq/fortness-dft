#!/public3/soft/python/3.7.6/bin/python3.7


import os
import sys
import os.path
import numpy as np
import math as mp
import shutil


directlist = os.getcwd().split('/')
comname = directlist[len(directlist)-1]
calculations = sys.argv[1]
jobname = comname + '-' + calculations


def checkcluster():
    cluster = os.popen("pwd").read().split('/')[3]
    return cluster.strip()

def checkrelaxation(relx):
    ''' ical = 0: no relaxation
        ical = 1: INCAR-1
        ical = 2: INCAR-2
        ical = 3: INCAR-3
        ical = 4: INCAR-4
        ical = 5: INCAR-self
        ical = 6: INCAR-phonon
        ical = 7: INCAR-band
        ical = 8: BTE '''
    ical = 0
    converstring = 'reached required accuracy - stopping structural energy minimisation'
    if relx == 'relaxation':
        outcarlist = ['OUTCAR-4', 'OUTCAR-3', 'OUTCAR-2', 'OUTCAR-1']
        icalist = []
        for i in range(len(outcarlist)):
            if os.path.exists(outcarlist[i]):
                if converstring in open(outcarlist[i]).read():
                    icalist.append(1)
                else:
                    icalist.append(0)
            else:
                icalist.append(0)
        if icalist.count(1) == 4:
            ical = 0
        else:
            ical =  icalist.count(1) + 1
    elif relx == 'static':
        if os.path.exists('OUTCAR-4'):
            foutcar = open('OUTCAR-4','r')
            for line in foutcar:
                if converstring in line:
                    ical = 6
                    break
                else:
                    print('relaxation is not sucess and I can not do static')
                    ical = 0
            foutcar.close()
        else:
            ical = 0
            print('relaxation is not sucess, please do relaxation first')
    elif relx == 'phonon' or relx == 'hse' or relx == 'band' or relx == 'bandsoc' or relx == 'bte' :
        if os.path.exists('OUTCAR-4'):
            foutcar = open('OUTCAR-4','r')
            for line in foutcar:
               if converstring in line:
                   ical = 7
                   break
            if ical != 7:
               print('relaxation is not sucess and I can not do phonon/band/BTE')
               ical = 0
            foutcar.close()
        else:
            ical = 0
            print('relaxation is not sucess, please do relaxation first')
    else:
        ical = 0
        print('please check your setting')
        print('relaxation, phonon, hse, band, bandsoc, bte')
    return ical


def check_specail_element(poscar):
    myalgo = 'ALGO      = Normal'
    fposcar = open(poscar,'r').readlines()
    element = fposcar[5]
    if 'Lu' in element:
       myalgo = 'ALGO      = Fast'
    return myalgo


def checkmagnetic(poscar):
    lspin = 'ISPIN     = 1'
    fposcar = open(poscar,'r').readlines()
    element = fposcar[5].split()
    melemt = ['Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Ce', 'Eu']
    for ele in element:
        if ele in melemt:
            lspin = 'ISPIN     = 2'
            break
    return lspin

def setnpar(clus):
    npar = 'NPAR      = 1'
    if clus == 'scb6433' :
        npar = 'NPAR     = 2'
    elif clus == 'a6s000254':
        npar = 'NPAR      = 2'
    return npar


##############
def supecellgen():
    '''generate supercell for phonon calculation'''

    #Target size: a diagonal matrix with some lenth acell
    alat=12.0
    A = np.matrix(((alat,0.,0.),(0.,alat,0.),(0.,0.,alat)))

    poscar = open('phonon/POSCAR-prim','r')
    title = poscar.readline().strip()
    comment = title
    scale = float(poscar.readline().strip())
    s = float(scale)
    cell = [[ float(v) for v in poscar.readline().split() ],
           [  float(v) for v in poscar.readline().split() ],
           [  float(v) for v in poscar.readline().split() ]]
    poscar.close()
    cell = np.matrix(cell)
    celli=np.linalg.inv(cell)
    trans=np.dot(A,celli)
    transc=np.round(trans)
    dims=np.array(transc)
    f=open('phonon/supercell', 'w')
    # f.write('%-10s %3d %3d %3d %3d %3d %3d %3d %3d %3d' % ('DIM = ', int(dims[0][0]), int(dims[0][1]), int(dims[0][2]),
    #    int(dims[1][0]), int(dims[1][1]), int(dims[1][2]), int(dims[2][0]), int(dims[2][1]), int(dims[2][2])))
    f.write('DIM = 2 2 2  \n ')
    f.write('\n')
    f.write('# DISPLACEMENT_DISTANCE = 0.01')
    f.close()
    os.system('phonopy --tolerance=1e-3  -d phonon/supercell -c phonon/POSCAR-prim')
##############


#### set INCAR
def setincar():
    if calculations == 'relaxation':
       incarlist=['INCAR-1','INCAR-2','INCAR-3','INCAR-4']
       print('here')
       for inc in incarlist:
           if inc == 'INCAR-1':
               encut = 'ENCUT     = 400'
               prec  = 'PREC      = Normal'
               lreal = 'LREAL     = Auto'
           elif inc == 'INCAR-2':
               encut = 'ENCUT     = 450'
               prec  = 'PREC      = Normal'
               lreal = 'LREAL     = Auto'
           elif inc == 'INCAR-3':
               encut = 'ENCUT     = 490'
               prec  = 'PREC      = Accurate'
               lreal = 'LREAL     = False'
           elif inc == 'INCAR-4':
               encut = 'ENCUT     = 520'
               prec  = 'PREC      = Accurate'
               lreal = 'LREAL     = False'
           fwincar = open(inc,'w')
           fwincar.write('%-20s \n' % (check_specail_element('POSCAR')))
           fwincar.write('%-20s \n' % (checkmagnetic('POSCAR')))
           fwincar.write(encut)
           fwincar.write('\n')
           fwincar.write(prec)
           fwincar.write('\n')
           fwincar.write(lreal)
           fwincar.write('\n')
           fwincar.write('EDIFF     = 1.0e-05 \n')
           fwincar.write('EDIFFG    = -0.01 \n')
           fwincar.write('%-20s \n' % (setnpar(checkcluster())))
           fwincar.write('KPAR      = 2 \n')
           fwincar.write('NSW       = 100 \n')
           fwincar.write('IBRION    = 2 \n')
           fwincar.write('ISIF      = 3 \n')
           fwincar.write('NELMIN    = 5 \n')
           fwincar.write('NELMDL    = 6 \n')
           fwincar.write('LMAXMIX   = 4 \n')
           fwincar.write('AMIX      = 0.2 \n')
           fwincar.write('BMIX      = 0.00001 \n')
           fwincar.write('AMIX_MAG  = 0.8 \n')
           fwincar.write('BMIX_MAG  = 0.0001 \n')
           fwincar.write('LCHARG    = .FALSE. \n')
           fwincar.write('LWAVE     = .FALSE. \n')
           fwincar.write('ISMEAR    = 0 \n')
           fwincar.write('SIGMA     = 0.05 \n')
           fwincar.write('GGA       = PS')
           fwincar.close()
    elif calculations == 'phonon':
       os.system('mkdir phonon')
       os.system('cp CONTCAR-4 phonon/POSCAR-prim')
       frincar = open('INCAR-4')
       fwincar = open('phonon/INCAR','w')
       for line in frincar:
           if 'NSW' in line:
               fwincar.write('NSW       = 0 \n')
           elif 'EDIFF' in line and 'EDIFFG' not in line:
               fwincar.write('EDIFF     = 1.0e-08 \n')
           else:
               fwincar.write(line)
       fwincar.close()
       # fwincar = open('phonon/INCAR','w')
       # fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       # fwincar.write('%-20s \n' % (checkmagnetic('CONTCAR-4')))
       # fwincar.write('ENCUT     = 520 \n')
       # fwincar.write('EDIFF     = 1.0e-08 \n')
       # fwincar.write('EDIFFG    = -0.01 \n')
       # fwincar.write('ISYM      = -1 \n')
       # fwincar.write('%-20s \n' % (setnpar(checkcluster())))
       # fwincar.write('KPAR      = 8 \n')
       # fwincar.write('NSW       = 0 \n')
       # fwincar.write('IBRION    = 2 \n')
       # fwincar.write('ISIF      = 3 \n')
       # fwincar.write('NELMIN    = 5 \n')
       # fwincar.write('NELMDL    = 6 \n')
       # fwincar.write('LMAXMIX   = 4 \n')
       # fwincar.write('AMIX      = 0.2 \n')
       # fwincar.write('BMIX      = 0.00001 \n')
       # fwincar.write('AMIX_MAG  = 0.8 \n')
       # fwincar.write('BMIX_MAG  = 0.0001 \n')
       # fwincar.write('LCHARG    = .FALSE. \n')
       # fwincar.write('LWAVE     = .FALSE. \n')
       # fwincar.write('ISMEAR    = 0 \n')
       # fwincar.write('SIGMA     = 0.05\n')
       # fwincar.write('LREAL     = False \n')
       # fwincar.close()
    elif calculations == 'static':
       fwincar = open('INCAR-self','w')
       fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       fwincar.write('%-20s \n' % (checkmagnetic('CONTCAR-4')))
       fwincar.write('ENCUT     = 520 \n')
       fwincar.write('EDIFF     = 1.0e-08 \n')
       fwincar.write('EDIFFG    = -0.01 \n')
       fwincar.write('%-20s \n' % (setnpar(checkcluster())))
       fwincar.write('KPAR      = 2 \n')
       fwincar.write('NSW       = 0 \n')
       fwincar.write('IBRION    = 2 \n')
       fwincar.write('ISIF      = 3 \n')
       fwincar.write('NELMIN    = 5 \n')
       fwincar.write('NELMDL    = 6 \n')
       fwincar.write('LMAXMIX   = 4 \n')
       fwincar.write('AMIX      = 0.2 \n')
       fwincar.write('BMIX      = 0.00001 \n')
       fwincar.write('AMIX_MAG  = 0.8 \n')
       fwincar.write('BMIX_MAG  = 0.0001 \n')
       fwincar.write('LCHARG    = .FALSE. \n')
       fwincar.write('LWAVE     = .FALSE. \n')
       fwincar.write('ISMEAR    = -5 \n')
       fwincar.write('EMIN      = -10 \n')
       fwincar.write('EMAX      = 15  \n')
       fwincar.write('NEDOS     = 5000 \n')
       fwincar.close()
    elif calculations == 'band':
       os.system('mkdir band')
       os.system('cp CONTCAR-4 band/POSCAR-prim')
       os.system('cp CONTCAR-4 band/POSCAR')
       os.system('cp POTCAR    band/POTCAR')
       fwincar = open('band/INCAR-self','w')
       fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       fwincar.write('%-20s \n' % (checkmagnetic('CONTCAR-4')))
       fwincar.write('ENCUT     = 520 \n')
       fwincar.write('EDIFF     = 1.0e-08 \n')
       fwincar.write('EDIFFG    = -0.01 \n')
       fwincar.write('%-20s \n' % (setnpar(checkcluster())))
       fwincar.write('KPAR      = 2 \n')
       fwincar.write('NSW       = 0 \n')
       fwincar.write('IBRION    = 2 \n')
       fwincar.write('ISIF      = 3 \n')
       fwincar.write('NELMIN    = 5 \n')
       fwincar.write('NELMDL    = 6 \n')
       fwincar.write('LMAXMIX   = 4 \n')
       fwincar.write('AMIX      = 0.2 \n')
       fwincar.write('BMIX      = 0.00001 \n')
       fwincar.write('AMIX_MAG  = 0.8 \n')
       fwincar.write('BMIX_MAG  = 0.0001 \n')
       fwincar.write('ISMEAR    = -5 \n')
       fwincar.write('NEDOS     = 5000 \n')
       fwincar.write('LORBIT    = 10 \n')
       fwincar.write('LWAVE     = .FALSE. \n')
       fwincar.close()
       fwincar = open('band/INCAR-band','w')
       fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       fwincar.write('%-20s \n' % (checkmagnetic('CONTCAR-4')))
       fwincar.write('ISTART    = 1  \n')
       fwincar.write('ICHARG    = 11 \n')
       fwincar.write('ENCUT     = 520 \n')
       fwincar.write('EDIFF     = 1.0e-08 \n')
       fwincar.write('EDIFFG    = -0.01 \n')
       fwincar.write('%-20s \n' % (setnpar(checkcluster())))
       fwincar.write('NSW       = 0 \n')
       fwincar.write('IBRION    = 2 \n')
       fwincar.write('ISIF      = 3 \n')
       fwincar.write('NELMIN    = 5 \n')
       fwincar.write('NELMDL    = 6 \n')
       fwincar.write('LMAXMIX   = 4 \n')
       fwincar.write('AMIX      = 0.2 \n')
       fwincar.write('BMIX      = 0.00001 \n')
       fwincar.write('AMIX_MAG  = 0.8 \n')
       fwincar.write('BMIX_MAG  = 0.0001 \n')
       fwincar.write('LCHARG    = .FALSE. \n')
       fwincar.write('LWAVE     = .FALSE. \n')
       fwincar.write('ISMEAR    = 0 \n')
       fwincar.write('SIGMA     = 0.02\n')
       fwincar.write('LORBIT    = 11 \n')
       fwincar.close()
    elif calculations == 'bandsoc':
       os.system('mkdir bandsoc')
       os.system('cp CONTCAR-4 bandsoc/POSCAR')
       os.system('cp POTCAR    bandsoc')
       fwincar = open('bandsoc/INCAR-self','w')
       fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       fwincar.write('ISPIN     = 2 \n')
       fwincar.write('ENCUT     = 520 \n')
       fwincar.write('EDIFF     = 1.0e-08 \n')
       fwincar.write('EDIFFG    = -0.01 \n')
       fwincar.write('%-20s \n' % (setnpar(checkcluster())))
       fwincar.write('KPAR      = 2 \n')
       fwincar.write('NSW       = 0 \n')
       fwincar.write('IBRION    = 2 \n')
       fwincar.write('ISIF      = 3 \n')
       fwincar.write('NELMIN    = 5 \n')
       fwincar.write('NELMDL    = 6 \n')
       fwincar.write('LMAXMIX   = 4 \n')
       fwincar.write('AMIX      = 0.2 \n')
       fwincar.write('BMIX      = 0.00001 \n')
       fwincar.write('AMIX_MAG  = 0.8 \n')
       fwincar.write('BMIX_MAG  = 0.0001 \n')
       fwincar.write('ISMEAR    = -5 \n')
       fwincar.write('LSORBIT   = .TRUE. \n')
       fwincar.write('LWAVE     = F \n')
       fwincar.close()
       fwincar = open('bandsoc/INCAR-band','w')
       fwincar.write('ISTART    = 1 \n')
       fwincar.write('ICHARG    = 11 \n')
       fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       fwincar.write('ISPIN     = 2 \n')
       fwincar.write('ENCUT     = 520 \n')
       fwincar.write('EDIFF     = 1.0e-08 \n')
       fwincar.write('EDIFFG    = -0.01 \n')
       fwincar.write('%-20s \n' % (setnpar(checkcluster())))
       fwincar.write('NSW       = 0 \n')
       fwincar.write('IBRION    = 2 \n')
       fwincar.write('ISIF      = 3 \n')
       fwincar.write('NELMIN    = 5 \n')
       fwincar.write('NELMDL    = 6 \n')
       fwincar.write('LMAXMIX   = 4 \n')
       fwincar.write('AMIX      = 0.2 \n')
       fwincar.write('BMIX      = 0.00001 \n')
       fwincar.write('AMIX_MAG  = 0.8 \n')
       fwincar.write('BMIX_MAG  = 0.0001 \n')
       fwincar.write('LCHARG    = .FALSE. \n')
       fwincar.write('LWAVE     = .FALSE. \n')
       fwincar.write('ISMEAR    = 0 \n')
       fwincar.write('SIGMA     = 0.02\n')
       fwincar.write('LSORBIT   = .TRUE. \n')
       fwincar.close()
    elif calculations == 'hse':
       os.system('mkdir hse')
       fwincar = open('hse/INCAR-pbe','w')
       fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       fwincar.write('%-20s \n' % (checkmagnetic('CONTCAR-4')))
       fwincar.write('ENCUT     = 400 \n')
       fwincar.write('EDIFF     = 1.0e-08 \n')
       fwincar.write('EDIFFG    = -0.01 \n')
       fwincar.write('%-20s \n' % (setnpar(checkcluster())))
       fwincar.write('KPAR      = 2 \n')
       fwincar.write('NSW       = 0 \n')
       fwincar.write('IBRION    = 2 \n')
       fwincar.write('ISIF      = 3 \n')
       fwincar.write('NELMIN    = 5 \n')
       fwincar.write('NELMDL    = 6 \n')
       fwincar.write('LMAXMIX   = 4 \n')
       fwincar.write('AMIX      = 0.2 \n')
       fwincar.write('BMIX      = 0.00001 \n')
       fwincar.write('AMIX_MAG  = 0.8 \n')
       fwincar.write('BMIX_MAG  = 0.0001 \n')
       fwincar.write('LCHARG    = .True. \n')
       fwincar.write('LWAVE     = .True. \n')
       fwincar.write('ISMEAR    = -5 \n')
       fwincar.close()
       fwincar = open('hse/INCAR-hse','w')
       fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       fwincar.write('%-20s \n' % (checkmagnetic('CONTCAR-4')))
       fwincar.write('ENCUT     = 400 \n')
       fwincar.write('EDIFF     = 1.0e-04 \n')
       fwincar.write('EDIFFG    = -0.01 \n')
       fwincar.write('KPAR      = 2 \n')
       fwincar.write('NSW       = 0 \n')
       fwincar.write('IBRION    = 2 \n')
       fwincar.write('ISIF      = 3 \n')
       fwincar.write('NELMIN    = 5 \n')
       fwincar.write('NELMDL    = 6 \n')
       fwincar.write('LMAXMIX   = 4 \n')
       fwincar.write('LCHARG    = .FALSE. \n')
       fwincar.write('LWAVE     = .FALSE. \n')
       fwincar.write('ISMEAR    = -5 \n')
       fwincar.write('LHFCALC   = .TRUE. \n')
       fwincar.write('HFSCREEN  = 0.2 \n')
       fwincar.write('AEXX      = 0.25 \n')
       fwincar.write('ALGO      = D  \n')
       fwincar.write('TIME      = 0.3 \n')
       fwincar.write('LDIAG     = .TRUE. \n')
       fwincar.write('EMIN      = -10 \n')
       fwincar.write('EMAX      = 15  \n')
       fwincar.write('NEDOS     = 5000 \n')
       fwincar.write('LORBIT    = 11 \n')
       fwincar.close()
    elif calculations == 'bte':
       os.mkdir('bte')
       os.system('cp CONTCAR-4 bte/POSCAR')
       fwincar = open('bte/INCAR','w')
       fwincar.write('ENCUT     = 520 \n')
       fwincar.write('%-20s \n' % (check_specail_element('CONTCAR-4')))
       fwincar.write('%-20s \n' % (checkmagnetic('CONTCAR-4')))
       fwincar.write('EDIFF     = 1.0e-05 \n')
       fwincar.write('EDIFFG    = -0.01 \n')
       fwincar.write('KPAR      = 2 \n')
       fwincar.write('%-20s \n' % (setnpar(checkcluster())))
       fwincar.write('NSW       = 0 \n')
       fwincar.write('IBRION    = 2 \n')
       fwincar.write('NELMIN    = 5 \n')
       fwincar.write('NELMDL    = 6 \n')
       fwincar.write('LMAXMIX   = 4 \n')
       fwincar.write('LCHARG    = .FALSE. \n')
       fwincar.write('LWAVE     = .FALSE. \n')
       fwincar.write('ISMEAR    = -5 \n')
       fwincar.close()

def setpotcar(v,strfile):
#    set potcar
#    v: verstion
    def poten(elem):
       return {
       'Ac': 'Ac',
       'Ag': 'Ag',
       'Al': 'Al',
       'Ar': 'Ar',
       'As': 'As',
       'Au': 'Au',
        'B': 'B',
       'Ba': 'Ba_sv',
       'Be': 'Be',
       'Bi': 'Bi_d',
       'Br': 'Br',
        'C': 'C',
       'Ca': 'Ca_sv',
       'Cd': 'Cd',
       'Ce': 'Ce',
       'Cl': 'Cl',
       'Co': 'Co',
       'Cr': 'Cr_pv',
       'Cs': 'Cs_sv',
       'Cu': 'Cu',
       'Dy': 'Dy_3',
       'Er': 'Er_3',
       'Eu': 'Eu_2',
        'F': 'F',
       'Fe': 'Fe',
       'Ga': 'Ga_d',
       'Gd': 'Gd_3',
       'Ge': 'Ge_d',
        'H': 'H',
       'He': 'He',
       'Hf': 'Hf_pv',
       'Hg': 'Hg',
       'Ho': 'Ho_3',
        'I': 'I',
       'In': 'In_d',
       'Ir': 'Ir',
        'K': 'K_sv',
       'Kr': 'Kr',
       'La': 'La',
       'Li': 'Li_sv',
       'Lu': 'Lu_3',
       'Mg': 'Mg',
       'Mn': 'Mn_pv',
       'Mo': 'Mo_sv',
        'N': 'N',
       'Na': 'Na_pv',
       'Nb': 'Nb_sv',
       'Nd': 'Nd_3',
       'Ne': 'Ne',
       'Ni': 'Ni',
       'Np': 'Np',
        'O': 'O',
       'Os': 'Os_pv',
        'P': 'P',
       'Pa': 'Pa',
       'Pb': 'Pb_d',
       'Pd': 'Pd',
       'Pm': 'Pm_3',
       'Pr': 'Pr_3',
       'Pt': 'Pt',
       'Pu': 'Pu',
       'Rb': 'Rb_sv',
       'Re': 'Re',
       'Rh': 'Rh_pv',
       'Ru': 'Ru_pv',
        'S': 'S',
       'Sb': 'Sb',
       'Sc': 'Sc_sv',
       'Se': 'Se',
       'Si': 'Si',
       'Sm': 'Sm_3',
       'Sn': 'Sn_d',
       'Sr': 'Sr_sv',
       'Ta': 'Ta_pv',
       'Tb': 'Tb_3',
       'Tc': 'Tc_pv',
       'Te': 'Te',
       'Th': 'Th',
       'Ti': 'Ti_sv',
       'Tl': 'Tl_d',
       'Tm': 'Tm_3',
        'U': 'U',
        'V': 'V_sv',
        'W': 'W_sv',
       'Xe': 'Xe',
        'Y': 'Y_sv',
       'Yb': 'Yb_2',
       'Zn': 'Zn',
       'Zr': 'Zr_sv'
    }.get(elem)

    v = 64
    if checkcluster() == 'a6s000254':
       if v == 64:
           poten_path = '/public3/home/a6s000254/software/potpaw64/PBE/'
#       elif v == 'oqmd':
#           poten_path = '/jet/home/jh2336/software/potpaw_PBE_OQMD/'
    elif checkcluster() == 'sch4085':
       if v == 54:
           poten_path = '/public1/home/sch4085/software-sch4085/potpaw_PBE.54'
#       elif v == 'oqmd':
#           poten_path = '/jet/home/jh2336/software/potpaw_PBE_OQMD/'
    print(checkcluster())
    print(poten_path)
    fpos = open(strfile, 'r').readlines()
    i = 0
    elemlist = []
    mplist = []
    potpath = []
    potlist = []
    elemlist  = fpos[5].split()
    for i in range(0,len(elemlist)):
        mplist.append(poten(elemlist[i]))
        print(poten_path)
        potpath.append(poten_path + mplist[i])
        potlist.append(os.path.join(potpath[i], 'POTCAR'))


    dstname = os.path.join('./', 'POTCAR')
    with open(dstname, 'w') as outfile:
         for fname in potlist:
             with open(fname) as infile:
                 for line in infile:
                     outfile.write(line)


    print('potential file', v, 'is adopted')
#########################################


def setpbs():
   if calculations == 'relaxation':
       if checkrelaxation(calculations) == 1:
           sincar = 'for i in 1 1 2 3 4'
       elif checkrelaxation(calculations) == 2:
           sincar = 'for i in 2 3 4'
       elif checkrelaxation(calculations) == 3:
           sincar = 'for i in 3 4'
       elif checkrelaxation(calculations) == 4:
           sincar = 'for i in 4'
       else:
           sincar = 'I can not set incar'
           print('relaxation finished, no need to set INCAR')
       if checkrelaxation(calculations) > 0:
           fw = open('PBS_vasp','w')
           if checkcluster() == 'a6s000254':
               fw.write('#!/bin/bash -l \n')
               fw.write('#SBATCH -p amd_256 \n')
               fw.write('#SBATCH -N 1 \n')
               fw.write('#SBATCH -n 64 \n')
               fw.write('#SBATCH -J ')
               fw.write(jobname)
               fw.write('\n')
               fw.write(' \n')
               fw.write('source /public3/soft/modules/module.sh \n')
               fw.write('module load mpi/oneAPI/2022.1 \n')
               fw.write('export PATH=/public3/home/a6s000254/software-a6s000254/bin-642:$PATH \n')
               fw.write(' \n')
               fw.write('if [ ! -f POSCAR-org ]; then \n')
               fw.write('   cp POSCAR POSCAR-org \n')
               fw.write('fi \n')
               fw.write('cp INCAR-relax  INCAR \n')
               fw.write('\n')
               fw.write('for i in 1 2 3 4 \n')
               fw.write('\n')
               fw.write('do \n')
               fw.write('cp INCAR-$i  INCAR \n')
               fw.write('cp  KPOINTS-$i KPOINTS \n')
               fw.write('mpirun -np  64  vasp_std \n')
               fw.write('cp  CONTCAR   CONTCAR-$i \n')
               fw.write('cp  OUTCAR   OUTCAR-$i \n')
               fw.write('cp  OSZICAR   OSZICAR-$i \n')
               fw.write('cp  CONTCAR    POSCAR \n')
               fw.write('done \n')
               fw.write(' \n')
               fw.write(' \n')
               #fw.write('cp INCAR-static  INCAR \n')
               #fw.write('srun vasp_std \n')
               #fw.write('mv OSZICAR   OSZICAR-static \n')
               #fw.write('mv OUTCAR    OUTCAR-static \n')
               fw.close()
           elif checkcluster() == 'sch4085':
               fw.write('#!/bin/bash \n')
               fw.write('#SBATCH -N 1 \n')
               fw.write('#SBATCH -n 96 \n')
               fw.write('#SBATCH -p v6_384 \n')
               fw.write('#SBATCH -J ')
               fw.write(jobname)
               fw.write('\n')
               fw.write('\n')
               fw.write('source /public1/soft/modules/module.sh \n')
               fw.write('module load mpi/oneAPI/2022.1 \n')
               fw.write('export PATH=/public1/home/sch4085/software-sch4085/vasp.6.3.0/bin:$PATH \n')
               fw.write(' \n')
               fw.write('if [ ! -f POSCAR-org ]; then \n')
               fw.write('   cp POSCAR POSCAR-org \n')
               fw.write('fi \n')
               fw.write('cp INCAR-relax  INCAR \n')
               fw.write('\n')
               fw.write('for i in 1 2 3 4 \n')
               fw.write('\n')
               fw.write('do \n')
               fw.write('cp INCAR-$i  INCAR \n')
               fw.write('cp  KPOINTS-$i KPOINTS \n')
               fw.write('mpirun -np 96 vasp_std \n')
               fw.write('cp  CONTCAR   CONTCAR-$i \n')
               fw.write('cp  OUTCAR   OUTCAR-$i \n')
               fw.write('cp  OSZICAR   OSZICAR-$i \n')
               fw.write('cp  CONTCAR    POSCAR \n')
               fw.write('done \n')
               fw.write(' \n')
               fw.write(' \n')
               #fw.write('cp INCAR-static  INCAR \n')
               #fw.write('mpirun -np 96 vasp_std \n')
               #fw.write('mv OSZICAR   OSZICAR-static \n')
               #fw.write('mv OUTCAR    OUTCAR-static \n')
               fw.close()

   elif calculations == 'band':
       sincar = 'for i in self band'
       fw = open('band/PBS_vasp','w')
       if checkcluster() == 'a6s000254':
           fw.write('#!/bin/bash \n')
           fw.write('#SBATCH -p amd_256 \n')
           fw.write('#SBATCH -N 1 \n')
           fw.write('#SBATCH -n 64 \n')
           fw.write('#SBATCH -J ')
           fw.write(jobname)
           fw.write('\n')
           fw.write('source /public3/soft/modules/module.sh \n')
           fw.write('')
           fw.write('module load mpi/oneAPI/2022.1 \n')
           fw.write('export PATH=/public3/home/a6s000254/software-a6s000254/bin-642:$PATH \n')
           fw.write(' \n')
           fw.write('if [ ! -f POSCAR-org ]; then \n')
           fw.write('   cp POSCAR POSCAR-org \n')
           fw.write('fi \n')
           fw.write('\n')
           fw.write('for i in self band \n')
           fw.write('\n')
           fw.write('do \n')
           fw.write('cp INCAR-$i  INCAR \n')
           fw.write('cp  KPOINTS-$i KPOINTS \n')
           fw.write('mpirun -np 64 vasp_std \n')
           fw.write('cp  EIGENVAL  EIGENVAL-$i \n')
           fw.write('cp  OUTCAR    OUTCAR-$i \n')
           fw.write('cp  OSZICAR   OSZICAR-$i \n')
           fw.write('cp  DOSCAR    DOSCAR-$i \n')
           fw.write('done \n')
           fw.write(' \n')
           fw.write(' \n')
           fw.close()
       elif checkcluster() == 'sch4085':
           fw.write('#!/bin/bash -x \n')
           fw.close() 
   elif calculations == 'phonon':
       fw = open('phonon/PBS_vasp','w')
       if checkcluster() == 'a6s000254':
           fw.write('#!/bin/bash \n')
           fw.write('#SBATCH -p amd_256 \n')
           fw.write('#SBATCH -N 1 \n')
           fw.write('#SBATCH -n 64 \n')
           fw.write('#SBATCH -J phonon \n')
           fw.write('\n')
           fw.write('\n')
           fw.write('source /public3/soft/modules/module.sh \n')
           fw.write('module load mpi/oneAPI/2022.1 \n')
           fw.write('\n')
           fw.write('export PATH=/public3/home/a6s000254/software-a6s000254/bin-642:$PATH \n')
           fw.write('\n')
           fw.write('mpirun -np 64 vasp_std\n')
           fw.close()

       elif checkcluster() == 'sch4085':
           fw.write('#!/bin/bash -l \n')
           fw.write('#SBATCH -N 1 \n')
           fw.write('#SBATCH -n 96 \n')
           fw.write('#SBATCH -p v6_384 \n')
           fw.write(' \n')
           fw.write('source /public1/soft/modules/module.sh \n')
           fw.write('module load mpi/oneAPI/2022.1  \n')
           fw.write('export PATH=/public1/home/sch4085/software-sch4085/vasp.6.3.0/bin:$PATH \n')
           fw.write('\n')
           fw.write('\n')
           fw.write('mpirun -np 96 vasp_std\n')
           fw.close()

def setkpoints():
   if  os.path.exists('POSCAR'):
       if os.stat('POSCAR').st_size != 0 :
           lattice = open('POSCAR', 'r').readlines()
       else:
           print('POSCAR is empty!')
   else:
       print('POSCAR does not exist!')

   scale=float(lattice[1].split()[0])
   a11  = float(lattice[2].split()[0])
   a12  = float(lattice[2].split()[1])
   a13  = float(lattice[2].split()[2])
   a21  = float(lattice[3].split()[0])
   a22  = float(lattice[3].split()[1])
   a23  = float(lattice[3].split()[2])
   a31  = float(lattice[4].split()[0])
   a32  = float(lattice[4].split()[1])
   a33  = float(lattice[4].split()[2])

   x0 =[]
   x1 =[]
   x2 =[]
   x0.extend([float(a11), float(a12), float(a13)])
   x1.extend([float(a21), float(a22), float(a23)])
   x2.extend([float(a31), float(a32), float(a33)])

   natom=0

   atomlist = lattice[6].split()

   for atom in atomlist:
       natom = natom + int(atom)

   l0 = np.linalg.norm(x0)
   l1 = np.linalg.norm(x1)
   l2 = np.linalg.norm(x2)

   N = (l0*l1*l2*8600/natom)**(1.0/3.0)

   k0= int(round(N/l0))
   k1= int(round(N/l1))
   k2= int(round(N/l2))


   if (natom*k0*k1*k2) < 7000:
      klist=[]
      if k0 == k1 and k0 != k2:
         k2=k2+1
      elif k0 == k2 and k0 != k1:
         k1=k1+1
      elif k1 == k2 and k0 != k1:
         k0=k0+1
      elif k0 == k1 and k0 == k2:
         k0=k0+1
         k1=k1+1
         k2=k2+1
      else:
         klist.extend([k0, k1, k2])
         x = min(int(s) for s in klist)
         xind= klist.index(x)
         if xind == 0:
            k0 = k0 + 1
         elif xind == 1:
            k1 = k1 + 1
         else:
            k2 = k2 +1
   faclist = ['0.2', '0.4','0.8','1.0','1.2']
   if calculations == 'relaxation' and checkrelaxation(calculations) == 1:
       for i in range(1,5):
           factor = float(faclist[i])
           kk0 = int(factor*k0)
           kk1 = int(factor*k1)
           kk2 = int(factor*k2)
           if kk0 <1 :
               kk0 = 1
           if kk1 <1 :
               kk1 = 1
           if kk2 <1 :
               kk2 = 1
           kfilename = 'KPOINTS-' + str(i)
           fw = open(kfilename,'w')
           fw.write(kfilename)
           fw.write('\n')
           fw.write('0 \n')
           fw.write('Gamma \n')
           fw.write('%3d %5d %5d \n' % (kk0, kk1, kk2))
           fw.write('0  0  0')
           fw.close()

   if calculations == 'relaxation' and checkrelaxation(calculations) == 2:
       for i in range(2,5):
           factor = float(faclist[i])
           kk0 = int(factor*k0)
           kk1 = int(factor*k1)
           kk2 = int(factor*k2)
           if kk0 <1 :
               kk0 = 1
           if kk1 <1 :
               kk1 = 1
           if kk2 <1 :
               kk2 = 1
           kfilename = 'KPOINTS-' + str(i)
           fw = open(kfilename,'w')
           fw.write(kfilename)
           fw.write('\n')
           fw.write('0 \n')
           fw.write('Gamma \n')
           fw.write('%3d %5d %5d \n' % (kk0, kk1, kk2))
           fw.write('0  0  0')
           fw.close()

   if calculations == 'relaxation' and checkrelaxation(calculations) == 3:
       for i in range(3,5):
           factor = float(faclist[i])
           kk0 = int(factor*k0)
           kk1 = int(factor*k1)
           kk2 = int(factor*k2)
           if kk0 <1 :
               kk0 = 1
           if kk1 <1 :
               kk1 = 1
           if kk2 <1 :
               kk2 = 1
           kfilename = 'KPOINTS-' + str(i)
           fw = open(kfilename,'w')
           fw.write(kfilename)
           fw.write('\n')
           fw.write('0 \n')
           fw.write('Gamma \n')
           fw.write('%3d %5d %5d \n' % (kk0, kk1, kk2))
           fw.write('0  0  0')
           fw.close()

   if calculations == 'relaxation' and checkrelaxation(calculations) == 4:
       for i in range(4,5):
           factor = float(faclist[i])
           kk0 = int(factor*k0)
           kk1 = int(factor*k1)
           kk2 = int(factor*k2)
           if kk0 <1 :
               kk0 = 1
           if kk1 <1 :
               kk1 = 1
           if kk2 <1 :
               kk2 = 1
           kfilename = 'KPOINTS-' + str(i)
           fw = open(kfilename,'w')
           fw.write(kfilename)
           fw.write('\n')
           fw.write('0 \n')
           fw.write('Gamma \n')
           fw.write('%3d %5d %5d \n' % (kk0, kk1, kk2))
           fw.write('0  0  0')
           fw.close()

   if calculations == 'band' or calculations == 'bandsoc':
       for i in range(4,5):
           factor = float(faclist[i])
           kk0 = int(factor*k0)
           kk1 = int(factor*k1)
           kk2 = int(factor*k2)
           if kk0 <1 :
               kk0 = 1
           if kk1 <1 :
               kk1 = 1
           if kk2 <1 :
               kk2 = 1
           if calculations == 'band':
               os.system("mkdir band")
               fw = open('band/KPOINTS-self','w')
#               os.system("aflow --bzd < band/POSCAR-prim > band/BZ.dat")
#               fbz = open('band/BZ.dat','r').readlines()
#               fw2 = open('band/KPOINTS-band','w')
           elif calculations == 'bandsoc':
               fw = open('bandsoc/KPOINTS-self','w')
#               os.system("aflow --bzd < bandsoc/POSCAR > bandsoc/BZ.dat")
#               fbz = open('bandsoc/BZ.dat','r').readlines()
#               fw2 = open('bandsoc/KPOINTS-band','w')
           fw.write('preband \n')
           fw.write('0 \n')
           fw.write('Gamma \n')
           fw.write('%3d %5d %5d \n' % (kk0, kk1, kk2))
           fw.write('0  0  0')

           os.system('cd band | echo -e "303\n" | vaspkit')
           os.system('cp KPATH.in  band/KPOINTS-band')
           fw.close()

           #hsympoint = {}
           #hsymorder = fbz[0].split(')')[1].split()[0].split('-')
           #print(hsymorder[len(hsymorder)-1])
           #for i in range(4,len(fbz)):
           #    if len(fbz[i]) > 5:
           #         hsympoint[(fbz[i].split('!')[1]).strip()] = fbz[i].split('!')[0]
           #for key in hsympoint:
           #    print(key, hsympoint[key])
           #for i in range(3*len(hsymorder)):
           #   if i == 1:
           #        fw2.write('50   ! 50 grids \n')
           #    else:
           #        fw2.write(fbz[i])
           #fw2.close()


   if calculations == 'hse':
      factor = 0.5
      kk0 = int(factor*k0)
      kk1 = int(factor*k1)
      kk2 = int(factor*k2)
      fw = open('hse/KPOINTS','w')
      fw.write('KPOINTS-hse \n')
      fw.write('0 \n')
      fw.write('Gamma \n')
      fw.write('%3d %5d %5d \n' % (kk0, kk1, kk2))
      fw.write('0  0  0')
      fw.close()

   if calculations == 'bte':
      factor = 2.8
      kk0 = int(factor*k0)
      kk1 = int(factor*k1)
      kk2 = int(factor*k2)
      kmax = kk0
      if kk1 > kmax:
          kmax = kk1
      if kk2 > kmax:
          kmax = kk2
      print(kmax)
      if kmax > 41:
         factor = factor * 0.9
      kk0 = int(factor*k0)
      kk1 = int(factor*k1)
      kk2 = int(factor*k2)
      fw = open('bte/KPOINTS','w')
      fw.write('KPOINTS-bte \n')
      fw.write('0 \n')
      fw.write('Gamma \n')
      fw.write('%6d %6d %6d \n' % (kk0, kk1, kk2))
      fw.write('0  0  0')
      fw.close()


def convertPOSCAR():
    os.system('phonopy --symmetry -c POSCAR')
    os.system('cp PPOSCAR POSCAR')


directlist = os.getcwd().split('/')
comname = directlist[len(directlist)-1]
calculations = sys.argv[1]
jobname = comname + '-' + calculations


if checkrelaxation(calculations):
   print(calculations)
   setincar()
   setpbs()
   if calculations == 'relaxation':
       convertPOSCAR()
       setpotcar(64,'POSCAR')
   elif calculations == 'phonon':
       supecellgen()
       os.system('mv POSCAR-0* phonon')
#       os.system('mv disp.yaml phonon')
       os.system('mv phonopy_disp.yaml phonon ')
       # setpotcar(54,'POSCAR')
       os.system('cp POTCAR phonon')
#       os.system('cp KPOINTS-2 phonon/KPOINTS')
       fw = open('phonon/KPOINTS','w')
       fw.write('KPOINTS-phonon \n')
       fw.write('0 \n')
       fw.write('Gamma \n')
       fw.write('4  4  4 \n')
       fw.write('0  0  0')
       fw.close()
   elif calculations == 'bte':
       os.system('cp POTCAR bte')
   elif calculations == 'band':
       os.system('cp POTCAR band')
   elif calculations == 'bandsoc':
       os.system('cp POTCAR bandsoc')
   else:
       setpotcar('oqmd','POSCAR')
   setkpoints()

