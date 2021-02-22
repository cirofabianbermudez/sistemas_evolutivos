%%
clear;
close;
clc;
% syms x;
% eqn = x^2 -7x + 1.5*pi*cos(1.5*pi*x) == 0;
% S = solve(eqn,x)

syms f(x) x;
f(x) = x^2 - 7*x + 10 + sin(1.5*pi*x);
g = diff(f);
x(1)= 6 ;%initial point
for i=1:1000 %it should be stopped when tolerance is reached
        x(i+1) = x(i) - f(x(i))/g(x(i));
        if( abs(f(x(i+1))) < 0.001 )   % tolerance
            disp(double(x(i+1)));
            break;
       end
end