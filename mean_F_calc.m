% to calculate total amount of partial melting given thickness of oceanic
% crust
rho_crust=2880;% density of oceanic crust in kg/m3
g=9.8;% accelration due to gravity
%% Po and Pf are dependent on the composition fugacity oxygen, or presence of water.
% standad values can be used or can be computed (e.g pmelts need to know how to)
Po=2.75; % pressure at intersection of solidus. Essensially pressure at which melting starts (P in GPa)
Pf=0.2;% pressure at which melting stops (P in GPa)
% these values of Po and Pf are from Asimow et al.,1999,2001 
%%
hc=6.5;% thickness of oceanic crust

%% Calculating mean fractional melting
F_mean= (hc*rho_crust*g)/((Po-Pf)*10^4) % Based on Afonso,s G3 paper about LitMod
