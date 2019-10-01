% Script to calculate chemical variation of  solid and melt phases due to
% partial melting based on Langmuir et al.,1992 fromAfons,s G3 LitMod paper

% read the database percentage of oxides in source (solid) and bulk
% partition coefficient of oxides


%PUM Hart and Zindler(1986)
%       SiO2  Al2O3   FeO   Mg0   CaO Na2O
x_s_o=[45.96  4.06   7.54  37.80 3.21 0.03] % initial concentration of oxides in the original source (wt%)
x_s_i=[] % concentration of oxides in the solid after partial melting (wt%)
x_l_i=[] % concentration of oxides in the liquid (wt%)
F_mean=10: %mean fractional melting
P=10; % Pressure in kilobars
%% Bulk Partition Coefficients for major oxides Niu [1997]
%  oxide      a         b         c       d
%  DSiO 2 = 0·8480 − 0·2200F + 0·0055P
%D_SiO2=

x_s_i(1,1)= 0.8480 - 0.2200*F_mean + 0.0055*P
x_s_i(1,2)= 0.1064 - 0.2200*F_mean + 0.0055*P
x_s_i(1,3)= 0.8480 - 0.2200*F_mean + 0.0055*P
x_s_i(1,4)= 0.8480 - 0.2200*F_mean + 0.0055*P
x_s_i(1,5)= 0.8480 - 0.2200*F_mean + 0.0055*P
x_s_i(1,6)= 0.8480 - 0.2200*F_mean + 0.0055*P