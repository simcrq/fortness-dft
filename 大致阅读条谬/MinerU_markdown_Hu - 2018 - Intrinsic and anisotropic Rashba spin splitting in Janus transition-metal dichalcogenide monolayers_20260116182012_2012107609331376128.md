# Intrinsic and anisotropic Rashba spin splitting in Janus transition-metal dichalcogenide monolayers

Tao Hu, $^{1,2}$  Fanhao Jia, $^{1,2}$  Guodong Zhao, $^{1,2}$  Jiongyao Wu, $^{1,2}$  Alessandro Stroppa, $^{1,3}$  and Wei Ren $^{1,2,4,*}$

$^{1}$ Department of Physics, and International Center of Quantum and Molecular Structures, Shanghai University, Shanghai 200444, China

$^{2}$ Materials Genome Institute, and Shanghai Key Laboratory of High Temperature Superconductors, Shanghai University, Shanghai 200444, China

$^{3}$ CNR-SPIN c/o Università degli Studi dell'Aquila, Via Vetoio 10, I-67010 Coppito (L'Aquila), Italy

$^{4}$ State Key Laboratory of Solidification Processing, Northwestern Polytechnical University, Xi'an 710072, People's Republic of China

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/5d3e5a6fa0ac007ae12e47533b0e1ce6c8d946c409c2d261d5a951fd620380ec.jpg)


(Received 18 March 2018; published 4 June 2018)

Transition-metal dichalcogenides (TMDs) monolayers have been considered as important two-dimensional semiconductor materials for the study of fundamental physics in the field of spintronics. However, the out-of-plane mirror symmetry in TMDs may constrain electrons' degrees of freedom and it may limit spin-related applications. Recently, a newly synthesized Janus TMDs MoSSe was found to intrinsically possess both the in-plane inversion and the out-of-plane mirror-symmetry breaking. Here we performed first-principles calculations in order to systematically investigate the electronic band structures of a series of Janus monolayer TMDs with chemical formula  $MXY$  ( $M = \mathrm{Mo}$ , W and  $X, Y = \mathrm{S}$ , Se, Te). It is found that they possess robust electronic properties like their parent phases. We explored also the effect of perpendicular external electric field and in-plane biaxial strain on the Rashba spin splittings. The Zeeman-type spin splitting and valley polarization at  $K(K')$  point are well preserved and we observed a Rashba-type spin splitting around the  $\Gamma$  point for all the  $MXY$  systems. We have also found that these spin splittings can be enhanced by an external electric field collinear with the local electric field derived by the polar bonds and by the compressive strain. The Rashba parameters change linearly with the external electric field, but nonlinearly with the biaxial strain. The compressive strain is found to enhance significantly the anisotropic Rashba spin splitting.

DOI: 10.1103/PhysRevB.97.235404

# I. INTRODUCTION

Spintronics based on two-dimensional (2D) materials has drawn increasing interests in the last decade [1]. Transition-metal dichalcogenides (TMDs), such as  $\mathrm{MoS}_2$ , have been regarded as a remarkable platform for future electronic applications due to two inherent characteristics [2,3]. One is that monolayer TMDs lack in-plane inversion symmetry, which introduces new degrees of freedom for the electrons. The other characteristic is that TMDs materials may have strong spin-orbit coupling (SOC) [4]. Together, the in-plane inversion symmetry breaking and a strong SOC effect lead to Zeeman-type spin and valley coupling physics in TMDs monolayers [5]. However, Rashba-type spin splitting [6-8], which appears due to the internal electric field, does not always intrinsically appear in the TMDs. The main reason is that generally TMDs materials possess out-of-plane mirror symmetry [9].

Therefore, great efforts have been made to break the out-of-plane mirror symmetry, by which extra degrees of freedom of electrons could be induced. For example, combining  $\mathrm{MoS}_2$  with different materials, such as graphene [10], bismuth (111) [11], and ferromagnet CoFeB [12], one can consider van der Waals heterostructures. Furthermore, external electric field (EEF) is also an easy way to break the vertical mirror symmetry [13-15]. The Rashba-type spin splitting is also found in trimerized  $1T\text{-MoS}_2$ , which is polar TMD because of

non-mirror-symmetric S atoms on the top and bottom sides of Mo [16].

Recently, a ternary compound MoSSe has been synthesized, namely Janus TMD, in which top-layer S atoms of  $\mathrm{MoS}_2$  are fully replaced by Se atoms [17]. It was also reported that postsynthesis ion-beam-mediated techniques could be employed to obtain Janus TMD samples [18,19]. Owing to the different electronegativity of S and Se, i.e., noncompensating polar bonds, MoSSe has an internal electric field  $(\vec{E}_{\mathrm{int}})$  perpendicular to the monolayer plane. The lack of out-of-plane mirror symmetry leads to the Rashba-type spin splitting in such polar TMD systems. It can be described by the Bychkov-Rashba Hamiltonian [6]

$$
H _ {R} = \alpha_ {R} (| \vec {E} _ {\mathrm {i n t}} |) \vec {\sigma} \cdot (\vec {k} _ {| |} \times \vec {z}),
$$

where the prefactor  $\alpha_{R}$  is the Rashba parameter,  $\vec{\sigma}$  denotes the Pauli matrices,  $\vec{k}_{||}$  is the momentum of the 2D electron, and  $\vec{z} = (0,0,1)$  is the out-of-plane direction. Therefore, the energy versus momentum dispersion relation has an effective form due to the lifted spin degeneracy

$$
E _ {\pm} (k) = \frac {\hbar^ {2} \vec {k} _ {| |} ^ {2}}{2 m ^ {*}} \pm \alpha_ {R} | \Delta k |.
$$

This formula characterizes the Rashba-type spin splitting representing two parabolas shifted with respect to each other by  $\Delta k$  in reciprocal space.

In this work, we systematically investigate the electronic band structure of the Janus TMD monolayers  $MXY$  ( $M = \mathrm{Mo}, \mathrm{W}; X, Y = \mathrm{S}, \mathrm{Se}, \mathrm{Te}$ ) using first-principles

calculations. The structure stabilities of these six  $MXY$  monolayers have been confirmed thorough phonon dispersion computation. Besides the Zeeman-type spin splitting and valley polarization [20] at the  $K(K^{\prime})$  point for  $MX_{2}$ , we have found the Rashba-type spin splitting around the  $\Gamma$  point for all the  $MXY$  systems. Moreover, we further reveal that Rashba parameters  $\alpha_{R}$  can be tuned by lattice strain and external electric field.

# II. COMPUTATIONAL METHODS

First-principle simulations were performed with the projector augmented wave (PAW) approach [21,22] as implemented in the Vienna ab initio simulation package (VASP) [23,24]. The electron exchange-correlation functional was treated by the generalized gradient approximation [25] of Perdew-Burke-Ernzerhof (PBE). The van der Waals interaction was described by the optB86b-vdw functional [26,27]. The energy convergence threshold was set to  $10^{-8}\mathrm{eV}$  and atomic positions were fully relaxed until the maximum force on each atom was less than  $10^{-3}\mathrm{eV} / \AA$ . The energy cutoff was fixed to  $600\mathrm{eV}$  and the Brillouin zone was sampled with a  $15\times 15\times 1$  gamma point centered grid in both geometry optimization and self-consistent calculations. The Gaussian smearing method with a width of  $0.05\mathrm{eV}$  was employed.

The  $MXY$  monolayer was placed in the  $x - y$  plane with the  $z$  direction perpendicular to the layer plane, and a vacuum slab of  $16\AA$  in the  $z$  direction was added to avoid interactions between periodic adjacent layers. Phonon dispersion analysis was performed with a  $4\times 4\times 1$  supercell by using the PHONOPY code [28,29] interfaced with the density-functional perturbation theory [30]. The dipole layer method implemented in VASP is used to introduce the electric field and to correct the dipole moment presented in the  $MXY$  slab due to asymmetric geometry. The direction of positive EEF is defined along the positive  $z$  direction. For strain-modified systems, the biaxial tensile and compressive strains were applied by fixing the lattice constant to a series of values, which are larger or smaller than that of the equilibrium structure. The geometry optimizations were performed after fixing the lattice parameters. According to the crystal symmetry, band structures of  $MXY$  monolayer were calculated along the special lines connecting the following high-symmetry points, namely  $\Gamma (0,0,0)$ ,  $M(0,0.5,0)$ ,  $M^{\prime}(0.5,0,0)$ ,  $K(-1/3,2/3,0)$ , and  $K^{\prime}(1/3,1/3,0)$  in the  $k$  space. To further confirm the electronic properties, screened hybrid functional (HSE06) [31,32] computations were


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/6811f968c8f74d2b978b72d9fbf3351d4e998eaca501e98b3b0313843939c9b5.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/aad8b8af413c9907b435926abf1bec2a7314bd50352b7a1cfefaa7070013da3a.jpg)



FIG. 1. (a) Top and side views of the unit cell of MoSSe monolayer in hexagonal lattice with parameters  $a = b$ . The bond length of Mo-S is smaller than that of Mo-Se ( $l_1 < l_2$ ), thus the distance between different sublayers  $d_1$  is slightly smaller than  $d_2$ . (b) Calculated phonon dispersion for the MoSSe monolayer.


performed. To investigate the Rashba effect and reveal the spin distribution in the momentum space, SOC calculations were performed.

# III. RESULTS AND DISCUSSION

We consider the atomic structure of the MoSSe as a representative of the  $MXY$  systems in Fig. 1(a). From the top view, the MoSSe shows a hexagonal lattice. From the side view, it is easy to distinguish that the bond lengths of Mo-S and Mo-Se are slightly different, and thus the mirror symmetry is broken. The Mo atoms are bonded with three S and three Se atoms on two sides. The point group is  $C_{3v}$  for  $MXY$  monolayers, and the structural parameters of  $MXY$  monolayers are listed in Table I. The lattice constants are gradually increasing with the increase of atomic radii of  $X$  and  $Y$  chalcogenide atoms.

To confirm the structural stability of  $MXY$  systems, we have performed the phonon dispersion calculations along the high-symmetry points in the Brillouin zone. No imaginary frequency is found around the  $\Gamma$  point in  $k$  space for the MoSSe monolayer as shown in Fig. 1(b). A quadratic dispersion is found in the out-of-plane acoustic branch (ZA mode) around the  $\Gamma$  point, which is a universal feature of 2D materials [33,34]. The phonon dispersion of the other five systems are also characterized with no imaginary frequency. This clearly confirms the structural stability of the polar  $MXY$  monolayer. However, a previous study [35] found that two systems (MoSTe


TABLE I. Calculated structural parameters and band gaps of  ${MXY}$  monolayers. The lattice constant  $\left( {a = b}\right)$  ,the bond length of  $M - X\left( {l}_{1}\right)$  and  $M - Y\left( {l}_{2}\right)$  ,and the distance between the sublayers of  $M,X\left( {d}_{1}\right)$  and  $M,Y\left( {d}_{2}\right)$  are shown. The atomic number of  $X$  is smaller than that of  $Y$  in each  ${MXY}$  system,since  ${l}_{1} < {l}_{2},{d}_{1} < {d}_{2}$  . The band gaps of six  ${MXY}$  systems within different functionals (PBE,HSE06,and PBE + SOC) are also displayed. The band-gap values are labeled by letter D or I, which represents the direct or indirect band gap.


<table><tr><td></td><td>a,b(Å)</td><td>l1(Å)</td><td>l2(Å)</td><td>d1(Å)</td><td>d2(Å)</td><td>PBE (eV)</td><td>HSE06 (eV)</td><td>PBE + SOC (eV)</td></tr><tr><td>MoSSe</td><td>3.228</td><td>2.416</td><td>2.530</td><td>1.537</td><td>1.711</td><td>1.63 (D)</td><td>2.10 (D)</td><td>1.27 (I)</td></tr><tr><td>MoSTe</td><td>3.343</td><td>2.432</td><td>2.715</td><td>1.479</td><td>1.909</td><td>1.15 (I)</td><td>1.65 (I)</td><td>0.73 (I)</td></tr><tr><td>MoSeTe</td><td>3.412</td><td>2.552</td><td>2.717</td><td>1.623</td><td>1.871</td><td>1.34 (D)</td><td>1.79 (D)</td><td>0.99 (D)</td></tr><tr><td>WSSe</td><td>3.232</td><td>2.421</td><td>2.538</td><td>1.543</td><td>1.720</td><td>1.77 (D)</td><td>2.27 (D)</td><td>1.23 (D)</td></tr><tr><td>WSTe</td><td>3.344</td><td>2.438</td><td>2.720</td><td>1.488</td><td>1.916</td><td>1.34 (I)</td><td>1.82 (I)</td><td>0.85 (I)</td></tr><tr><td>WSeTe</td><td>3.413</td><td>2.559</td><td>2.722</td><td>1.633</td><td>1.879</td><td>1.42 (D)</td><td>1.88 (D)</td><td>0.84 (D)</td></tr></table>

and MoSeTe) should show a structural instability, according to small negative frequencies displayed around the  $\Gamma$  point. But we agree with works [36,37] which reported that the imaginary frequency of the  $ZA$  mode could be an artifact of the mesh size. Such softening of phonons can be eliminated by improving the calculation parameters and mesh size.

The band gaps of six systems with different computational methods are shown in Table I, among which the WSSe monolayer exhibits the largest band gap. In Figs. 2(a) and 2(b), we show the calculated electronic structures of the WSSe monolayer without and with SOC. The band gaps are 1.77 and  $2.27\mathrm{eV}$  with PBE and HSE06 functionals, respectively, when SOC effect is not included. We note that some of  $MXY$  systems have direct band gap, while the others have indirect band gap. As shown in Fig. 2(b), the Rashba spin splitting around the  $\Gamma$  point is indicated for which the other five systems have also similar splitting but with different magnitude. We have plotted the spin texture of the valence-band maximum (VBM) around the  $\Gamma$  point. From Fig. 2(c), one can see that spin arrows in the zone center are forming a clockwise rotation pattern without the perpendicular component, which confirms the characteristic of Rashba spin splitting.

Figure 2(d) presents a zoom-in of the schematic illustration of the Rashba spin splitting along with related parameters. The Rashba parameter is defined as  $\alpha_{R}^{K} = 2E_{R}^{K} / k_{R}^{K}$  in the  $\Gamma - K$  direction, and  $\alpha_{R}^{M} = 2E_{R}^{M} / k_{R}^{M}$  in the  $\Gamma - M$  direction. It is found that the energy difference  $E_{R}^{K}$  and the momentum offset  $k_{R}^{K}$  are quite close to those of the  $\Gamma - M$  direction  $(E_{R}^{M}, k_{R}^{M})$  for all the six systems. The  $\alpha_{R}^{K}$  values are calculated to be 77, 147,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/63da69adcedadb41962d12b7b67922decc193d476a62356890c8dc5e2205081b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/a7a6b84d74f0c6299d02024d4a1a8692344e96416afcf7be8125a47a147779ff.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/a2af70ca3e6768409cd06a5d39716631a35bbdf938a4e21c056318c58027a92a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/467e629e45ba5397239c7ae89fcccaa194e90a374824ea296ccde8892883e9a6.jpg)



FIG. 2. Calculated electronic band structure of the WSSe monolayer (a) without and (b) with SOC. Two band gaps  $(\Delta_{1}$  and  $\Delta_{2})$  are defined here:  $\Delta_{1}$  is the direct band gap at the  $K$  point and  $\Delta_{2}$  is the band gap between the CBM at the  $K$  point and the VBM around the  $\Gamma$  point. (c) Spin texture of the VBM around the  $\Gamma$  point. The arrows provide the in-plane spin vector orientation and the colors indicate the out-of-plane component of spins. (d) Schematic view of the Rashba spin splitting around the  $\Gamma$  point.  $E_R^K$  and  $E_R^M$  are the energy difference between the energies of the two peaks and the degenerate energy at the  $\Gamma$  point, while  $k_R^K$  and  $k_R^M$  are the momentum offsets in the  $\Gamma - K$  and  $\Gamma - M$  directions.


479, 158, 322, and  $514\mathrm{meV}$  Å for MoSSe, MoSTe, MoSeTe, WSSe, WSTE, and WSeTe, respectively. The  $\alpha_{R}^{M}$  have slightly different values, i.e., 77, 148, 487, 157, 324, and  $524\mathrm{meV}$  Å for MoSSe, MoSTe, MoSeTe, WSSe, WSTE, and WSeTe, respectively. Roughly speaking, the Rashba parameters are not very sensitive to the directions selected in the Brillouin zone for these systems. In general, the  $\alpha_{R}$  value of WXY is larger than that of MoXY with the same chalcogenides due to a larger SOC effect of W than Mo. Considering the SOC strength of chalcogenides parts, the value of  $\alpha_{R}$  increases with the order  $XY = \mathrm{SSe}$ , STe, SeTe as well.

A perpendicular electric field is being considered as an effective approach to increase the degrees of freedom of electrons by breaking the inversion symmetry in 2D electron systems [13,38], which can create and manipulate spin splitting without changing the system's time-reversal invariant symmetry [14]. Previous studies have shown that the magnitude of Rashba-type spin splitting is also tunable by an applied electric field [39,40] which modifies the quantum well asymmetry and electron occupation [41]. In our  $MXY$  systems, we theoretically applied electric field from  $-0.5$  to  $0.5\mathrm{V} / \mathring{\mathrm{A}}$  to tune the Rashba splitting. The positive EEF was set to be pointing from  $Y$  (with larger atomic number) to  $X$ , which allows us to align it parallel to the internal electric field due to the electronegativity  $S > Se > Te$ . We first observe the band gaps changing with the EEF as presented in Figs. 3(a) and 3(b), which can be ascribed to the Stark effect in the condensed matters [42]. Like other 2D materials [43,44], the band gaps  $(\Delta_{1}$  and  $\Delta_{2})$  of  $MXY$  monolayers can be linearly modulated. The band gap  $\Delta_{1}$  at the  $K$  point increases monotonically with the EEF from  $-0.5$  to  $0.5\mathrm{V} / \mathring{\mathrm{A}}$ , while the band gap  $\Delta_{2}$  along  $K - \Gamma$  decreases monotonically. The slopes of the linear relationship between  $\Delta_{1}$  and EEF are 0.004, 0.007, 0.005, 0.008, 0.018, and  $0.012\mathrm{e}\mathring{\mathrm{A}}$  for MoSSe, MoSTe, MoSeTe, WSSe, WSTE, and WSeTe, respectively. And, the slopes of lines for  $\Delta_{2}$  are  $-0.068$ ,  $-0.113$ ,  $-0.084$ ,  $-0.060$ ,  $-0.105$ , and  $-0.073\mathrm{e}\mathring{\mathrm{A}}$  for the six systems, respectively. From the symmetry point of view, the EEF with the same magnitude but different directions ( $z$  or  $-z$ ) should generate the same Stark effect in  $MX_{2}$  TMDs monolayers with an out-of-plane mirror symmetry. However, the  $MXY$  monolayers here have distinctive behaviors due to their intrinsic polar structures and a competition between the EEF and the internal electric field.

By checking the change of charge density of  $X$  and  $Y$  atoms, we found that the charge accumulation on  $X$  (with smaller atomic number) was gradually increasing as the increase of the EEF magnitude. Naturally, we expected that an EEF with the same direction as the local electric field could enhance the Rashba effect. Indeed, our results in Fig. 3(c) reveal that the four out of six Rashba parameters  $\alpha_{R}^{K}$  are increased linearly by the positive EEF, while a negative EEF linearly suppresses the Rashba splitting. This is consistent with a previous work [45], but interestingly for two cases of MSTe we find that the  $\alpha_{R}^{K}$  values are not sensitive to the EEF. On the other hand, the WSeTe monolayer provides the largest change of  $31\mathrm{meV}\AA$  for  $\alpha_{R}^{K}$  modulation by comparing zero field and a large EEF  $(0.5\mathrm{V}/\mathring{\mathrm{A}})$ . We have also calculated the Rashba parameters  $\alpha_{R}^{M}$  of  $MXY$  monolayers along the  $\Gamma - M$  direction. The linear EEF dependences of  $\alpha_{R}^{M}$  are quantitatively the same as those of  $\alpha_{R}^{K}$ ,


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/56a2212594d73158ed1eec1e7f81714fda32329e38c821555ac0561487077097.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/11848277133ef1dad291f0f3310b570067b374a2d4d6b81ac6f53d0a2239df96.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/a9dd35ed4eb19af5db20f178f4c4198e7d8adc3a035e398690a7774370dcc5c1.jpg)



FIG. 3. (a) Band gaps  $\Delta_{1}$  of  $MXY$  monolayers changing with EEF. (b) Band gaps  $\Delta_{2}$  of  $MXY$  monolayers changing with EEF. The two band gaps are defined in Fig. 2. (c) Calculated Rashba parameters  $(\alpha_{R}^{K})$  as a function of external electric field for  $MXY$  monolayers along the  $\Gamma - K$  direction. The linear EEF dependences of  $\alpha_{R}^{M}$  are almost overlapping with those of  $\alpha_{R}^{K}$ , which are not shown here.


which suggests that the EEF does not change the isotropic property of Rashba splitting around the Brillouin-zone center.

To further explore the manipulation of the Rashba spin splitting in Janus TMD monolayers, an in-plane biaxial strain is applied in our calculations. The band structures including SOC for each  $MXY$  monolayer under certain strain (from  $-3$  to  $5\%$ ) are calculated and analyzed. The band-gap evolution as a function of strain is plotted in Fig. 4(a). For MoSeTe, WSSe, and WSeTe monolayers, both compressive and tensile strains reduce the band gaps. But, for MoSSe and WSTe monolayers, a  $1\%$  compressive strain slightly increases the band gaps; for MoSTe the band gap has a maximal value with the compressive strain of  $2\%$ . It is also observed that the strain causes change of band-gap types, i.e., indirect-to-direct or direct-to-indirect transition. We also find that the MoSSe

has a semiconductor-metal transition at  $11\%$  tensile strain, similar to the published results on the pure  $\mathrm{MoS}_2$  [46]. Thus, we might expect that Janus-TMDs preserve some features from its parent-phase TMDs, such as the robust electronic structure [47] and the approximately linear band-gap reduction upon the tensile strain [46,48].

The calculated Rashba parameters  $\alpha_{R}^{K}$  as a function of the biaxial strain are presented in Fig. 4(b). We found that the tensile strain suppresses the Rashba splitting, while a compressive strain enhances the  $\alpha_{R}^{K}$  significantly. In the case of the MoSeTe monolayer, the  $\alpha_{R}^{K}$  is  $479\mathrm{meV}\AA$  at the zero strain condition and it is increased to  $1117\mathrm{meV}\AA$  by a compressive strain of  $3\%$ . In general, Rashba parameters could be largely increased under a  $3\%$  compressive strain. In comparison to the EEF, the strain engineering has a large effect on the tuning of the Rashba spin splittings. A lattice strain of


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/f7049acb1efe01ee9266efb0b2b21c9c269d808b44e66bfb6ceb2bd3b08c833d.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/f3ba093ed733895961116b7f82bb441bad3d3ec59826b4dd2d21adb11590a9ff.jpg)



FIG. 4. (a) Calculated band gaps versus in-plane biaxial strain when the SOC is included. Solid square symbols are for indirect band gap, and open circles represent direct band gap. (b) Calculated Rashba parameters  $\alpha_{R}^{K}$  as a function of in-plane biaxial strain for  $MXY$  monolayers along the  $\Gamma - K$  direction.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/5a902dcf8405a3cfc53b8d021f6b19909977d84885c30908691f46364a675174.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-16/e70f61be-70b2-4bfd-9d68-1ead1520647c/26127a07abcf4fbf2100cb21dae2e66fd61375dac1be72df0d7068f520300acc.jpg)



FIG. 5. (a) Calculated Rashba parameters as a function of in-plane biaxial strain for WSeTe monolayer along the  $\Gamma -K$  and  $\Gamma -M$  directions. (b) Illustration of anisotropic Rashba spin splitting caused by the compressive strain.


$3\%$  can be currently considered in realistic experiments, and such compressive strain would enhance the Rashba parameters in these systems.

We have checked whether the lattice strain has some influence on the calculated Rashba parameters  $\alpha_{R}$  along the  $\Gamma - K$  and  $\Gamma - M$  directions. Figure 5(a) shows  $\alpha_{R}^{K}$  and  $\alpha_{R}^{M}$  values for the WSeTe monolayer as a function of the biaxial strain. Under the compressive strain condition, we find the appearance of anisotropic Rashba splitting as illustrated in Fig. 5(b). From Fig. 5(a) one observes that such anisotropic Rashba parameters become more pronounced with the increase of the compressive strain amplitude. When a  $3\%$  compressive strain is applied, the Rashba parameter difference is calculated to be  $\alpha_{R}^{M} - \alpha_{R}^{K} = 54 \mathrm{meV} \AA$ . To understand this result, we have calculated the bands along the  $\Gamma - K$  and  $\Gamma - M$  paths, and found a substantial energy maximal difference of  $E_{R}^{K} - E_{R}^{M} = 9 \mathrm{meV}$ . The other  $MXY$  monolayers under compressive strain show qualitatively similar but smaller results.

# IV. CONCLUSIONS

In summary, we found the monotonic Stark effect of Janus TMDs, which is due to their intrinsic polar structures and a competition between the EEF and the internal electric field. Our results reveal that Janus TMDs inherit robust electronic structure from their parent-phase TMDs. The Janus TMDs  $MXY$  monolayers intrinsically possess Rashba-type spin splitting due to the out-of-plane mirror-symmetry breaking

and the SOC effect. Six  $MXY$  monolayers show different magnitudes of the splitting quantified by the Rashba parameter  $\alpha_{R}$  as determined by the SOC strength of their constituent elements. It is found that the Rashba effect can be tuned by an external electric field and/or strain engineering. The Rashba spin splitting is found to be enhanced by a positive electric field or a compressive strain. The Rashba parameters have a linear dependence on the external electric field, and a nonlinear response to the lattice strain. Interestingly, we have shown significant anisotropic energy splittings along the  $\Gamma - K$  and  $\Gamma - M$  directions when a 3% compressive strain is applied. We conclude that the strain engineering is an efficient way to control the Rashba spin splitting and it may further enhance anisotropic effects.

# ACKNOWLEDGMENTS

This research was supported by the National Key Basic Research Program of China (Grant No. 2015CB921600), the National Natural Science Foundation of China (Grants No. 11274222 and No. 51672171), and the Eastern Scholar Program from the Shanghai Municipal Education Commission. This work is also a part of the Project funded by China Postdoctoral Science Foundation. The Special Program for Applied Research on Super Computation of the NSFC-Guangdong Joint Fund (the second phase) under Grant No. U1501501, the fund of the State Key Laboratory of Solidification Processing in NWPU (Grant No. SKLSP201703), the supercomputing services from AM-HPC, and Fok Ying Tung education foundation are also acknowledged.



[1] X. Xu, W. Yao, D. Xiao, and T. F. Heinz, Nat. Phys. 10, 343 (2014).





[2] A. F. Morpurgo, Nat. Phys. 9, 532 (2013).





[3] H. Qiu, T. Xu, Z. Wang, W. Ren, H. Nan, Z. Ni, Q. Chen, S. Yuan, F. Miao, F. Song, G. Long, Y. Shi, L. Sun, J. Wang, and X. Wang, Nat. Commun. 4, 2642 (2013).





[4] Z. Y. Zhu, Y. C. Cheng, and U. Schwingenschlögl, Phys. Rev. B 84, 153402 (2011).





[5] D. Xiao, G.-B. Liu, W. Feng, X. Xu, and W. Yao, Phys. Rev. Lett. 108, 196802 (2012).





[6] Y. A. Bychkov and E. I. Rashba, JETP Lett. 39, 78 (1984).





[7] W. Ren, Z. Qiao, J. Wang, Q. Sun, and H. Guo, Phys. Rev. Lett. 97, 066603 (2006).





[8] S. Hu, H. Gao, Y. Qi, Y. Tao, Y. Li, J. R. Reimers, M. Bokdam, C. Franchini, D. Di Sante, A. Stroppa, and W. Ren, J. Phys. Chem. C 121, 23045 (2017).





[9] K. F. Mak and J. Shan, Nat. Photonics 10, 216 (2016).





[10] M. Gmitra and J. Fabian, Phys. Rev. B 92, 155403 (2015).





[11] K. Lee, W. S. Yun, and J. D. Lee, Phys. Rev. B 91, 125420 (2015).





[12] Q. Shao, G. Yu, Y.-W. Lan, Y. Shi, M.-Y. Li, C. Zheng, X. Zhu, L.-J. Li, P. K. Amiri, and K. L. Wang, Nano Lett. 16, 7514 (2016).





[13] S. Wu, J. S. Ross, G.-B. Liu, G. Aivazian, A. Jones, Z. Fei, W. Zhu, D. Xiao, W. Yao, D. Cobden, and X. Xu, Nat. Phys. 9, 149 (2013).





[14] H. Yuan, M. S. Bahramy, K. Morimoto, S. Wu, K. Nomura, B.-J. Yang, H. Shimotani, R. Suzuki, M. Toh, C. Kloc, X. Xu, R. Arita, N. Nagaosa, and Y. Iwasa, Nat. Phys. 9, 563 (2013).





[15] C. Cheng, J.-T. Sun, X.-R. Chen, H.-X. Fu, and S. Meng, Nanoscale 8, 17854 (2016).





[16] E. Bruyer, D. Di Sante, P. Barone, A. Stroppa, M.-H. Whangbo, and S. Picozzi, Phys. Rev. B 94, 195402 (2016).





[17] A.-Y. Lu, H. Zhu, J. Xiao, C.-P. Chuu, Y. Han, M.-H. Chiu, C.-C. Cheng, C.-W. Yang, K.-H. Wei, Y. Yang, Y. Wang, D. Sokaras, D. Nordlund, P. Yang, D. A. Muller, M.-Y. Chou, X. Zhang, and L.-J. Li, Nat. Nanotechnol. 12, 744 (2017).





[18] Q. Ma, M. Isarraraz, C. S. Wang, E. Preciado, V. Klee, S. Bobek, K. Yamaguchi, E. Li, P. M. Odenthal, A. Nguyen, D. Barroso, D. Sun, G. von Son Palacio, M. Gomez, A. Nguyen, D. Le, G. Pawin, J. Mann, T. F. Heinz, T. S. Rahman, and L. Bartels, ACS Nano 8, 4672 (2014).





[19] M. Ghorbani-Asl, S. Kretschmer, D. E. Spearot, and A. V. Krasheninnikov, 2D Mater. 4, 025078 (2017).





[20] H. Zeng, J. Dai, W. Yao, D. Xiao, and X. Cui, Nat. Nanotechnol. 7, 490 (2012).





[21] P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).





[22] G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).





[23] G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).





[24] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).





[25] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).





[26] J. Klimes, D. R. Bowler, and A. Michaelides, J. Phys.: Condens. Matter 22, 022201 (2010).





[27] J. Klimes, D. R. Bowler, and A. Michaelides, Phys. Rev. B 83, 195131 (2011).





[28] A. Togo, F. Oba, and I. Tanaka, Phys. Rev. B 78, 134106 (2008).





[29] A. Togo and I. Tanaka, Scr. Mater. 108, 1 (2015).





[30] S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, Rev. Mod. Phys. 73, 515 (2001).





[31] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 118, 8207 (2003).





[32] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 124, 219906 (2006).





[33] H. Zabel, J. Phys.: Condens. Matter 13, 7679 (2001).





[34] L. Zhu, G. Zhang, and B. Li, Phys. Rev. B 90, 214302 (2014).





[35] Y. C. Cheng, Z. Y. Zhu, M. Tahir, and U. Schwingenschlögl, Europhys. Lett. 102, 57001 (2013).





[36] H. Sahin, S. Cahangirov, M. Topsakal, E. Bekaroglu, E. Akturk, R. T. Senger, and S. Ciraci, Phys. Rev. B 80, 155453 (2009).





[37] C. Kamal and M. Ezawa, Phys. Rev. B 91, 085423 (2015).





[38] J. Wu, Y. Yang, H. Gao, Y. Qi, J. Zhang, Z. Qiao, and W. Ren, AIP Adv. 7, 035218 (2017).





[39] S.-J. Gong, C.-G. Duan, Y. Zhu, Z.-Q. Zhu, and J.-H. Chu, Phys. Rev. B 87, 035403 (2013).





[40] K. V. Shanavas and S. Satpathy, Phys. Rev. Lett. 112, 086802 (2014).





[41] A. Manchon, H. C. Koo, J. Nitta, S. M. Frolov, and R. A. Duine, Nat. Mater. 14, 871 (2015).





[42] M. Ishigami, J. D. Sau, S. Aloni, M. L. Cohen, and A. Zettl, Phys. Rev. Lett. 94, 056804 (2005).





[43] L. Fucai, Z. Jiadong, Z. Chao, and L. Zheng, Adv. Funct. Mater. 27, 1602404 (2016).





[44] B. Ghosh, S. Nahas, S. Bhowmick, and A. Agarwal, Phys. Rev. B 91, 115433 (2015).





[45] Q.-F. Yao, J. Cai, W.-Y. Tong, S.-J. Gong, J.-Q. Wang, X. Wan, C.-G. Duan, and J. H. Chu, Phys. Rev. B 95, 165401 (2017).





[46] M. Ghorbani-Asl, S. Borini, A. Kuc, and T. Heine, Phys. Rev. B 87, 235434 (2013).





[47] T. Lorenz, M. Ghorbani-Asl, J.-O. Joswig, T. Heine, and G. Seifert, Nanotechnology 25, 445201 (2014).





[48] E. Scalise, M. Houssa, G. Pourtois, V. Afanas'ev, and A. Stesmans, Nano Res. 5, 43 (2012).

