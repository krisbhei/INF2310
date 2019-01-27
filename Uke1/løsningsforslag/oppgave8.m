
f = imread('mona.png');

noiseFactor = 10;
[N,M] = size(f);
fNoisy = double(f) + noiseFactor .* randn(N,M); 

for ii = 1:2:8
    bit = ii; 
    f_requantized = floor(fNoisy./(2^(8-bit))); 
    
    % Vis resultat:
    figure()
    imagesc(f_requantized); colormap('gray');
    title(sprintf('bit = %d, antall verdier = %d', bit, max(f_requantized(:))+1))
end
