G = 256;
intensiteter = linspace(0,G-1,G);

img = imread('mona.png');

gauss = @(x,mu,std) exp(-0.5.*((x-mu)./std).^2)./sqrt(2*pi*std^2);
mu = input('Middelverdi = ');
std_ = input('Standardavvik = ');

q = gauss(intensiteter,mu,std_);
q = q./sum(q);

img_T = histogramtilpasning(img,q);


fprintf('Sum av ønsket histogram: %g\n',sum(q));
fprintf('Middelverdi til transformert bilde: %g\n',mean2(img_T));
fprintf('Standardavvik til transformert bilde: %g\n',std2(img_T));


plot_histogramtransformert(img,img_T,q)



