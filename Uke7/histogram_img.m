function p = histogram_img(img,G)
    bins = linspace(0,G-1,G);
    p = zeros(1,G);
    for i=1:G
        p(i) = sum(sum(img == i-1));
    end
    p = p./numel(img);
end
