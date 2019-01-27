D = 10*1e-3;    % m
f = 50*1e-3;    % m
s = 5;          % m
lmb = 500*1e-9; % m

% a)
y = s*1.22*lmb/D;
fprintf('deloppgave a: y = %g \n',y);

% b)
y_ = y*f/(s-f);
fprintf('deloppgave b: y = %g \n',y_)

% c)
T_o = y_;
f_o = 1/T_o;
fprintf('deloppgave c: T_o = %g, f_o = 1/T_o = %g \n',T_o,f_o)

% d)
grense = T_o/2;
fprintf('deloppgave d: minste avstand mellom samplingselementer: %g\n', grense)

% e)
b = 16*1e-3; % m
l = 24*1e-3; % m
fprintf('deloppgave e: antall elementer for aa oppfylle samplingsteoremet: %g x %g \n',b/grense,l/grense)

% f)
fprintf('deloppgave f: \nb): y'' doblet\nc): T_o doblet, f_o halvparten\nd): doblet minste avstand\n')

% g)
fprintf('deloppgave g: bedre fordi minste avstand for aa skille to punkter vil bli mindre\n')

