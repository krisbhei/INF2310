img = imread('houses.png');
if ndims(img) == 3
    img = rgb2gray(img);
end
img = double(img);

% Øke kontrast
img_increased_contrast = img*1.5;

% Gjøre bildet lysere
img_brighter = img + 100;

figure()
subplot(2,1,1) % subplot deler et vindu i flere delplott.
imshow(img_increased_contrast,[0 255],'InitialMagnification','fit')
title('Økt kontrast')

subplot(2,1,2)
imshow(img_brighter,[0 255],'InitialMagnification','fit')
title('Økt lyshet')

