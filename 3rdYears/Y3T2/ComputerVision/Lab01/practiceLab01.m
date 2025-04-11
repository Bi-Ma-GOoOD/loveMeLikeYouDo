input = imread('scrambled_image.tif');
copy = zeros(size(input));
copy = uint8(copy);

% For Loop
col = 1170;
row = 909;

for i = 1:row
    for j = 1:col
        copy(r(i), c(j), 1) = input(i, j, 1);
        copy(r(i), c(j), 2) = input(i, j, 2);
        copy(r(i), c(j), 3) = input(i, j, 3);
    end
end
imshow(copy);