function [p, intensities] = oppgave2_hist(img)
    % Anta at bildet har heltallige verdier mellom 0 og 255 
    G = 256;
    
    intensities = 0:(G-1);
    
    p = zeros(G, 1);
    for i = 1:G
        p(i) = sum(sum(img == intensities(i))); 
    end
    
    p = p ./ numel(img);

end