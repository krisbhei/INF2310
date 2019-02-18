

function img_T = histogramtilpasning(img,q)
	
	% histogramtilpasning(img,q)
	% Histogramtilpasser et innbilde img til et gitt histogram q.
	%
	% Argumenter:
	%   * img: Bildet som skal histogramtilpasses.
	%   * q: Det normaliserte histogrammet img skal tilpasses til.
	% Returnerer:
	%   * img_T: Det histogramtilpassede bildet. 


    % Antar 8-bits bilde 
    G = 256;

    % Finn innbildets histogram og deretter dets kumulative histogram:
    [~,c] = finn_histogram_bilde(img);

    % Finn det kumulative histogrammet til q:
    cq = cumsum(q);
    
    % Transformér innbildet img:
    T = zeros(1,G);

    for i=1:G
        [~,argmin] = min(abs(c(i) - cq));
        T(i) = argmin-1; % -1 fordi utbildet skal ha verdier mellom 0 og 255.
    end
    
    [N,M] = size(img);
    img_T = zeros(N,M);
    
    for i=1:N
        for j=1:M
            img_T(i,j) = T(img(i,j)+1); % +1 fordi img(i,j) er mellom 0 og 255. 
                                        % Null er ikke gyldig indeks i Matlab. 
        end
    end

end
