clear;
close;
clc;


x = 0:1e-6:7;
%y = x.^2 -7*x +10 + sin(1.5*pi*x);
y = 2*x -7 + 1.5*pi*cos(1.5*pi*x);
figure;
plot(x, y, '-', 'DisplayName', '$f(x)$')
grid on;
grid minor;
axis( [min(x) max(x) min(y) max(y)] );
% legend('Interpreter','latex','Location','northeast');
% title('$f(x) = (x-2)(x-3) + \sin(1.5 \pi x)$','Interpreter','latex','FontSize',14);
% xlabel('$x$','Interpreter','latex','Color','black','FontSize',12);
% ylabel('$f(x)$','Interpreter','latex','Color','black','FontSize',12);
% set(gca,'TickLabelInterpreter','latex', 'FontSize', 12);

for i=1:length(y)
    if abs(y(i)) < 1e-5
        z(i) = y(i);
    end
end