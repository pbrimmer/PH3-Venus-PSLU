# PH3-Venus-PSLU
A PSLU C3 Practical, looking at PH3 in and above the clouds of Venus.

## Learning Goals for these Practicals

- Words.
- Words.

## Pre-Practical Motivation and Review

Take some time to look over [Lincowski, A.P., Meadows, V.S., Crisp, D., Akins, A.B., Schwieterman, E.W., Arney, G.N., Wong, M.L., Steffes, P.G., Parenteau, M.N. and Domagal-Goldman, S., 2021. Claimed detection of PH3 in the clouds of Venus is consistent with mesospheric SO2. The Astrophysical Journal Letters, 908(2), p.L44.](https://iopscience.iop.org/article/10.3847/2041-8213/abde47/meta)

You will be working out their calculation using properties of radiative transfer and lineshapes. These lecture notes [here are a great review for the concepts and implementation](https://cefrc.princeton.edu/sites/g/files/toruqf1071/files/Files/2013%20Lecture%20Notes/Hanson/pLecture6.pdf)

## The Practical

For this practical, clone the repository and start looking at `ph3-pslu.py`. This is the code you will use to calculate the absorption of the phosphine $J=0,1$ transition, using the temperature profile of Venus, `pT-Venus.dat`.

1. Apply the appropriate parameters for the phosphine $J=0,1$ transition using the [JPL database for molecular spectroscopy](https://spec.jpl.nasa.gov/).
1. Find the appropriate profile and calculate the lineshape for an arbitrary constant amount of phosphine.
1. Try a function for phosphine, can be as simple or complex as you like, placing all the phosphine above the clouds, below the clouds, etc.
1. What if ammonia were observed in the clouds of Venus? Find strong transitions using the above JPL database for 23 GHz $< \nu <$ 24.5 GHz. Apply the same calculations for a single, or multiple transitions.
1. Speculate on what implications this may have on the opacity of the IR windows in Venus's atmosphere. Compare the infrared windows of [Arney et al.](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014JE004662) to [ExoMol Database](https://www.exomol.com/) values for ammonia. If you chose a sufficiently universal function for the python code, you can even apply the python code to one of these transitions, in order to predict the opacity effect of ammonia.
