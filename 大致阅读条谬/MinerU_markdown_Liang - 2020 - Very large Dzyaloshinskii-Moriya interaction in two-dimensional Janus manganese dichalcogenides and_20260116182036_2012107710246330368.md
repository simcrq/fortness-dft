# Very large Dzyaloshinskii-Moriya interaction in two-dimensional Janus manganese dichalcogenides and its application to realize skyrmion states

Jinghua Liang, $^{1}$  Weiwei Wang $^{2}$ , Haifeng Du, $^{2}$  Ali Hallal, $^{3}$  Karin Garcia, $^{4}$  Mairbek Chshiev $^{5,6}$ , Albert Fert, $^{4,5}$  and Hongxin Yang $^{6,7}$

$^{1}$ Ningbo Institute of Materials Technology and Engineering, Chinese Academy of Sciences, Ningbo 315201, China

<sup>2</sup>Anhui Province Key Laboratory of Condensed Matter Physics at Extreme Conditions, High Magnetic Field Laboratory, Chinese Academy of Sciences and University of Science and Technology of China, Hefei 230026, China

<sup>3</sup>Univ. Grenoble Alpes, CEA, CNRS, Spintec, 38000 Grenoble, France

$^{4}$ DIPC and University of the Basque Country, 2018, San Sebastian, Spain

<sup>5</sup>Unité Mixte de Physique, CNRS, Thales, Université Paris-Saclay, 91767 Palaiseau, France

$^{6}$ Center of Materials Science and Optoelectronics Engineering, University of Chinese Academy of Sciences, Beijing 100049, China

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/fbe7eb4757669afc248bdb0a0ae5afa86f917e83a01aace878a82660ee8ae66d.jpg)


(Received 12 August 2019; revised manuscript received 30 March 2020; accepted 7 April 2020; published 1 May 2020)

The Dzyaloshinskii-Moriya interaction (DMI), which only exists in noncentrosymmetric systems, is responsible for the formation of exotic chiral magnetic states. The absence of DMI in most two-dimensional (2D) magnetic materials is due to their intrinsic inversion symmetry. Here, using first-principles calculations, we demonstrate that significant DMI can be obtained in a series of Janus monolayers of manganese dichalcogenides  $\mathrm{Mn}XY$  ( $X,Y = \mathrm{S}$ , Se, Te,  $X \neq Y$ ) in which the difference between  $X$  and  $Y$  on the opposite sides of Mn breaks the inversion symmetry. In particular, the DMI amplitudes of MnSeTe and MnSTe are comparable to those of state-of-the-art ferromagnet/heavy metal heterostructures. In addition, by performing Monte Carlo simulations, we find that at low temperatures the ground states of the MnSeTe and MnSTe monolayers can transform from ferromagnetic states with wormlike magnetic domains into the skyrmion states by applying an external magnetic field. At increasing temperature, the skyrmion states start fluctuating above  $50\mathrm{K}$  before an evolution to a completely disordered structure at higher temperature. The present results pave the way for new device concepts utilizing chiral magnetic structures in specially designed 2D ferromagnetic materials.

DOI: 10.1103/PhysRevB.101.184401

# I. INTRODUCTION

Chiral magnetic structures such as chiral domain walls [1,2], helical structures [3,4], and magnetic skyrmions [5-7] hold promise for potential applications in future spintronic devices. Microscopically, the Dzyaloshinskii-Moriya interaction (DMI), which favors canted spin configurations, plays an essential role in the formation of such noncollinear magnetic nanostructures. For the presence of DMI, in addition to strong spin-orbit coupling (SOC) and magnetism, the system is required to have broken inversion symmetry [8,9]. Therefore, significant DMI typically arises in noncentrosymmetric bulk magnets [10-12] and at interfaces [13,14] between a ferromagnet and an adjacent layer with strong SOC. Notably, much effort has been devoted to growing multilayer stacks of ferromagnet/heavy metal (FM/HM) heterostructures, e.g., Ir/Co/Pt [15], Ir/Fe/Co/Pt [16], and Pt/Co/MgO [17] multilayers, in order to enhance the interfacial DMI [18].

Two-dimensional (2D) materials are a fascinating class of materials combining an extremely small thickness with novel physical properties related to their 2D character [19]. Recently, experimental progress has led to a breakthrough in

the synthesis of the long-sought 2D magnets, which were first realized in the  $\mathrm{Cr_2Ge_2Te_6}$  bilayers [20] and  $\mathrm{CrI}_3$  monolayers [21] at low temperature, and then in the monolayers of  $\mathrm{VSe}_2$  [22],  $\mathrm{MnSe}_2$  [23], and  $\mathrm{Fe_3GeTe_2}$  [24] around room temperature. The discoveries of these truly 2D magnets have opened up new opportunities for spintronic technology. However, most of the above 2D magnets are centrosymmetric such that the DMI is absent in these structures. It is possible to break the inversion symmetry by modifying the substrate, combining different 2D materials, and applying a bias voltage or strain [25,26]. However, the simplest and most desirable situation should be a 2D magnet with inherent inversion asymmetry, intrinsic DMI, and intrinsic chiral textures.

Recent experiments have demonstrated that Janus monolayers of transition metal dichalcogenides (TMDs), e.g., MoSSe [27,28], can be synthesized by controlling the reaction conditions. The intrinsically broken inversion symmetry, together with the feasibility of tunable electronic properties by a selection of a suitable pair of chalcogen elements [29-31] in the Janus TMD monolayers, inspired us to speculate that large DMI can be obtained in the 2D magnetic Janus materials. With this conjecture, we investigate the structural and magnetic behavior of a series of Janus monolayers of manganese dichalcogenides  $\mathrm{MnXY}$ $(X,Y = \mathrm{S},\mathrm{Se},\mathrm{Te},X\neq Y)$  via first-principles calculations. Strikingly, we find that the

DMI in MnSeTe and MnSTe monolayers is as strong as those in state-of-the-art FM/HM heterostructures. Furthermore, we apply Monte Carlo (MC) simulations to show that magnetic skyrmions can be stabilized in these 2D magnets.

# II. COMPUTATIONAL METHODS

Our first-principles calculations are performed within the framework of density-functional theory (DFT) as implemented in the Vienna ab initio simulation package (VASP) [32]. The electron-core interaction is described by the projected augmented wave (PAW) method [33-35]. The exchange correlation effects are treated with the generalized gradient approximation (GGA) of Perdew, Burke, and Ernzerhof (PBE) [36]. In order to describe well the  $3d$  electrons, we employ the GGA+U method [37] with an effective  $U = 2\mathrm{eV}$  for Mn as reported in the previous studies [38,39]. The energy cutoff for plane wave expansion is set to  $520~\mathrm{eV}$ , and a  $\Gamma$ -centered  $22\times 22\times 1$ $k$ -point mesh is adopted for the Brillouin zone integration. All the structures are fully relaxed until the force acting on each atom is less than  $0.001\mathrm{eV / A}$ . Phonon dispersions are calculated with a  $4\times 4\times 1$  supercell by using the PHONOPY code [40,41] along with the density-functional perturbation theory (DFPT) [42]. We have used the chirality-dependent total energy difference approach to obtain the DMI strength, which has been successfully employed for the DMI calculations in frustrated bulk systems and insulating chiral-lattice magnets [43,44] and adapted to the case of thin films [45,46]. In the calculations of DMI, a  $\Gamma$ -centered  $20\times 5\times 1$ $k$ -point mesh is adopted.

Using the magnetic interaction parameters determined by the first-principles calculations, we apply MC simulations

with the Metropolis algorithm to explore the magnetic states. The investigated systems are gradually cooled down from  $1000\mathrm{K}$  to the required low temperature. For each temperature,  $2\times 10^{5}$  MC steps are employed to thermalize the system. In all MC simulations, a large supercell of  $160\times 160\times 1$  unit cells with periodic boundary conditions is used in order to avoid the nonuniversal effects of boundary conditions. All MC simulations are performed with our JUMAG package [47].

# III. RESULTS AND DISCUSSION

# A. Geometric properties and structural stability

Figures 1(a) and 1(b) show the top and side views of the crystal structure of the MnXY  $(X,Y = \mathrm{S},\mathrm{Se},\mathrm{Te},X\neq Y)$  monolayers. One can see that the Mn atoms with point group  $C_{3v}$  form a hexagonal network sandwiched by two atomic planes of different chalcogen atoms. Note that in our calculations, for the chemical formula MnXY, the lighter chalcogen atom  $X$  is always set in the top layer while the heavier atom  $Y$  is in the bottom layer. The calculations of the phonon spectrum [see Figs. 1(c)-1(e)] indicate that except for MnSSe, the other two monolayers are dynamically stable. For MnSSe, the small negative frequency in the out-of-plane acoustic (ZA) phonon branch around the  $\Gamma$  point [see Fig. 1(e)] is related to the structural instability due to in-plane bending of the two different chalcogen atomic (S/Se) planes, which has also been reported in some nonmagnetic Janus monolayers [29]. The relaxed structural parameters of MnXY monolayers including lattice constants  $a$ ; bond lengths of Mn-  $X(Y)$ ,  $d_{X(Y)}$ ; and tilting angles of atomic planes Mn-  $X(Y)$ -Mn,  $\theta_{X(Y)}$ , are listed in Table I. The lattice constants of MnXY decrease as

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/4c51afb8a752e48b173f7d277b8623128148ecc5abd7886171cfb0fb8305aee6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/11a47b0a872d52d85ee9c5e5afc482c6cd1021d285dfc5fa91fa286d985dcaf7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/52585cf58726d02be9f4d477096e2a27755ed73f4a0d89907d7867eec91c80cc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/4a943da07c24739088547b2d365aacb083cf59f5a937e49443ab1b4569c5562c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/366ecf8dd9a99c1bb581a9902d9a08629a5b39080c635ef2154ef4eca6862192.jpg)



FIG. 1. The top (a) and side (b) views of the crystal structure and the phonon spectra (c-e) for the  $\mathrm{MnXY}$ $(X,Y = \mathrm{S},\mathrm{Se},\mathrm{Te},X\neq Y)$  monolayers. The dashed lines in (a) show the primitive cell. The yellow vectors in (b) indicate the two spin configurations with opposite chirality used to extract the in-plane DMI parameters.



TABLE I. The optimized lattice constants  $a$ , bond lengths of  $\mathrm{Mn - X}(Y)$ ,  $d_{X(Y)}$ , and tilting angles of atom planes  $\mathrm{Mn - X}(Y) - \mathrm{Mn}$ ,  $\theta_{X(Y)}$ , of  $\mathrm{MnXY}$  monolayers.


<table><tr><td>Pattern</td><td>a(Å)</td><td>dX(Å)</td><td>dY(Å)</td><td>θX(deg)</td><td>θY(deg)</td></tr><tr><td>MnSeTe</td><td>3.68</td><td>2.52</td><td>2.74</td><td>51.88</td><td>58.53</td></tr><tr><td>MnSTe</td><td>3.60</td><td>2.38</td><td>2.74</td><td>48.31</td><td>59.90</td></tr><tr><td>MnSSe</td><td>3.50</td><td>2.38</td><td>2.50</td><td>51.15</td><td>55.64</td></tr></table>

a function of the sum of  $X$  and  $Y$  atomic radii, and for a given MnXY monolayer,  $d_{X}$  and  $\theta_{X}$  are always smaller than  $d_{Y}$  and  $\theta_{Y}$ , respectively, due to the smaller atomic radius of the  $X$  atom compared to that of  $Y$  atom. Similar relationships of structural parameters are also found in the nonmagnetic Janus TMD monolayers [29-31]. The asymmetry between the top and bottom layers in MnXY materials breaks the inversion symmetry, thus allowing the DMI between the Mn ions, as we demonstrate in the following discussions.

# B. Spin model and magnetic parameters

In order to explore the magnetic properties of Janus MnXY monolayers, we fit the following model Hamiltonian for the spins of Mn atoms in the hexagonal structure:

$$
\begin{array}{l} H = - \sum_ {\langle i, j \rangle} \boldsymbol {D} _ {\mathrm {i j}} \cdot (\boldsymbol {S} _ {i} \times \boldsymbol {S} _ {j}) - J \sum_ {\langle i, j \rangle} \boldsymbol {S} _ {i} \cdot \boldsymbol {S} _ {j} - \lambda \sum_ {\langle i, j \rangle} S _ {i} ^ {z} S _ {j} ^ {z} \\ - K \sum_ {i} \left(S _ {i} ^ {z}\right) ^ {2} - \mu_ {\mathrm {M n}} B \sum_ {i} S _ {i} ^ {z}, \tag {1} \\ \end{array}
$$

with the results of our DFT calculations. In Eq. (1)  $S_{i}$  is a three-dimensional unit vector representing the orientation of the spin of the ith Mn atom, and  $\langle i,j\rangle$  refers to nearest-neighbor Mn atom pairs. The first three magnetic interaction terms including the DMI, the Heisenberg isotropic exchange, the anisotropic symmetric exchange, and the easy axis single ion anisotropy are characterized by the parameters  $D_{\mathrm{ij}}$ ,  $J$ ,  $\lambda$ , and  $K$  in the corresponding terms. The last term is the Zeeman interaction, where  $\mu_{\mathrm{Mn}}$  and  $B$  represent the magnetic moment of the Mn atoms and the external magnetic field, respectively.

We first discuss the DMI, which is the most interesting parameter for this work. According to Moriya's symmetry rules [9], since the reflection planes pass through the middle of the bonds between two adjacent Mn atoms, the DMI vector  $D_{\mathrm{ij}}$  for each pair of nearest-neighbor Mn atoms is perpendicular to their bonds. Thus  $D_{\mathrm{ij}}$  can be expressed as  $D_{\mathrm{ij}} = d_{//}(\hat{\mathbf{u}}_{\mathrm{ij}} \times \hat{\mathbf{z}}) + d_{\mathrm{ij},z}\hat{\mathbf{z}}$  with  $\hat{\mathbf{u}}_{\mathrm{ij}}$  being the unit vector between sites  $i$  and  $j$  and  $\hat{\mathbf{z}}$  indicating normal to the plane. The in-plane component  $d_{//}$  along with the associated SOC energy  $\Delta E_{\mathrm{soc}}$  can be evaluated by the chirality-dependent total energy difference approach [45,46] with the two spin configurations depicted by yellow arrows in Fig. 1(b). Here we adopt the sign convention such that  $d_{//} < 0$  ( $d_{//} > 0$ ) favors spin canting with clockwise (counterclockwise) chirality. To calculate the out-of-plane component  $d_{\mathrm{ij},z}$ , we can use the relation  $d_{\mathrm{ij},z} \approx d_{//} / \tan \tilde{\theta}_{\mathrm{ij}}$  [26], where  $\tilde{\theta}_{\mathrm{ij}} = (\theta_{\mathrm{ij},X} + \theta_{\mathrm{ij},Y}) / 2$  represents the average of the tilting angle of the atomic plane  $(\mathrm{Mn})_i - X(Y) - (\mathrm{Mn})_j$ . Note that although we include  $d_{\mathrm{ij},z}$  in the following MC simulations, it does not play any dominant role since the sign of  $d_{\mathrm{ij},z}$  changes

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/e632f739a9f70a2c14b66e056b6ee98799c2cb3c97fe0984df46f5f3d920bc60.jpg)



FIG. 2. The calculated in-plane DMI parameters  $d_{//}$  of the Janus MnXY monolayers. Here  $d_{//} < 0$  ( $d_{//} > 0$ ) favors spin canting with clockwise (counterclockwise) chirality. The inset shows the DMI vectors  $D_{\mathrm{ij}}$  (blue vectors) between the nearest neighbors of Mn atoms (red balls). For clarity, the chalcogen atoms are omitted.


in a staggered way for the six nearest neighbors of the Mn atoms, leading to a vanishing  $d_{\mathrm{ij},z}$  in average.

Figure 2 presents the calculated in-plane DMI component  $d_{//}$  of Janus MnXY monolayers with the DMI vectors  $D_{\mathrm{ij}}$  between the nearest neighbors of Mn atoms schematically shown in the inset. It is remarkable that all Janus MnXY monolayers have strong DMIs, especially for MnSeTe and MnSTe whose magnitude of  $d_{//}$  reaches 2.14 and  $2.63~\mathrm{meV}$ , respectively. These values are comparable to many state-of-the-art FM/HM heterostructures, e.g., Co/Pt ( $\sim 3.0~\mathrm{meV}$ ) [17,45] and Fe/Ir(111) ( $\sim 1.7~\mathrm{meV}$ ) [48] thin films that serve as prototype multilayer systems to host skyrmion states. Even for MnSSe with the weakest DMI among the investigated 2D magnets, the magnitude of  $d_{//}$  ( $0.39~\mathrm{meV}$ ) is larger than that of the graphene/Co system ( $\sim 0.16~\mathrm{meV}$ ), for which DMI-induced chiral domain walls have been reported recently [46].

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/c1f254d6299a9ff1f8d7484337b72bdbbf732bcf53124da58e68889f38e35a58.jpg)



FIG. 3. Atomic-layer-resolved localization of the DMI associated SOC energy  $\Delta E_{\mathrm{soc}}$  for the Janus MnXY monolayers. As can be seen  $\Delta E_{\mathrm{soc}}$  is dominated by heavy chalcogen atom  $Y$ .



TABLE II. The calculated parameters of exchange coupling  $J$ , anisotropic symmetric exchange  $\lambda$ , and easy axis single ion anisotropy  $K$ , and the magnetic moments  $\mu_{\mathrm{Mn}}$  of Mn atoms.


<table><tr><td>Structure</td><td>J (meV)</td><td>λ (meV)</td><td>K (meV)</td><td>μMn (μB)</td></tr><tr><td>MnSeTe</td><td>13.26</td><td>0.16</td><td>0.37</td><td>3.68</td></tr><tr><td>MnSTe</td><td>10.52</td><td>0.004</td><td>0.29</td><td>3.64</td></tr><tr><td>MnSSe</td><td>15.60</td><td>0.12</td><td>0.07</td><td>3.42</td></tr></table>

To elucidate the origin of the exceptional DMI in Janus MnXY monolayers, we plot their associated SOC energy  $\Delta E_{\mathrm{soc}}$  in Fig. 3. One can see that in all MnXY monolayers the dominant contribution to DMI stems from the adjacent heavy  $Y$  atom, especially the heavy Te atom in MnSeTe and MnSTe which makes their DMI magnitudes much larger than that of MnSSe. Similar behavior has been identified for the FM/HM heterostructures [45], where  $\Delta E_{\mathrm{soc}}$  is dominated by the heavy

$5d$  transition metal at the interfacial layer. This is the so-called Fert-Levy mechanism of DMI which can be understood by considering that the heavy chalcogen atoms (5d transition metals in the FM/HM heterostructures) act as spin-orbit active sites to induce the spin-orbit scattering necessary for the DMI [9,49].

In Table II, we summarize the remaining magnetic interaction parameters of the exchange coupling  $J$ , the anisotropic symmetric exchange  $\lambda$ , and the easy axis single ion anisotropy  $K$  as calculated with the method illustrated in the Supplemental Material [50], and the magnetic moments  $\mu_{\mathrm{Mn}}$  of Mn atoms. All MnXY monolayers are ferromagnetic with  $J > 0$  and have an out-of-plane easy axis with both  $\lambda$  and  $K$  being positive. Moreover, the calculated Curie temperature  $T_{c}$  (see Table S1 in [50]) of MnSeTe, MnSTe, and MnSSe is 170, 140, and  $190~\mathrm{K}$ , respectively. Interestingly, previous studies [51] and our calculations show that tensile strain can enhance the exchange interactions in the manganese dichalcogenide monolayers, which indicate that  $T_{c}$  of the Janus MnXY


MnSeTe


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/003c632b2faa298ff70ac8ec532eb5b762f7280313111f16fa91fae88fa507fe.jpg)



MnSTe


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/6882e8857da00950aec2131c3a58b305aad597c004abfcfa839705d2b0ac4c7c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/7d47d149e3443731fb9bf7f509a61a97743768f74782ea136585f263aede4c17.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/9376e43657ac7451b4d2ad8fde01dd3965d14991579bcc9fb290908c3612fc9b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/14195a420a8dee0435ba2be6ffbbf650bc4a4b307edd1f3ea311f6adfb364297.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/a4f8ee29e48dc8a952fe9390601eaf0d97b75d14d9facc1a30c95d237946efd5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/856d47d23849efb07e1af139910a001e057f91a106f6477c00dd5d2b85972de6.jpg)



FIG. 4. Spin textures for (a-c) MnSeTe and (d-f) MnSTe monolayers in real-space. The corresponding temperatures and external fields for the simulations are labeled inside each panel. The color map indicates the out-of-plane spin component of Mn atoms.


monolayers can be increased close to the room temperature by appropriate change of system parameters (Fig. S2 in Ref. [50]).

# C. Spin textures from Monte Carlo simulations

Once all the parameters in the spin Hamiltonian are determined, we can perform MC simulations starting from an initial disordered state at  $1000\mathrm{K}$  to check whether it is possible to stabilize chiral spin textures in the MnXY monolayers. Moreover, we note that while the DMI/exchange ratios  $|d_{/ / } / J|$  of MnSSe is only about 0.03, those of MnSeTe and MnSTe can reach 0.16 and 0.25, respectively, which are within or larger than the typical range of 0.1-0.2 for the formation of skyrmions [52]. We thus only consider MnSeTe and MnSTe monolayers in the following discussions.

Our simulations immediately reveal that, in both systems, at low temperature (10 K) and in zero field, we obtain a ferromagnetic state with wormlike domains separated by chiral Néel domain walls (DWs), the thin white lines between domains of up and down magnetizations in Figs. 4(a) and 4(d). Notably, the size of the domain in MnSeTe is much larger than in MnSTe, which is consistent with the smaller DMI/exchange ratio,  $|d_{/ / } / J|$ , and the resulting larger DW energy in MnSeTe compared with MnSTe. We have also found that different initial random spin configurations can lead to different shapes and different orientations of the domains.

More importantly, next we find that, in both MnSeTe and MnSTe, skyrmion states can be induced by external magnetic fields as in many magnetic systems with skyrmions [15-17]. For the MnSeTe monolymer, applying a field shrinks the red domains [see Fig. 4(a)] and isolated skyrmions begin to appear at about  $0.05\mathrm{T}$ . The worm domains completely disappear above  $0.15\mathrm{T}$  and we show in Fig. 4(b) a typical image of the disordered assembly of skyrmions in a ferromagnetic background observed between 0.2 and  $0.4\mathrm{T}$ . Above  $0.4\mathrm{T}$ , the density of skyrmions decreases and a uniform ferromagnetic state without skyrmions is set above  $0.6\mathrm{T}$ . The diameters of the skyrmions (diameter of the white circle with in-plane magnetization) decrease from 6.6 to  $5\mathrm{nm}$  between 0.2 and  $0.55\mathrm{T}$ .

For MnSTe, we find a similar tendency evolving from a ferromagnetic state with worm domains at low field [see Fig. 4(d)], to a lattice of skyrmions for fields in the  $1.4 - 1.8$  T range [see Fig. 4(e)]. The density of skyrmions increases as the field increases from 1.4 to  $1.8\mathrm{T}$  and they finally tend to form an approximate hexagonal lattice. Their diameter decreases from about 8 to  $7\mathrm{nm}$  at increasing field. The crossover from individual skyrmions in MnSeTe to the skyrmion lattice [53] is consistent with the larger DMI in MnSTe.

As the temperature increases, the images of the skyrmions in MnSTe and MnSTe begin to be less well defined above about  $50\mathrm{K}$  and become more and more blurred, as shown in Figs. 4(c) and 4(f) for  $T = 150\mathrm{K}$ . This blurring expresses the destabilization of the skyrmions by thermal fluctuations. To obtain more quantitative information on the thermal destabilization of the skyrmions, we have derived from our simulations the temperature and field dependence of topological charge,  $Q = \frac{1}{4\pi}\int S\cdot (\partial_xS\times \partial_yS)dxdy$  [54,55], of MnSTe per supercell. The skyrmion lattice phase of MnSTe corresponds to the blue area shown in the phase diagram of Fig. 5. Here

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/a6d77ee8-200d-4a0a-a90f-77d94cbe25e6/2a178d6dc03ef008e3a53a424cb29c5f64bfd5b046e1b7f88a272cdff6b45914.jpg)



FIG. 5. The topological charge  $Q$  per supercell of MnSTe monolayers as a function of temperature and external magnetic field, calculated from MC simulations.


an external field  $B$  pointing upwards along the out-of-plane direction leads to skyrmions with  $Q = -1$ . One can clearly see from Fig. 5 that, approximately above  $1\mathrm{T}$  and below  $125\mathrm{K}$ , there is a large blue area associated with significant negative  $Q$  in the  $B-T$  plane, which signals the formation of the skyrmion states [26 in Fig. 4(e) corresponding to  $Q = -26$ ]. We also find that in this area, for a fixed  $B$ , the number of skyrmions in the system does not change significantly as the temperature is increased up to  $90\mathrm{K}$ . When the temperature is further increased, the magnitude of  $Q$  starts decreasing and eventually goes to zero. The decrease of the magnitude of  $Q$  is associated with a fluctuation-disordered state [see Fig. 4(f) for  $B = 1.5\mathrm{T}$  and  $T = 150\mathrm{K}$ ], where the skyrmion lifetime is finite. Similar relations between thermal fluctuation of skyrmions and the evolution of the density of topological charge were already discussed in [56,57]. We note that the temperature dependence of magnetic parameters [58] can also affect the thermal stability of the skyrmion at finite temperature. Since the calculation of the temperature dependence of exchange interactions is outside the scope of the present study, we would leave it for future research.

The most interesting skyrmions for applications are the individual skyrmions which can be manipulated individually in devices such as racetrack memories or logic components [59]. Such individual skyrmions are those shown in Fig.4(b) for MnSeTe. The field range  $(0.2 - 0.4\mathrm{T})$  in which they exist in MnSeTe is somewhat higher than the typical range  $(0.02 - 0.08\mathrm{T})$  found in metallic multilayers [59]. This can be a disadvantage for applications. A possible way for the reduction of the DMI and the corresponding reduction of the field scale in MnSeTe can be the use of proximity effects by integration in van der Waals heterostructures. In addition, there are several alternative approaches to replacing an applied field for the stabilization of skyrmions. For instance, one can use exchange biasing with an antiferromagnet as proposed recently [60] and demonstrated for the stabilization of skyrmions in zero field.

Exchange biasing with a ferromagnetic layer has also been demonstrated [61].

# IV. CONCLUSION

In summary, using first-principles calculations we demonstrated that strong DMI can be obtained in Janus MnXY monolayers with inherent inversion asymmetry. We find that the strong DMI stems from the large SOC in the heavy chalcogen atoms. The MC simulations show that, in the low field limit, MnSeTe and MnSTe host wormlike domains separated by a chiral Néel domain wall. Moreover, an external field can break the wormlike domains and create skyrmion states in these two monolayer structures.

As compared with FM/HM multilayers fabricated with stacks of different materials to enhance the DMI and generate skyrmions, using a single 2D material as the MnXY monolayers is a simpler situation and can probably be beneficial for a low density of defects. Moreover, our MnXY monolayers can be integrated in van der Waals heterostructures [19,62] to extend their properties. One also knows from theoretical calculations by Gmitra and Fabian [63] that the proximity of graphene with a TMD can induce a large spin-orbit splitting of the Dirac cone of graphene with creation of Rashba-like

Fermi contours. For the current-induced motion of skyrmions in MnXY, this gives the possibility of injecting a spin current into the MnXY layers by using the Edelstein effect [64] of the Rashba-like electrons in graphene. Altogether, our calculation results suggest that the Janus MnXY monolayers are good candidates for spintronic nanomaterials and nanodevices.

Note added. After submission of this work, two articles have appeared on complimentary studies discussing Janus 2D ferromagnets with strong DMI and metastable skyrmions [65,66].

# ACKNOWLEDGMENTS

We thank O. Boulle and L. Buda-Prejbeanu for helpful discussions and acknowledge financial support from the National Natural Science Foundation of China (11874059), Zhejiang Province Natural Science Foundation of China (LR19A040002), and Key Research Program of Frontier Sciences, CAS, Grant No. ZDBS-LY-7021. We also acknowledge the support from DARPA TEE program, DIPC and University of the Basque Country, and Horizon 2020 Research and Innovation Programme under Grant Agreement No. 785219 (Graphene Flagship).



[1] A. Thiaville, S. Rohart, É. Jué, V. Cros, and A. Fert, Europhys. Lett. 100, 57002 (2012).





[2] K.-S. Ryu, L. Thomas, S.-H. Yang, and S. Parkin, Nat. Nanotechnol. 8, 527 (2013).





[3] M. Bode, M. Heide, K. von Bergmann, P. Ferriani, S. Heinze, G. Bihlmayer, A. Kubetzka, O. Pietzsch, S. Blügel, and R. Wiesendanger, Nature 447, 190 (2007).





[4] C. S. Spencer, J. Gayles, N. A. Porter, S. Sugimoto, Z. Aslam, C. J. Kinane, T. R. Charlton, F. Freimuth, S. Chadov, S. Langridge, J. Sinova, C. Felser, S. Blügel, Y. Mokrousov, and C. H. Marrows, Phys. Rev. B 97, 214406 (2018).





[5] A. N. Bogdanov and D. A. Yablonskii, Sov. Phys. JETP 68, 101 (1989).





[6] S. Muhlbauer, B. Binz, F. Jonietz, C. Pfleiderer, A. Rosch, A. Neubauer, R. Georgii, and P. Boni, Science 323, 915 (2009).





[7] X. Z. Yu, N. Kanazawa, Y. Onose, K. Kimoto, W. Z. Zhang, S. Ishiwata, Y. Matsui, and Y. Tokura, Nat. Mater. 10, 106 (2010).





[8] I. Dzyaloshinsky, J. Phys. Chem. Solids 4, 241 (1958).





[9] T. Moriya, Phys. Rev. 120, 91 (1960).





[10] V. E. Dmitrienko, E. N. Ovchinnikova, S. P. Collins, G. Nisbet, G. Beutier, Y. O. Kvashnin, V. V. Mazurenko, A. I. Lichtenstein, and M. I. Katsnelson, Nat. Phys. 10, 202 (2014).





[11] G. Beutier, S.P. Collins, O.V. Dimitrova, V.E. Dmitrienko, M.I. Katsnelson, Y.O. Kvashnin, A.I. Lichtenstein, V.V. Mazurenko, A.G.A. Nisbet, E.N. Ovchinnikova, and D. Pincini, Phys. Rev. Lett. 119, 167201 (2017).





[12] J. Miyawaki, S. Suga, H. Fujiwara, M. Urasaki, H. Ikeno, H. Niwa, H. Kiuchi, and Y. Harada, Phys. Rev. B 96, 214420 (2017).





[13] J. Cho, N. Kim, S. Lee, J. Kim, R. Lavrijsen, A. Solignac, Y. Yin, D. Han, N. J. J. van Hoof, H. J. M. Swagten, B. Koopmans, and C. You, Nat. Commun. 6, 7635 (2015).





[14] X. Ma, G. Yu, C. Tang, X. Li, C. He, J. Shi, K. L. Wang, and X. Li, Phys. Rev. Lett. 120, 157204 (2018).





[15] C. Moreau-Luchaire, C. Moutafis, N. Reyren, J. Sampaio, C. A. F. Vaz, N. Van Horne, K. Bouzehouane, K. Garcia, C. Deranlot, P. Warnicke, P. Wohlhuber, J.-M. George, M. Weigand, J. Raabe, V. Cros, and A. Fert, Nat. Nanotechnol. 11, 444 (2016).





[16] A. Soumyanarayanan, M. Raju, A. L. Gonzalez Oyarce, A. K. C. Tan, M.-Y. Im, A. P. Petrovic, P. Ho, K. H. Khoo, M. Tran, C. K. Gan, F. Ernult, and C. Panagopoulos, Nat. Mater. 16, 898 (2017).





[17] O. Boulle, J. Vogel, H. Yang, S. Pizzini, D. de Souza Chaves, A. Locatelli, T. O. Mentes, A. Sala, L. D. Buda-Prejbeanu, and O. Klein et al., Nat. Nanotechnol. 11, 449 (2016).





[18] H. X. Yang, O. Boulle, V. Cros, A. Fert, and M. Chshiev, Sci. Rep. 8, 12356 (2018).





[19] K. S. Novoselov, A. Mishchenko, A. Carvalho, and A. H. Castro Neto, Science 353, aac9439 (2016).





[20] C. Gong, L. Li, Z. Li, H. Ji, A. Stern, Y. Xia, T. Cao, W. Bao, C. Wang, Y. Wang, Z. Q. Qiu, R. J. Cava, S. G. Louie, J. Xia, and X. Zhang, Nature 546, 265 (2017).





[21] B. Huang, G. Clark, E. Navarro-Moratalla, D. R. Klein, R. Cheng, K. L. Seyler, D. Zhong, E. Schmidgall, M. A. McGuire, D. H. Cobden, W. Yao, D. Xiao, P. Jarillo-Herrero, and X. Xu, Nature 546, 270 (2017).





[22] M. Bonilla, S. Kolekar, Y. Ma, H. C. Diaz, V. Kalappattil, R. Das, T. Eggers, H. R. Gutierrez, M.-H. Phan, and M. Batzill, Nat. Nanotechnol. 13, 289 (2018).





[23] D. J. O'Hara, T. Zhu, A. H. Trout, A. S. Ahmed, Y. K. Luo, C. H. Lee, M. R. Brenner, S. Rajan, J. A. Gupta, D. W. McComb, and R. K. Kawakami, Nano Lett. 18, 3125 (2018).





[24] Y. Deng, Y. Yu, Y. Song, J. Zhang, N. Z. Wang, Z. Sun, Y. Yi, Y. Z. Wu, S. Wu, J. Zhu, J. Wang, X. H. Chen, and Y. Zhang, Nature 563, 94 (2018).





[25] W. Yao, D. Xiao, and Q. Niu, Phys. Rev. B 77, 235406 (2008).





[26] J. Liu, M. Shi, J. Lu, and M. P. Anantram, Phys. Rev. B 97, 054416 (2018).





[27] A.-Y. Lu, H. Zhu, J. Xiao, C.-P. Chuu, Y. Han, M.-H. Chiu, C.-C. Cheng, C.-W. Yang, K.-H. Wei, Y. Yang, Y. Wang, D. Sokaras, D. Nordlund, P. Yang, D. A. Muller, M.-Y. Chou, X. Zhang, and L.-J. Li, Nat. Nanotechnol. 12, 744 (2017).





[28] J. Zhang, S. Jia, I. Kholmanov, L. Dong, D. Er, W. Chen, H. Guo, Z. Jin, V. B. Shenoy, L. Shi, and J. Lou, ACS Nano 11, 8192 (2017).





[29] Y. C. Cheng, Z. Y. Zhu, M. Tahir, and U. Schwingenschlögl, Europhys. Lett. 102, 57001 (2013).





[30] Q.-F. Yao, J. Cai, W.-Y. Tong, S.-J. Gong, J.-Q. Wang, X. Wan, C.-G. Duan, and J. H. Chu, Phys. Rev. B 95, 165401 (2017).





[31] C. Xia, W. Xiong, J. Du, T. Wang, Y. Peng, and J. Li, Phys. Rev. B 98, 165424 (2018).





[32] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).





[33] G. Kresse and J. Hafner, Phys. Rev. B 47, 558 (1993).





[34] G. Kresse and J. Hafner, Phys. Rev. B 49, 14251 (1994).





[35] G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).





[36] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).





[37] V. I. Anisimov, F. Aryastiawan, and A. I. Lichtenstein, J. Phys.: Condens. Matter 9, 767 (1997).





[38] W. Zhou and S. Li, J. Magn. Magn. Mater. 395, 166 (2015).





[39] X. Sui, T. Hu, J. Wang, B.-L. Gu, W. Duan, and M.-S. Miao, Phys. Rev. B 96, 041410(R) (2017).





[40] A. Togo, F. Oba, and I. Tanaka, Phys. Rev. B 78, 134106 (2008).





[41] A. Togo and I. Tanaka, Scr. Mater. 108, 1 (2015).





[42] S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, Rev. Mod. Phys. 73, 515 (2001).





[43] J. H. Yang, Z. L. Li, X. Z. Lu, M.-H. Whangbo, S.-H. Wei, X. G. Gong, and H. J. Xiang, Phys. Rev. Lett. 109, 107203 (2012).





[44] H. J. Xiang, E. J. Kan, S.-H. Wei, M.-H. Whangbo, and X. G. Gong, Phys. Rev. B 84, 224429 (2011).





[45] H. X. Yang, A. Thiaville, S. Rohart, A. Fert, and M. Chshiev, Phys. Rev. Lett. 115, 267210 (2015).





[46] H. X. Yang, G. Chen, A. A. C. Cotta, A. T. N'Diaye, S. A. Nikolaev, E. A. Soares, W. A. A. Macedo, K. Liu, A. K. Schmid, A. Fert, and M. Chshiev, Nat. Mater. 17, 605 (2018).





[47] https://github.com/ww1g11/JuMag.jl.





[48] B. Dupe, M. Hoffmann, C. Paillard, and S. Heinze, Nat. Commun. 5, 4030 (2014).





[49] A. Fert and P. M. Levy, Phys. Rev. Lett. 44, 1538 (1980).





[50] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.101.184401 for (1) the calculations of magnetic interaction parameters  $J$ ,  $\lambda$ , and  $K$ ; (2) the calculations of Curie temperature.





[51] M. Kan, A. Adhikari, and Q. Sun, Phys. Chem. Chem. Phys. 16, 4990 (2014).





[52] A. Fert, V. Cros, and J. Sampaio, Nat. Nanotechnol. 8, 152 (2013).





[53] A Siemens, Y Zhang, J Hagemeister, E. Y. Vedmedenko1, and R. Wiesendanger, New J. Phys. 18, 045021 (2016).





[54] B. Berg and M. Luscher, Nucl. Phys. B 190, 412 (1981).





[55] G. Yin, Y. Li, L. Y. Kong, R. K. Lake, C. L. Chien, and J. D. Zang, Phys. Rev. B 93, 174403 (2016).





[56] L. Rózsa, E. Simon, K. Palotás, L. Udvardi, and L. Szunyogh, Phys. Rev. B 93, 024417 (2016).





[57] W. T. Hou, J. X. Yu, M. Daly, and J. Zang, Phys. Rev. B 96, 140403(R) (2017).





[58] A. Szilva, M. Costa, A. Bergman, L. Szuynogh, L. Nordstrom, and O. Eriksson, Phys. Rev. Lett. 111, 127204 (2013).





[59] A. Fert, N. Reyren, and V. Cros, Nat. Rev. Mater. 2, 17031 (2017).





[60] K. Gaurav Rana, A. Finco, F. Fabre, S. Chouaieb, A. Haykal, L. D. Buda-Prejbeanu, O. Fruchart, S. Le Denmat, P. David, M. Belmeguenai, T. Denneulin, R. E. Dunin-Borkowski, G. Gaudin, V. Jacques, and O. Boulle, arXiv:2001.00912 [Phys. Rev. Applied (to be published)].





[61] W. Legrand, D. Maccariello, F. Ajejas, S. Collin, A. Vecchiola, K. Bouzehouane, N. Reyren, V. Cros, and A. Fert, Nat. Mater. 19, 34 (2020).





[62] A. K. Geim and I. V. Grigorieva, Nature 499, 419 (2013).





[63] M. Gmitra and J. Fabian, Phys. Rev. B 92, 155403 (2015).





[64] A. Soumyanarayanan, N. Reyren, and A. Fert, Nature 539, 509 (2016).





[65] C. Xu, J. Feng, S. Prokhorenko, Y. Nahas, H. Xiang, and L. Bellaiche, Phys. Rev. B 101, 060404(R) (2020).





[66] J. Yuan, Y. Yang, Y. Cai, Y. Wu, Y. Chen, X. Yan, and L. Shen, Phys. Rev. B 101, 094420 (2020).

