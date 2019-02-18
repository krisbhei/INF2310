

function [p,c] = finn_histogram_bilde(img)

	% finn_histogram_bilde(img)
	% Finner det normaliserte og kumulative histogrammet til innbildet img
	%
	% Argument:
	%   * img: Bildet som funksjonen skal finne histogrammene til. 
	%          Bildet antas å være i 8-bit
	% Returnerer:
	%   * [p,c]: p er normalisert histogram og c er det kumulative
	%            histogrammet.

	% Anta bildet er 8-bit
    G = 256;
    p = zeros(1,G);
    
    for i=1:G
        p(i) = sum(sum(img == i-1));
    end
    p = p./numel(img);
    
    c = zeros(1,G);
    c(1) = p(1);
    for i=2:G
        c(i) = c(i-1) + p(i);
    end
    
end
