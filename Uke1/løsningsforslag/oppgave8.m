
f = imread('mona.png');

noiseFactor = 10;
[N,M] = size(f);
fNoisy = double(f) + noiseFactor .* randn(N,M); 

% Nå kan fNoisy ha verdier over og under [0,255].
% Det er mulig å transformere fNoisy  slik at minste og største verdi til fNoisy
% blir henholdsvis 0 og 255.
% Transformasjonen kommer vi tilbake til senere i emnet:
fNoisy = (fNoisy - min(fNoisy(:))) ./ (max(fNoisy(:))- min(fNoisy(:))) .* 255;

% Merk at i denne oppgaven er det viktigste at du får til at bildet
% kan ha opp til 2**bit antall verdier

for ii = 1:2:8
    bit = ii; 
    f_requantized = floor(fNoisy./(2^(8-bit))); 
    
    % Vis resultat:
    figure()
    imagesc(f_requantized); colormap('gray');
    title(sprintf('bit = %d, antall mulige verdier = %d', bit, max(f_requantized(:))+1))
end
