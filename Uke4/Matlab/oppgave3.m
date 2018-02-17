G = 256;
intensiteter = linspace(0,G-1,G);

img = imread('mona.png');

uniform = @(G) ones(1,G)./G;

q = uniform(G);

img_T = histogramtilpasning(img,q);

plot_histogramtransformert(img,img_T,q)
