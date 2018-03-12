close all; clear all

img_rgb = imread('rose_rgb.png');
img_rgb = double(img_rgb);
img_rgb = img_rgb./max(max(max(img_rgb)));

[N,M,~] = size(img_rgb);

img_ihs = zeros(N,M,3);

for x=1:N
    for y=1:M
        R = img_rgb(x,y,1);
        G = img_rgb(x,y,2);
        B = img_rgb(x,y,3);
        
        thr = 1e-7;
        
        if (abs(R - G) < thr) & (abs(G-B) < thr)
            H = 361;
        else
            th = acos(0.5*((R-G) + (R-B))/sqrt((R-G)^2 + (R-B)*(G-B)));
            th = th*180/pi;
            
            H = th;
            if B > G
                H = 360 - H;
            end
        end
        
        if R+G+B < thr
            S = 0;
            I = 0;
        else
            S = 1 - 3*min([R,G,B])/(R+G+B);
            I = (R+G+B)/3;
        end
        
        img_ihs(x,y,1) = I;
        img_ihs(x,y,2) = H;
        img_ihs(x,y,3) = S;
    end
end

% Vis fram IHS:
titles = {'Intensitet I',...
          'Metning (saturation) S',...
          'Dominerende boelgelengde (hue) H'};
figure()

for i=1:3
    subplot(2,3,i)
    imagesc(img_ihs(:,:,i))
    title(titles{i})
    axis off
    colormap(gray(256))
end

subplot(2,3,5)
axis off
imagesc(img_rgb)
title('Original RGB-bilde')

% Lagre intensitet-komponenten I fra IHS:
figure()

imagesc(img_ihs(:,:,1))
colormap(gray(256))
axis off 

saveas(gcf,'rose_gray.png')

% Finn histogram - noe tilsvarende som fra Uke 3 - oppgave 2
G = 256;
bins = linspace(0,G-1,G);

R_hist = histogram_img(round(255*img_rgb(:,:,1)),G);
G_hist = histogram_img(round(255*img_rgb(:,:,2)),G);
B_hist = histogram_img(round(255*img_rgb(:,:,3)),G);

I_hist = histogram_img(round(255*img_ihs(:,:,1)),G);

% Vis frem histogrammene
figure()

subplot(1,3,1)
hold on 
bar(bins,R_hist,'FaceColor',[1 0 0],'FaceAlpha',0.3,'EdgeColor','none')
bar(bins,G_hist,'FaceColor',[0 1 0],'FaceAlpha',0.3,'EdgeColor','none')
bar(bins,B_hist,'FaceColor',[0 0 1],'FaceAlpha',0.3,'EdgeColor','none')
title('Histogram av R,G og B komponent')
legend('R','G','B')

subplot(1,3,2)
bar(bins,I_hist,'FaceColor',[0 0 0],'EdgeColor','none')
title('Histogram av I - komponent')

subplot(1,3,3)
hold on
bar(bins,R_hist,'FaceColor',[1 0 0],'FaceAlpha',0.3,'EdgeColor','none')
bar(bins,G_hist,'FaceColor',[0 1 0],'FaceAlpha',0.3,'EdgeColor','none')
bar(bins,B_hist,'FaceColor',[0 0 1],'FaceAlpha',0.3,'EdgeColor','none')
bar(bins,I_hist,'FaceColor',[0 0 0],'FaceAlpha',0.3,'EdgeColor','none')
title('Histogram av I,R,G og B komponent')
legend('R','G','B','I')

% gir transformasjonen mening?
% Mulig aa regne tilbake for aa sjekke. (gitt at transformasjonen tilbake
% blir implementert riktig...)

img_ihs_inv = zeros(N,M,3);

for x = 1:N
    for y = 1:M
        I = img_ihs(x,y,1);
        H = img_ihs(x,y,2);
        S = img_ihs(x,y,3);
        
        if H == 361 % programmet har faatt graatone
            R = I; G = I; B = I;
        elseif H <= 120
            H_rad = H*pi/180;
            H_rad2 = (60 - H)*pi/180;
            
            R = I*(1 + S*cos(H_rad)/cos(H_rad2));
            B = I*(1-S);
            G = 3*I - (R+B);
            
        elseif H <= 240
            H_rad = (H-120)*pi/180;
            H_rad2 = (60 - (H-120))*pi/180;
            
            R = I*(1-S);
            G = I*(1 + S*cos(H_rad)/cos(H_rad2));
            B = 3*I - (R+G);
        else
            H_rad = (H-240)*pi/180;
            H_rad2 = (60 - (H-240))*pi/180;
            
            G = I*(1-S);
            B = I*(1 + S*cos(H_rad)/cos(H_rad2));
            R = 3*I - (B+G);
        end
        
        img_ihs_inv(x,y,:) = [R,G,B];
    end
end

% Teste om transformen fra IHS til RGB gir omtrentlig samme resultat som
% original RGB-bilde

err = abs(img_rgb - img_ihs_inv);
fprintf(['Stoerste feil fra RGB til IHS og tilbake til RGB: ' num2str(max(max(max(err)))) '\n']);

figure()

subplot(1,3,1)
imagesc(img_ihs_inv)
title('Fra RGB til IHS og tilbake til RGB')

subplot(1,3,2)
imagesc(img_rgb)
title('Opprinnelig RGB')

subplot(1,3,3)
imagesc(err)
title('Differense mellom bildene')



        


