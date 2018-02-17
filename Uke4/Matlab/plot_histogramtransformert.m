
% plot_histogramtransformert(img,img_T,q)
% Plotter det originale bildet img mot det histogramtilpassede bildet, samt
% bildenes normaliserte og kumulative histogram.
%
% Argumenter:
%   * img: Det originale bildet.
%   * img_T: Det histogramtilpassede bildet.
%   * q: Histogrammet img var ment å tilpasses til. 
% Returnerer:
%   Ingenting. Kun ett vindu skal fremvises av funksjonen.     
function plot_histogramtransformert(img,img_T,q)
    G = 256;
    intensiteter = linspace(0,G-1,G);

    [p,c] = finn_histogram_bilde(img);
    [p_T,c_T] = finn_histogram_bilde(img_T);

    figure()
    colormap gray

    subplot(3,2,1)
    imagesc(img_T)
    axis off
    title('Transformert bilde')

    subplot(3,2,2)
    imagesc(img)
    axis off
    title('Original bilde')

    subplot(3,2,3)
    bar(intensiteter,p_T)
    xlim([0 255])
    title('Histogram til det transformerte bildet')
    hold on
    plot(intensiteter,q,'r','LineWidth',2)
    legend({'bildets','ønsket'});

    subplot(3,2,4)
    bar(intensiteter,p)
    xlim([0 255])
    title('Histogram til det originale bildet')

    subplot(3,2,5)
    bar(intensiteter,c_T)
    xlim([0 255])
    title('Kumulativ histogram til det transformerte bildet')
    hold on
    plot(intensiteter,cumsum(q),'r')
    legend({'bildets','ønsket'});

    subplot(3,2,6)
    bar(intensiteter,c)
    xlim([0 255])
    title('Kumulativ histogram til det originale bildet')
end
