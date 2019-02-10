img = imread('mona.png');
if ndims(img) > 2
    img = rgb2gray(img);
end

[p, bins] = oppgave2_hist(img);

% For aa sammenligne med imhist fra Mathworks:
[h1, bins1] = imhist(img);
p1 = h1 ./ numel(img);

figure()

subplot(1,2,1)
bar(bins1, p1)
title('imhist (normalisert)')

subplot(1,2,2)
bar(bins, p1)
title('oppgave2\_hist')

% Sjekker om oppgave2_hist og imhist gjoer det samme:
thr = 1e-10;
test = all(abs(p1 - p) < thr);
if test == false
    error('oppgave2\_hist og imhist gjoer ikke det samme')
end
