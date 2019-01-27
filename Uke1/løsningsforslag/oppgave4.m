f = double(imread('mona.png')); % double for at divisjon ikke avrunder verdier 

for ii = 1:2:8
    bit = ii; 
    f_requantized = floor(f./(2^(8-bit))); % floor kan brukes her til aa 
                                           % avrunde verdiene som om 
                                           % heltallsdivisjon har blitt utfoert 
                                           % paa dette bildet. 

    figure()
    imagesc(f_requantized); colormap('gray');
    title(sprintf('bit = %d, antall verdier = %d', bit, max(f_requantized(:))+1))
end