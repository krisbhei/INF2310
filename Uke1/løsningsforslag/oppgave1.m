img = imread('mona.png');
[N,M] = size(img); 

f_out = zeros(N,M);
for i = 2:N 
    for j = 1:M 
        f_out(i,j) = f(i,j) - f(i-1, j);
    end
end

% Bilde med bias (merk at dette er noedvendig _kun_ hvis du bruker image
bias = 128;

figure()
imshow(f_out + bias, [])
colormap(gray(256))

% Bilde uten bias, fremvist ved bruk av imagesc (ikke noedvendig med bias)
figure()
imagesc(f_out)
colormap('gray')